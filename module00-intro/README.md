# Module 00: Welcome to UART

**Kind:** `intro` · Dual-track course welcome

← Start · [Course README](../README.md) · [UART frame →](../module01-uart-frame/README.md)

## What this course is

**learn_uart** follows the shared protocol arc: **spec → RTL sketch → TB → waves → VIP map**.

| Track | Where you practice | Best for |
|-------|--------------------|----------|
| **A — Real RTL/TB** | Local Verilog + iverilog/Verilator / HDL Simulator | Muscle memory, UART DUT/TB you keep |
| **B — Browser lab** | Interactive labs on the learning platform | Frame / FIFO / handshake intuition |

Do **not** re-teach full verification planning here — see **learn_verification_planning_management**.  
Legacy combined path: [`../learn_uart_spi_i2c/`](../learn_uart_spi_i2c/). Sibling courses: **learn_spi**, **learn_i2c**.

## Setup (Track A)

1. Editor for `.v` / `.sv` + optional iverilog / Verilator / [HDL Simulator](https://universal-verification-methodology.github.io/systemverilog-simulator/).
2. Optional: peek at UART examples under [`../learn_uart_spi_i2c/`](../learn_uart_spi_i2c/).
3. Open this repo at `courses/learn_uart`.

## Setup (Track B)

1. Serve the platform: `python -m http.server 8080 --directory platform` (from monorepo root).
2. Open http://127.0.0.1:8080/tools/index.html — shipped starters: [`fifo-lab`](http://127.0.0.1:8080/tools/fifo-lab/index.html), [`handshake`](http://127.0.0.1:8080/tools/handshake/index.html), [`waveform-lab`](http://127.0.0.1:8080/tools/waveform-lab/index.html).
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
