# Module 13 — UART complete

**Module id:** module13-wrap  
**Lab:** none (wrap)  
**Tracks:** recap · next course

## Slide 1 — UART complete

You have walked the UART path—from frame timing and spec-to-RTL checklists, through baud dividers and oversampling, error cases, FIFO and handshake in the datapath, self-checking testbenches, clock and reset discipline, wave reading, TB versus UVM mapping, and VIP package anatomy. This short wrap names what you can do now and points you to the next courses on the ladder.

## Slide 2 — What you can do now

You can describe a UART frame—idle, start, data, optional parity, stop—and name common error cases like framing and overrun. You can map a UART spec into an RTL checklist and explain baud timing with oversampling ideas. You can place FIFO plus valid-ready handshake in a datapath story and sketch a self-checking testbench rhythm. You can read basic waves for debug and explain how classic pin TB roles map to agents, checkers, coverage, and docs. That is UART literacy—not full chip verification planning, which lives in a different course.

## Slide 3 — Close the track gaps

If you mainly used browser labs, sketch a UART frame on paper and name where parity and stop bits sit. Revisit any module you skipped on Track A with a short Verilog or paper sketch. If you mainly used Track A, open the browser labs for visual challenges on frame timing, baud math, oversampling, waves, TB versus UVM map, and VIP anatomy. Either track works for self-study; both together stick best before SPI, I²C, or UVM depth.

## Slide 4 — The tools you practiced

![Tools index](assets/tools-index.png)

Here is the tools index again—the same shelf of UART and shared concept labs you opened along the way. You do not need to re-clear every challenge. Use it as a map: if frame timing or VIP anatomy still feels fuzzy, jump back to that lab, then return here when you are ready for the next protocol or methodology course.

## Slide 5 — Next on the ladder

Continue to learn SPI or learn I²C when you want the next serial protocol with different clocking rules. learn UVM twenty seventeen deepens the agent and environment story beyond this literacy map. learn verification planning and management is where planning depth lives—course fourteen on the syllabus—not here. Unix and Git fluency from earlier courses still help when you run sims, read logs, and manage RTL repos.

## Slide 6 — Your turn

Review the wrap checklist in the module README. Confirm you completed Track A and/or Track B for the modules you care about, and that you can draw a UART frame and name framing, parity, and overrun. When you are ready, take the short quiz, then open the next course that matches your path.
