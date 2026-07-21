# Two learning tracks

## Track A — Real RTL/TB

Practice with paper + small Verilog UART sketches (optional iverilog / Verilator / HDL Simulator).

- Prompts under each `moduleNN-*/EXAMPLES.md`
- Optional examples in [`../LEGACY.md`](../LEGACY.md) (archive; prefer **learn_uart** / **learn_spi** / **learn_i2c**)
- Self-check: `./scripts/module.sh NN --check`

## Track B — Browser lab

- Local tools: http://127.0.0.1:8080/tools/
- Live: https://universal-verification-methodology.github.io/learning/tools/
- **Shipped today:** `uart-frame`, `spec-to-rtl`, `tb-vs-uvm-map`, `self-check-tb`, `baud-divider`, `uart-oversample`, `uart-errors`, `fifo-lab`, `handshake`, `waveform-lab`
- Remaining UART-specific labs: TB / VIP stay **Planned** until they ship

## Recommended path

1. Intro + paper UART frame
2. Shipped FIFO / handshake / waves labs
3. Track A for planned UART-specific modules
4. Return to browser labs as they ship
