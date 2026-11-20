"""Exercise the planning and eval CLI writers against existing and shared logs."""

import json
import os
import runpy
import subprocess
import sys
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[3]
PLANNING = ROOT / "_bmad/scripts/memlog.py"
EVAL = Path("skills/bmad-eval-runner/scripts/memlog.py")
WRITERS = (PLANNING, ROOT / ".agents" / EVAL, ROOT / ".claude" / EVAL)


def run(command):
    return subprocess.run([sys.executable, *command], capture_output=True, text=True, timeout=60)


def parallel(commands):
    with ThreadPoolExecutor(max_workers=12) as pool:
        return list(pool.map(run, commands))


def test_one_initializer_wins(tmp_path):
    path = tmp_path / "new" / ".memlog.md"
    commands = [
        [WRITERS[i % len(WRITERS)], "init", "--path", path, "--field", f"owner=writer-{i}"]
        for i in range(24)
    ]
    results = parallel(commands)
    assert Counter(result.returncode for result in results) == {0: 1, 2: 23}
    winner = next(i for i, result in enumerate(results) if result.returncode == 0)
    assert f"owner: writer-{winner}" in path.read_text(encoding="utf-8").splitlines()


def test_concurrent_appends_and_metadata_updates_preserve_legacy_log(tmp_path):
    path = tmp_path / ".memlog.md"
    path.write_text("---\nowner: original\n---\n\n- existing entry\n", encoding="utf-8")
    commands = []
    for i in range(32):
        writer = WRITERS[i % len(WRITERS)]
        target = ["--workspace", tmp_path] if writer == PLANNING else ["--path", path]
        commands.append([writer, "append", *target, "--type", "note", "--text", f"item-{i}"])
        if i % 4 == 0:
            commands.append([PLANNING, "set", "--path", path, "--key", f"field-{i}", "--value", "saved"])
        if i == 7:
            commands.append([WRITERS[1], "set-complete", "--path", path])

    counts = []
    for command, result in zip(commands, parallel(commands)):
        assert result.returncode == 0, result.stderr
        receipt = json.loads(result.stdout)
        assert receipt["ok"]
        if command[1] == "append":
            counts.append(receipt.get("entries", receipt.get("n")))

    assert sorted(counts) == list(range(2, 34))
    lines = path.read_text(encoding="utf-8").splitlines()
    assert "owner: original" in lines
    assert "status: complete" in lines
    assert all(f"field-{i}: saved" in lines for i in range(0, 32, 4))
    expected = ["- existing entry", *(f"- (note) item-{i}" for i in range(32))]
    assert Counter(line for line in lines if line.startswith("- ")) == Counter(expected)


def test_explicit_alias_updates_the_same_log_and_preserves_existing_temp_file(tmp_path):
    path = tmp_path / ".memlog.md"
    path.write_text("---\nowner: original\n---\n\n- existing entry\n", encoding="utf-8")
    alias = tmp_path / "linked-log.md"
    try:
        alias.symlink_to(path)
    except OSError as error:
        pytest.skip(f"symlink creation is unavailable: {error}")
    stale = tmp_path / ".memlog.md.tmp"
    stale.write_text("unrelated file", encoding="utf-8")

    for script, target in zip(WRITERS, (alias, path, alias)):
        result = run([script, "append", "--path", target, "--type", "event", "--text", script.parent.name])
        assert result.returncode == 0, result.stderr
        assert json.loads(result.stdout)["memlog"] == str(target)
    assert alias.is_symlink()
    assert sum(line.startswith("- ") for line in path.read_text(encoding="utf-8").splitlines()) == 4
    assert stale.read_text(encoding="utf-8") == "unrelated file"


@pytest.mark.parametrize("script", WRITERS)
def test_failed_replace_leaves_old_log_and_releases_lock(script, tmp_path, monkeypatch):
    path = tmp_path / ".memlog.md"
    original = "---\nowner: original\n---\n\n- first\n"
    path.write_text(original, encoding="utf-8")
    memlog = runpy.run_path(str(script))

    def unavailable(source, destination):
        raise OSError("simulated replace failure")

    args = ["append", "--path", str(path), "--type", "note", "--text", "second"]
    with monkeypatch.context() as patch:
        patch.setattr(os, "replace", unavailable)
        with pytest.raises(OSError, match="simulated replace failure"):
            memlog["main"](args)

    assert path.read_text(encoding="utf-8") == original
    assert list(tmp_path.glob(".memlog.md.*.tmp")) == []
    result = run([script, *args])
    assert result.returncode == 0, result.stderr
    assert path.read_text(encoding="utf-8").splitlines()[-1] == "- (note) second"
