#!/usr/bin/env python3
"""Pass 2: re-capture lab/tools snapshots for learn_uart."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPT = ROOT / ".cursor/skills/module-slides/scripts/capture_lab_snapshot.py"
BASE = "http://127.0.0.1:8080/tools"

# (module_dir, lab_id, optional --name)
CAPTURES = [
    ("module00-intro", "index", "tools-index.png"),
    ("module01-uart-frame", "uart-frame", None),
    ("module02-spec-to-rtl", "spec-to-rtl", None),
    ("module03-baud-divider", "baud-divider", None),
    ("module04-uart-oversample", "uart-oversample", None),
    ("module05-uart-errors", "uart-errors", None),
    ("module06-fifo-lab", "fifo-lab", None),
    ("module07-handshake", "handshake", None),
    ("module08-self-check-tb", "self-check-tb", None),
    ("module09-tb-clock-reset", "tb-clock-reset", None),
    ("module10-waveform-lab", "waveform-lab", None),
    ("module11-tb-vs-uvm-map", "tb-vs-uvm-map", None),
    ("module12-vip-anatomy", "vip-anatomy", None),
    ("module13-wrap", "index", "tools-index.png"),
]


def main() -> int:
    failed = []
    for slug, lab, name in CAPTURES:
        mod = ROOT / "courses/learn_uart" / slug
        cmd = [
            sys.executable,
            str(SCRIPT),
            str(mod.relative_to(ROOT)).replace("\\", "/"),
            "--lab",
            lab,
            "--base",
            BASE,
        ]
        if name:
            cmd.extend(["--name", name])
        print(f"\n=== {slug} ({lab}) ===")
        r = subprocess.run(cmd, cwd=ROOT)
        if r.returncode != 0:
            failed.append(slug)
    if failed:
        print("FAILED:", ", ".join(failed), file=sys.stderr)
        return 1
    print("\nAll snapshots captured.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
