# Module 03 — Baud / divider

**Module id:** module03-baud-divider  
**Lab:** baud-divider  
**Tracks:** A (real RTL/TB) · B (browser lab)

## Slide 1 — Baud divider

Your system clock runs much faster than the UART bit rate. A baud divider turns sysclk into a slower enable. The integer formula is DIV approximately round of f_sys divided by baud. A counter runs zero through DIV minus one each sysclk. When it hits DIV minus one, you wrap to zero and fire a one-cycle baud_tick pulse. That pulse tells the TX or RX FSM to advance one bit time—not a fifty-percent duty clock on the wire.

## Slide 2 — Starter DIV equals four

Starter preset: DIV equals four in baud_tick pulse mode, sixteen sysclk cycles shown. Count zero, one, two, three—then baud_tick equals one on the wrap at cnt equals three, and the counter returns to zero. In sixteen cycles you see four ticks. Step once to watch cnt advance, or play to end for the full pattern. Compare with toggle mode: clk_div flips every DIV clocks, so one output period is about two times DIV sysclks—SPI-style, not UART enable.

## Slide 3 — Browser lab

![Baud divider starter](assets/lab-starter.png)

In the browser lab, load the starter example and read the four idea cards—DIV, baud_tick, clk_div, and oversampling OS. The wave table and SVG trace show cnt and the output pulse. Try Calc DIV for fifty megahertz and one-one-five-two-zero-zero baud—expect four-thirty-four. Switch OS to sixteen times and calc again for the sample-clock divider. Demo DIV equals four and Explain summarize pulse versus toggle in one click.

## Slide 4 — Real RTL/TB practice

In Track A, restate the divider formula in one sentence. Draw a counter from zero to DIV minus one and mark where baud_tick goes high for one cycle. Contrast that with a toggling clk_div output. Optional: peek at UART RTL examples in the legacy combined materials and name where a baud_tick would feed the bit FSM. This lab is divider literacy—not a full UART yet.

## Slide 5 — Pitfalls to watch

Do not confuse baud_tick with the serial line—it is an internal enable, one sysclk wide. Toggle mode is not UART bit timing; its period is two times DIV, not DIV. Integer division truncates—real designs pick f_sys and baud so the error stays acceptable. With oversampling, divide by baud times OS, not baud alone—that preview matters in the next module. And remember: the sketch panel shows concept Verilog; synthesis still needs reset and clock-domain hygiene.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, load starter DIV four pulse, step to a baud_tick at cnt three, and calc DIV for fifty megahertz at one-one-five-two-zero-zero. On paper, draw the counter wrap and one tick pulse. When you are ready, take the short quiz, then continue to oversampling.
