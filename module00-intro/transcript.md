# Module 00 — Welcome to UART

**Module id:** module00-intro  
**Lab:** none (intro)  
**Tracks:** A (real RTL/TB) · B (browser lab)

## Slide 1 — Welcome to UART

UART shows up everywhere in bring-up and debug—a serial line on a board, a console on a chip, a quick link between blocks. This short clip welcomes you to learn UART and shows how the course is meant to be used.

## Slide 2 — What you’ll build toward

Across the course you follow one protocol arc: read the spec, sketch RTL, build a self-checking testbench, read waves, then map the same ideas to a VIP-style view. You’ll walk frame timing, baud and oversampling, error cases, FIFO and handshake in the datapath, and finally TB versus UVM layering. Deep verification planning is a different course—here you build UART literacy first.

## Slide 3 — Two tracks, one idea

Every lab module offers two ways to practice. Track A is real RTL and testbench work—small Verilog sketches with optional Icarus, Verilator, or the browser HDL simulator. Track B uses interactive labs on the learning platform for frame timing, baud math, and wave intuition. You may do either track, or both. A good rhythm is browser first for the idea, then a short RTL sketch to harden it.

## Slide 4 — Set up Track A

Open an editor for Verilog or SystemVerilog files. Optional: install Icarus or Verilator, or use the public HDL simulator for quick runs. Stretch examples live in the older combined UART-SPI-I²C materials—they are optional, not required. From this course folder, open module READMEs and EXAMPLES prompts as you go; self-check scripts can grade checklist items when you want them.

## Slide 5 — Set up Track B

![Tools index](assets/tools-index.png)

From the monorepo, serve the platform folder with a simple local web server, then open the tools index in your browser. All twelve course labs are shipped—UART frame through VIP anatomy—alongside shared labs like FIFO, handshake, and waveform viewer. If you prefer, use the published tools site instead. Either way, confirm you can reach the index—the next module sends you into the UART frame lab.

## Slide 6 — How to move through modules

For each module, read the README for the outcome, pick a track—or both—then work the checklist. When you finish this intro checklist, continue to UART frame, where idle, start, data, and stop bits become a timeline you can read and sketch.
