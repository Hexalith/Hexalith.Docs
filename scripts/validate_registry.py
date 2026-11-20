"""Validate the Docs registry without network access or package dependencies."""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
QUICKSTARTS = {"Use the package", "Run it", "Use the tool"}


def relative_file(path):
    return (isinstance(path, str) and bool(path) and "\\" not in path
            and not PurePosixPath(path).is_absolute()
            and all(part not in {".", "..", ""} for part in path.split("/")))


def validate(registry, root, check_sources=False):
    problems = []
    if not isinstance(registry, dict) or registry.get("schemaVersion") != 1 or not isinstance(registry.get("modules"), list):
        return ["expected schemaVersion 1 and a modules array"]
    declarations = subprocess.run(
        ["git", "config", "-f", str(root / ".gitmodules"), "--get-regexp", r"^submodule\..*\.path$"],
        check=True, text=True, capture_output=True,
    ).stdout.splitlines()
    paths = {}
    for line in declarations:
        path = line.split(maxsplit=1)[1]
        paths[Path(path).name] = path
    expected = dict.fromkeys(paths, "direct")
    expected["Hexalith.Docs"] = "self"
    expected.setdefault("Hexalith.BmadSkills", "external")
    if len(registry["modules"]) != 21:
        problems.append("expected one row for each of the 21 in-scope repositories")
    names = set()
    for row in registry["modules"]:
        if not isinstance(row, dict) or not isinstance(row.get("name"), str):
            problems.append("module requires a repository name")
            continue
        name = row["name"]

        def require(condition, reason):
            if not condition:
                problems.append(f"{name}: {reason}")

        require(name not in names, "duplicate module")
        names.add(name)
        require(name in expected and row.get("checkout") == expected.get(name), "checkout disagrees with .gitmodules and workspace membership")
        description = row.get("description")
        require(isinstance(description, str) and 0 < len(description.strip()) <= 120, "description must be 1–120 characters")
        require(row.get("descriptionStatus") in ("confirmed", "proposed"), "description needs a review status")
        category = row.get("category")
        require("category" in row and ((category is None and row.get("categoryStatus") == "unconfirmed")
                or (category in ("technical", "business") and row.get("categoryStatus") in ("confirmed", "proposed"))), "invalid category or review status")
        blocks = row.get("quickstarts")
        require(isinstance(blocks, list) and all(isinstance(b, str) and b in QUICKSTARTS for b in blocks)
                and len(set(blocks)) == len(blocks), "invalid or duplicate quickstart block")
        require(row.get("ciOwnerTarget") in ("CiCd", "self", "caller"), "unknown CI owner")
        packages = row.get("packages")
        badges = row.get("badges")
        if not isinstance(packages, dict) or not isinstance(badges, dict):
            problems.append(f"{name}: packages and badges are required")
            continue
        ids = packages.get("ids")
        if not isinstance(ids, list) or not all(isinstance(i, str) and re.fullmatch(r"[\w.\-]+", i, re.ASCII) for i in ids):
            problems.append(f"{name}: invalid NuGet package IDs")
            continue
        require(len({i.casefold() for i in ids}) == len(ids) and packages.get("count") == len(ids), "package count or unique IDs disagree")
        require("primary" in packages and (packages["primary"] in ids if ids else packages["primary"] is None), "primary package must belong to this inventory")
        source = packages.get("inventorySource")
        valid_source = relative_file(source) or (isinstance(source, str) and source.startswith("https://"))
        require("inventorySource" in packages and (valid_source if ids else source is None), "package inventory needs a relative path or HTTPS source")
        require(not (isinstance(blocks, list) and "Use the package" in blocks) or bool(ids), "package quickstart needs a package")
        require("workflow" in badges and "licenseFile" in badges and "sonarKey" in badges, "missing badge sources")
        reads = packages.get("projectReadmes")
        if not isinstance(reads, list):
            problems.append(f"{name}: expected projectReadmes array")
            continue
        if all(relative_file(f) for f in reads):
            owners = [PurePosixPath(f).parent.name for f in reads]
            require(all(PurePosixPath(f).name == "README.md" for f in reads) and set(owners) <= set(ids)
                    and len(set(owners)) == len(owners), "per-package README paths must identify distinct inventory IDs")
        files = reads.copy()
        for key in ["appHost", "development", "operations", "devContainer"]:
            require(key in row, "missing " + key)
            if row.get(key) is not None:
                files.append(row[key])
        if badges.get("licenseFile") is not None:
            files.append(badges["licenseFile"])
        if badges.get("workflow") is not None:
            filename = badges["workflow"]
            require(isinstance(filename, str) and "/" not in filename, "badge workflow must be a filename")
            files.append(".github/workflows/" + str(filename))
        if not all(relative_file(f) for f in files):
            problems.append(f"{name}: expected a repository-relative file path")
            continue
        if not check_sources or name not in expected or expected[name] == "external":
            continue
        repo = root / paths[name] if name in paths else root
        if name in paths and not (repo / ".git").exists():
            problems.append(f"{name}: initialize the direct submodule for the source check")
            continue
        for f in files:
            require((repo / f).is_file(), "missing source file " + f)
        if relative_file(source):
            require((repo / source).exists(), "missing inventory source " + source)
            if source.endswith(".json") and (repo / source).is_file():
                manifest = json.loads((repo / source).read_text(encoding="utf-8-sig"))
                require(sorted(ids) == sorted(i["id"] for i in manifest["packages"]), "IDs differ from release manifest")
    for name in sorted(set(expected) - names):
        problems.append(f"missing registry entry for {name}")
    return problems


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=ROOT / "docs/module-registry.json")
    parser.add_argument("--check-sources", action="store_true", help="also check file evidence in initialized direct submodules")
    args = parser.parse_args()
    try:
        data = json.loads(args.registry.read_text())
        problems = validate(data, ROOT, args.check_sources)
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as error:
        print(error, file=sys.stderr)
        return 1
    if problems:
        print("\n".join(problems), file=sys.stderr)
        return 1
    print(f"Validated {len(data['modules'])} module registry entries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
