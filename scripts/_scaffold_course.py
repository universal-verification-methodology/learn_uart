#!/usr/bin/env python3
"""Scaffold courses/learn_uart from syllabus (lab-driven + dual tracks)."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]  # courses/learn_uart
COURSES = ROOT.parent
DST = ROOT

LAB_BASE_LOCAL = "http://127.0.0.1:8080/tools"
LAB_BASE_LIVE = "https://universal-verification-methodology.github.io/learning/tools"
LEGACY = "../learn_uart_spi_i2c"

# Status from disk audit (2026-07).
MODULES = [
    (0, "intro", "intro", "Welcome to UART", None, None),
    (1, "uart-frame", "lab", "UART frame", "uart-frame", "S"),
    (2, "spec-to-rtl", "lab", "Spec → RTL checklist", "spec-to-rtl", "S"),
    (3, "baud-divider", "lab", "Baud / divider", "baud-divider", "S"),
    (4, "uart-oversample", "lab", "Oversampling", "uart-oversample", "S"),
    (5, "uart-errors", "lab", "UART errors", "uart-errors", "S"),
    (6, "fifo-lab", "lab", "FIFO in the datapath", "fifo-lab", "S"),
    (7, "handshake", "lab", "Handshake", "handshake", "S"),
    (8, "self-check-tb", "lab", "Self-check TB", "self-check-tb", "S"),
    (9, "tb-clock-reset", "lab", "TB clock / reset", "tb-clock-reset", "P"),
    (10, "waveform-lab", "lab", "Waves", "waveform-lab", "S"),
    (11, "tb-vs-uvm-map", "lab", "TB vs UVM map", "tb-vs-uvm-map", "S"),
    (12, "vip-anatomy", "lab", "VIP anatomy", "vip-anatomy", "P"),
    (13, "wrap", "wrap", "UART complete", None, None),
]


def mod_dir(num: int, slug: str) -> Path:
    return DST / f"module{num:02d}-{slug}"


def lab_urls(lab_id: str) -> tuple[str, str]:
    return (f"{LAB_BASE_LOCAL}/{lab_id}/index.html", f"{LAB_BASE_LIVE}/{lab_id}/")


def write_module_readme(
    num: int, slug: str, kind: str, title: str, lab_id: str | None, status: str | None
) -> None:
    d = mod_dir(num, slug)
    d.mkdir(parents=True, exist_ok=True)
    nn = f"{num:02d}"
    prev = next((m for m in MODULES if m[0] == num - 1), None)
    nxt = next((m for m in MODULES if m[0] == num + 1), None)

    nav = []
    if prev:
        nav.append(f"[← {prev[3]}](../module{prev[0]:02d}-{prev[1]}/README.md)")
    else:
        nav.append("← Start")
    nav.append("[Course README](../README.md)")
    if nxt:
        nav.append(f"[{nxt[3]} →](../module{nxt[0]:02d}-{nxt[1]}/README.md)")
    else:
        nav.append("End →")
    nav_line = " · ".join(nav)

    if kind == "intro":
        body = f"""# Module {nn}: {title}

**Kind:** `intro` · Dual-track course welcome

{nav_line}

## What this course is

**learn_uart** follows the shared protocol arc: **spec → RTL sketch → TB → waves → VIP map**.

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Real RTL/TB** | Local Verilog + iverilog/Verilator / HDL Simulator | Muscle memory, UART DUT/TB you keep |
| **B — Browser lab** | Interactive labs on the learning platform | Frame / FIFO / handshake intuition |

Do **not** re-teach full verification planning here — see **learn_verification_planning_management**.  
Legacy combined path: [`{LEGACY}/`]({LEGACY}/). Sibling courses: **learn_spi**, **learn_i2c**.

## Setup (Track A)

