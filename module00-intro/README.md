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
2. Open http://127.0.0.1:8080/tools/index.html — all **12** UART course labs are shipped (frame through VIP anatomy).
3. Live mirror: [learning/tools](https://universal-verification-methodology.github.io/learning/tools/).

## How to move through modules

1. Read the module **README** (outcomes).
2. Pick Track A, Track B, or both—every lab module has a shipped browser lab.
3. Check off **CHECKLIST.md**.
4. Optional: skim `outline.yaml` / `transcript.md` for upcoming slides & clips.

## Media

| Artifact | Path |
|----------|------|
| Transcript | [transcript.md](transcript.md) |
| Outline | [outline.yaml](outline.yaml) |
| Slides | [slides.pptx](slides.pptx) · [slides.pdf](slides.pdf) |
| Video | [video.mp4](video.mp4) |
| Quiz | [quiz.json](quiz.json) |


## Next

→ [Module 01: UART frame](../module01-uart-frame/README.md)
