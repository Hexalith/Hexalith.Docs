"""Observe a documentation quickstart without installing or starting services."""

import argparse
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone


MILESTONES = {
    "package": ("package-installed", "sample-returned-expected-result"),
    "tool": ("tool-installed", "command-returned-expected-result"),
    "run": ("prerequisites-ready", "service-ready", "first-call-succeeded"),
    "try-it": (
        "prerequisites-ready",
        "container-start-requested",
        "container-started",
        "cold-build-started",
        "cold-build-finished",
        "services-ready",
        "project-created",
        "same-project-listed",
    ),
}


def probe(command):
    try:
        result = subprocess.run(
            command, capture_output=True, text=True, timeout=10, check=False
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return result.stdout if result.returncode == 0 else None


def preflight(journey):
    reasons = []
    tools = {name: bool(shutil.which(name)) for name in ("dotnet", "aspire", "dapr", "hexalith")}
    if journey in ("package", "tool"):
        if not (probe(["dotnet", "--list-sdks"]) or "").strip():
            reasons.append("The .NET SDK is missing or could not be queried.")
    elif tools["dotnet"]:
        reasons.append("A .NET toolchain is already on PATH.")
    for name in ("aspire", "dapr", "hexalith"):
        if tools[name]:
            reasons.append(f"{name} is already on PATH.")

    home = Path.home()
    cache = Path(os.environ.get("NUGET_PACKAGES", home / ".nuget" / "packages"))
    if cache.is_dir() and any(item.name.lower().startswith("hexalith.") for item in cache.iterdir()):
        reasons.append("The NuGet cache contains Hexalith packages.")
    if (home / ".hexalith").exists() or os.environ.get("HEXALITH_DAPR_HOME"):
        reasons.append("A Hexalith tool directory or isolated Dapr configuration exists.")

    root = probe(["git", "rev-parse", "--show-toplevel"])
    if root and Path(root.strip()).name.lower().startswith("hexalith"):
        reasons.append("The starting directory is a Hexalith checkout.")

    if journey in ("run", "try-it"):
        desktop = shutil.which("code") or Path("/Applications/Visual Studio Code.app").is_dir()
        if not desktop:
            reasons.append("VS Code could not be detected. Verify the desktop installation.")
        images = probe(["docker", "image", "ls", "--format", "{{.Repository}}"])
        if images is None:
            reasons.append("The Docker engine could not be queried.")
        elif any("hexalith" in name.lower() for name in images.splitlines()):
            reasons.append("The Docker engine already contains Hexalith images.")

    print(json.dumps({"journey": journey, "preflight_issues": reasons}, indent=2))
    return 1 if reasons else 0


def confirm(message):
    print(message + " [Enter to record, or type stop]", file=sys.stderr, flush=True)
    line = sys.stdin.readline()
    if not line:
        return False
    return line.strip() == ""


def observe(journey):
    if not confirm("Open the starting page and start the timer"):
        return 1
    start = time.monotonic()
    started_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    marks = {}
    try:
        for milestone in MILESTONES[journey]:
            if not confirm(milestone):
                break
            marks[milestone] = round(time.monotonic() - start, 2)
    except KeyboardInterrupt:
        print("Recording partial run.", file=sys.stderr)
    reached = len(marks) == len(MILESTONES[journey])
    result = {
        "journey": journey,
        "started_at_utc": started_at,
        "elapsed_seconds": round(time.monotonic() - start, 2),
        "milestones_elapsed_seconds": marks,
        "first_result_observed": reached,
    }
    print(json.dumps(result, indent=2))
    return 0 if reached else 1


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("preflight", "observe"))
    parser.add_argument("journey", choices=MILESTONES)
    args = parser.parse_args()
    sys.exit(preflight(args.journey) if args.command == "preflight" else observe(args.journey))