1. Editor for `.v` / `.sv` + optional iverilog / Verilator / [HDL Simulator](https://universal-verification-methodology.github.io/systemverilog-simulator/).
2. Optional: peek at UART examples under [`{LEGACY}/`]({LEGACY}/).
3. Open this repo at `courses/learn_uart`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html — shipped starters: [`fifo-lab`]({LAB_BASE_LOCAL}/fifo-lab/index.html), [`handshake`]({LAB_BASE_LOCAL}/handshake/index.html), [`waveform-lab`]({LAB_BASE_LOCAL}/waveform-lab/index.html).
3. UART-specific labs may still show Coming soon — use Track A sketches until they ship.

## How to move through modules

1. Read the module **README** (outcomes).
2. Prefer Track A when a browser lab is still planned.
3. Check off **CHECKLIST.md**.
4. Optional: skim `outline.yaml` / `transcript.md` for upcoming slides & clips.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | generate later with **module-slides** |

## Next

→ [Module 01: UART frame](../module01-uart-frame/README.md)
"""
    elif kind == "wrap":
        body = f"""# Module {nn}: {title}

**Kind:** `wrap`

{nav_line}

## You can now

- Describe a UART frame (start / data / parity / stop) and common error cases
- Map a UART spec into an RTL checklist and baud / oversample timing ideas
- Place FIFO + valid/ready handshake in a UART datapath story
- Point at TB / waves / VIP map next steps (even if some browser labs are still shipping)

## Dual-track recap

If you mainly used **shipped browser labs** (FIFO / handshake / waves), sketch a UART frame on paper and revisit planned modules when they ship.  
If you mainly used **Track A**, open the shipped labs for visual challenges.

## Next courses

→ **learn_spi** · **learn_i2c** · **learn_uvm2017** · **learn_verification_planning_management**  
Syllabus ladder: [../../syllabus.md](../../syllabus.md#suggested-learning-ladder)

## Checklist

- [ ] I completed Track A and/or Track B for the modules I care about
- [ ] I can draw a UART frame and name framing / parity / overrun
- [ ] I know planning depth lives in course 14, not here
"""
    else:
        assert lab_id and status
        local, live = lab_urls(lab_id)
        status_note = (
            "Shipped"
            if status == "S"
            else "Planned (Coming soon on tools index — use Track A until it ships)"
        )
        body = f"""# Module {nn}: {title}

**Kind:** `lab` · Primary lab: `{lab_id}` · **{status_note}**

{nav_line}

## Outcomes

After this module you can explain and practice the ideas taught by **`{lab_id}`**, in the browser and/or with a UART RTL/TB sketch.

## Two tracks (pick one or both)

### Track A — Real RTL/TB (hands-on)

1. Open [EXAMPLES.md](EXAMPLES.md) and work the prompts (paper + optional `.v`).
2. Complete [CHECKLIST.md](CHECKLIST.md); use [`{LEGACY}/`]({LEGACY}/) when helpful.
3. Optional self-check: `./scripts/module.sh {nn} --check` (from course root).

### Track B — Browser lab (online)

1. Local: [{local}]({local})
2. Live: [{live}]({live})
3. Load the **starter example**, then work challenges (or note Coming soon).
4. Check off the Track B items in [CHECKLIST.md](CHECKLIST.md).

> Concept labs are literacy tools — they do not replace a synthesizable UART + self-checking TB.

## Media (planned)

| Artifact | Path |
|----------|------|
| Outline | [outline.yaml](outline.yaml) |
| Transcript stub | [transcript.md](transcript.md) |
| Slides / video | generate later with **module-slides** |

## Files

```
module{nn}-{slug}/
├── README.md
├── CHECKLIST.md
├── EXAMPLES.md
├── outline.yaml
├── transcript.md
└── (optional) examples/
```
"""
    (d / "README.md").write_text(body, encoding="utf-8")


def write_checklist(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "intro":
        text = f"""# Module {nn} checklist — {title}

## Setup

- [ ] Editor ready for `.v` / notes
- [ ] Opened this repo at `courses/learn_uart`
- [ ] Opened the [tools index]({LAB_BASE_LOCAL}/index.html) once
- [ ] Opened at least one shipped lab (`fifo-lab` / `handshake` / `waveform-lab`)

## Mindset

- [ ] I understand the spec → RTL → TB → waves → VIP arc
- [ ] I know deep planning is a different course
"""
    elif kind == "wrap":
        text = f"""# Module {nn} checklist — {title}

- [ ] Reviewed outcomes in [README.md](README.md)
- [ ] Ready for SPI / I²C / UVM as needed
"""
    else:
        text = f"""# Module {nn} checklist — {title}

## Track A — Real RTL/TB

- [ ] Worked through at least one prompt in [EXAMPLES.md](EXAMPLES.md)
- [ ] Can explain the outcome in my own words

## Track B — Browser lab (`{lab_id}`)

- [ ] Opened the lab (local or live) **or** noted Coming soon
- [ ] If shipped: loaded starter + completed a few challenges

## Done when

- [ ] I can do the task offline **or** I finished the browser challenges (preferably both when shipped)
"""
    (d / "CHECKLIST.md").write_text(text, encoding="utf-8")


def write_examples_md(num: int, slug: str, kind: str, title: str) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    if kind == "lab":
        text = f"""# Module {nn} examples — {title}

Track A (UART RTL / TB literacy). Browser lab may still be planned.

## Prompts

1. Restate the core idea of **{title}** in one sentence.
2. Draw or tabulate one worked example (frame bits, baud math, FIFO pointers, …).
3. Optional: peek at [`{LEGACY}/`]({LEGACY}/) for a UART RTL/TB sketch.

## Stretch

When the browser lab ships, redo the same idea with the starter challenges.
"""
    else:
        text = f"""# Module {nn} — no example trees

This is an `{kind}` module. See [README.md](README.md).
"""
    (d / "EXAMPLES.md").write_text(text, encoding="utf-8")


def write_outline_transcript(num: int, slug: str, kind: str, title: str, lab_id: str | None) -> None:
    d = mod_dir(num, slug)
    nn = f"{num:02d}"
    (d / "outline.yaml").write_text(
        f"""# Module {nn} outline
title: "{title}"
kind: {kind}
lab: {lab_id or "null"}
slides:
  - Course context / why UART matters in chip bring-up
  - Core idea (1 concept)
  - Track B: show lab starter if shipped (else diagram)
  - Track A: paper / tiny .v cue
  - Common pitfalls
  - Your turn + quiz prompt
duration_minutes: 8
""",
        encoding="utf-8",
    )
    if lab_id:
        show_b = f"Open the browser lab, `{lab_id}` (or note Coming soon and show a diagram)."
        show_a = "Sketch on paper or show a tiny Verilog fragment from EXAMPLES.md."
    else:
        show_b = "Point at the course map / tools index."
        show_a = "Show the spec → RTL → TB → waves → VIP arc."
    (d / "transcript.md").write_text(
        f"""# Module {nn} transcript — {title}

> Stub for voiceover / clip. Expand when recording (module-slides).

## Hook

UART shows up everywhere in bring-up and debug. This module: **{title}**.

## Teach

(3–5 sentences on the concept.)

## Show Track B

{show_b}

## Show Track A

{show_a}

## Your turn

Complete the checklist for at least one track. Then take the short quiz.
""",
        encoding="utf-8",
    )


def write_docs_index() -> None:
    docs = DST / "docs"
    docs.mkdir(exist_ok=True)
    rows = []
    for num, slug, kind, title, lab_id, status in MODULES:
        lab = f"`{lab_id}`" if lab_id else "—"
        st = status or "—"
        rows.append(
            f"| {num:02d} | `{kind}` | [{title}](../module{num:02d}-{slug}/README.md) | {lab} | {st} |"
        )
    (docs / "MODULES.md").write_text(
        f"""# learn_uart — module index

Lab-driven syllabus (pass 3). Full product syllabus: [../../syllabus.md](../../syllabus.md#11-learn_uart).

| # | Kind | Module | Lab | Status |
|---|------|--------|-----|--------|
{chr(10).join(rows)}

## Dual tracks

See [TWO_TRACKS.md](TWO_TRACKS.md). Legacy: [`{LEGACY}/`]({LEGACY}/).
""",
        encoding="utf-8",
    )
    (docs / "TWO_TRACKS.md").write_text(
        f"""# Two learning tracks

## Track A — Real RTL/TB

Practice with paper + small Verilog UART sketches (optional iverilog / Verilator / HDL Simulator).

- Prompts under each `moduleNN-*/EXAMPLES.md`
- Optional examples in [`{LEGACY}/`]({LEGACY}/)
- Self-check: `./scripts/module.sh NN --check`

## Track B — Browser lab

- Local tools: {LAB_BASE_LOCAL}/
- Live: {LAB_BASE_LIVE}/
- **Shipped today:** `uart-frame`, `spec-to-rtl`, `tb-vs-uvm-map`, `baud-divider`, `uart-oversample`, `uart-errors`, `fifo-lab`, `handshake`, `waveform-lab`, `self-check-tb`
- Remaining UART-specific labs: TB / VIP stay **Planned** until they ship

## Recommended path

1. Intro + paper UART frame
2. Shipped FIFO / handshake / waves labs
3. Track A for planned UART-specific modules
4. Return to browser labs as they ship
""",
        encoding="utf-8",
    )


def write_course_readme() -> None:
    landing = [
        f"| {num:02d} — {title} | [module{num:02d}-{slug}](module{num:02d}-{slug}/README.md) |"
        for num, slug, _k, title, *_ in MODULES
    ]
    shipped = sum(1 for m in MODULES if m[5] == "S")
    planned = sum(1 for m in MODULES if m[5] == "P")
    (DST / "README.md").write_text(
        "\n".join(
            [
                "# learn_uart",
                "",
                "[![GitHub](https://img.shields.io/badge/GitHub-learn__uart-181717?logo=github)](https://github.com/universal-verification-methodology/learn_uart)",
                "[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)",
                "[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)",
                "[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)",
                "[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)",
                "[![Domain](https://img.shields.io/badge/domain-UART%20%7C%20protocol%20%7C%20RTL-purple)](https://github.com/universal-verification-methodology/learn_uart)",
                "",
                "**learn_uart** is the open learning path for *UART: spec → RTL → TB → waves → VIP map*.",
                "",
                "Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.",
                "",
                "",
                "## Table of contents",
                "",
                "- [Contents](#contents)",
                "- [Browse or clone](#browse-or-clone)",
                "- [Consume from the parent](#consume-from-the-parent)",
                "- [Author: publish or update](#author-publish-or-update)",
                "- [Two learning tracks](#two-learning-tracks)",
                "- [Module landings](#module-landings)",
                "- [Browser labs](#browser-labs)",
                "- [License](#license)",
                "",
                "## Contents",
                "",
                "```text",
                "learn_uart/",
                "├── README.md",
                "├── LICENSE",
                "├── docs/",
                "│   ├── MODULES.md       # full module index (00–13)",
                "│   └── TWO_TRACKS.md",
                "├── scripts/",
                "│   └── module.sh",
                "├── module00-intro/",
                "├── module06-fifo-lab/     # shipped shared lab",
                "├── …",
                "└── module13-wrap/",
                "```",
                "",
                "Videos and decks are optional per module. Generate with the **module-slides** skill in the parent monorepo when ready.",
                "",
                "## Browse or clone",
                "",
                "- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)",
                "- **Legacy:** [`learn_uart_spi_i2c`](https://github.com/universal-verification-methodology/learn_uart_spi_i2c)",
                "- **Syllabus (parent):** [`syllabus.md` § learn_uart](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#11-learn_uart)",
                "",
                "```bash",
                "git clone https://github.com/universal-verification-methodology/learn_uart.git",
                "cd learn_uart",
                "chmod +x scripts/*.sh",
                "./scripts/module.sh 06 --check",
                "```",
                "",
                "Then open [module00-intro/README.md](module00-intro/README.md).",
                "",
                "## Consume from the parent",
                "",
                "```bash",
                "git clone --recurse-submodules \\",
                "  git@github.com:universal-verification-methodology/learning.git",
                "ls courses/learn_uart",
                "```",
                "",
                "## Author: publish or update",
                "",
                "```bash",
                "cd courses/learn_uart",
                "# … edit module README / CHECKLIST / EXAMPLES / transcript …",
                "cd ../..",
                "python .cursor/skills/module-slides/scripts/transcript_to_outline.py \\",
                "  courses/learn_uart/moduleNN-slug",
                "bash .cursor/skills/module-slides/scripts/narrate_clips.sh \\",
                "  courses/learn_uart/moduleNN-slug",
                "```",
                "",
                "## Two learning tracks",
                "",
                "Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).",
                "",
                "| Track | Practice surface | Start here |",
                "|-------|------------------|------------|",
                f"| **A — Real RTL/TB** | Paper + `.v` · [`{LEGACY}`]({LEGACY}/) | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |",
                f"| **B — Browser lab** | Platform tools | [fifo-lab]({LAB_BASE_LIVE}/fifo-lab/) · [handshake]({LAB_BASE_LIVE}/handshake/) · [waveform-lab]({LAB_BASE_LIVE}/waveform-lab/) |",
                "",
                f"Lab status snapshot: **{shipped} shipped** · **{planned} planned** (see [docs/MODULES.md](docs/MODULES.md)).",
                "",
                "## Module landings",
                "",
                "Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–05 UART timing/errors · 06–07 datapath · 08–10 TB/waves · 11–12 VIP map · 13 wrap.",
                "",
                "| Module | Landing |",
                "|--------|---------|",
                *landing,
                "",
                "## Browser labs",
                "",
                f"**Shipped:** [uart-frame](https://universal-verification-methodology.github.io/learning/tools/uart-frame/) · [spec-to-rtl](https://universal-verification-methodology.github.io/learning/tools/spec-to-rtl/) · [baud-divider](https://universal-verification-methodology.github.io/learning/tools/baud-divider/) · [uart-oversample](https://universal-verification-methodology.github.io/learning/tools/uart-oversample/) · [uart-errors](https://universal-verification-methodology.github.io/learning/tools/uart-errors/) · [fifo-lab](https://universal-verification-methodology.github.io/learning/tools/fifo-lab/) · [handshake](https://universal-verification-methodology.github.io/learning/tools/handshake/) · [waveform-lab](https://universal-verification-methodology.github.io/learning/tools/waveform-lab/) · [tb-vs-uvm-map](https://universal-verification-methodology.github.io/learning/tools/tb-vs-uvm-map/) · [self-check-tb](https://universal-verification-methodology.github.io/learning/tools/self-check-tb/). **Planned:** `tb-clock-reset`, `vip-anatomy`. Use Track A + [{LEGACY}]({LEGACY}/) until remaining UART-specific labs ship.",
                "",
                "## License",
                "",
                "[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).",
                "",
                "Path split from [`learn_uart_spi_i2c`](https://github.com/universal-verification-methodology/learn_uart_spi_i2c). Platform tools and the parent monorepo may carry additional notices.",
                "",
            ]
        ),
        encoding="utf-8",
    )


def write_scripts() -> None:
    scripts = DST / "scripts"
    scripts.mkdir(exist_ok=True)
    (scripts / "module.sh").write_text(
        r"""#!/usr/bin/env bash
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
NN="${1:-}"
shift || true
if [[ -z "$NN" || "$NN" == "--help" ]]; then
  echo "Usage: $0 NN [--check|--demo|--help]"
  exit 0
fi
NN="$(printf '%02d' "$((10#$NN))")"
MOD_DIR="$(find "$ROOT" -maxdepth 1 -type d -name "module${NN}-*" | head -1)"
if [[ -z "$MOD_DIR" ]]; then
  echo "No module directory for $NN"
  exit 1
fi
ACTION="${1:---check}"
case "$ACTION" in
  --check)
    echo "Module $NN self-check (Track A environment)"
    echo "Module dir: $MOD_DIR"
    command -v bash >/dev/null && echo "[OK] bash"
    if command -v iverilog >/dev/null 2>&1; then
      echo "[OK] iverilog"
    else
      echo "[INFO] iverilog not on PATH (optional)"
    fi
    LEGACY="$(cd "$ROOT/.." && pwd)/learn_uart_spi_i2c"
    if [[ -d "$LEGACY" ]]; then
      echo "[OK] legacy course present: $LEGACY"
    else
      echo "[INFO] legacy learn_uart_spi_i2c not checked out"
    fi
    [[ -f "$MOD_DIR/EXAMPLES.md" ]] && echo "[OK] EXAMPLES.md"
    [[ -f "$MOD_DIR/CHECKLIST.md" ]] && echo "[OK] CHECKLIST.md"
    ;;
  --demo)
    echo "Demo: open $MOD_DIR/EXAMPLES.md and README.md"
    ;;
  *)
    echo "Unknown option: $ACTION"
    exit 1
    ;;
esac
""",
        encoding="utf-8",
    )
    (scripts / "README.md").write_text(
        """# Scripts

| Script | Purpose |
|--------|---------|
| `module.sh NN` | `--check` / `--demo` for module number `NN` |
| `_scaffold_course.py` | Regenerate course stubs from syllabus (authors) |

```bash
chmod +x scripts/*.sh
./scripts/module.sh 06 --check
```
""",
        encoding="utf-8",
    )


def write_license() -> None:
    src = COURSES / "learn_unix" / "LICENSE"
    dst = DST / "LICENSE"
    if src.exists():
        dst.write_text(
            src.read_text(encoding="utf-8").replace("learn_unix", "learn_uart"),
            encoding="utf-8",
        )
    else:
        dst.write_text(
            "Creative Commons Attribution 4.0 International (CC BY 4.0)\n\n"
            "Copyright (c) The learn_uart contributors.\n\n"
            "https://creativecommons.org/licenses/by/4.0/\n",
            encoding="utf-8",
        )


def main() -> None:
    DST.mkdir(parents=True, exist_ok=True)
    write_license()
    write_course_readme()
    write_docs_index()
    write_scripts()
    for num, slug, kind, title, lab_id, status in MODULES:
        print(f"module{num:02d}-{slug} …")
        write_module_readme(num, slug, kind, title, lab_id, status)
        write_checklist(num, slug, kind, title, lab_id)
        write_examples_md(num, slug, kind, title)
        write_outline_transcript(num, slug, kind, title, lab_id)
    print("Done:", DST)


if __name__ == "__main__":
    main()
