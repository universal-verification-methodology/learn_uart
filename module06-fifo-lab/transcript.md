# Module 06 — FIFO in the datapath

**Module id:** module06-fifo-lab  
**Lab:** fifo-lab  
**Tracks:** A (real RTL/TB) · B (browser lab)

## Slide 1 — FIFO in the datapath

UART bytes arrive asynchronously from the line rate while software reads when it can. A FIFO sits between the RX shifter and the holding register—or between the CPU and the TX serializer—to absorb bursts. First-in first-out means the oldest byte is always popped next. Empty means nothing to read; full means no room to push. That is how you avoid the overrun from the last module without dropping every late byte. This lab is a synchronous count-based FIFO model—one clock domain, behavioral pointers.

## Slide 2 — Starter depth four

Starter preset: depth-four FIFO, empty, write and read pointers both at zero, count zero. Din is hex A5. Click Push once—count becomes one, empty clears, write pointer advances to slot one, read pointer stays at zero. Slot zero holds A5. Pop once and you get A5 back, count returns to zero, read pointer moves to one, empty is true again. Fill with four pushes to see full equal one and a fifth push blocked in the event log. Switch depth to eight and the same rules apply with a longer slot row.

## Slide 3 — Browser lab

![FIFO lab starter](assets/lab-starter.png)

In the browser lab, load the starter example and watch the flag row—empty, full, count, almost full, almost empty. Each slot shows WR and RD markers; occupied cells display hex data. Push hex eleven then hex twenty-two and pop once—you must receive eleven first. Try fill-to-full then push again—the log shows blocked FULL. Reset clears pointers and count. Challenges walk push, pop, wrap, order, and depth eight.

## Slide 4 — Real RTL/TB practice

In Track A, restate FIFO in one sentence and why UART RX often needs one. Draw four slots with wr and rd pointers after one push of A5. Write the empty and full conditions using count and depth. Optional: peek at FIFO examples in the legacy combined materials and name where full would backpressure a push. This lab is pointer literacy—async clock-domain FIFOs with Gray codes are a separate topic.

## Slide 5 — Pitfalls to watch

Do not pop when empty or push when full in real hardware without checking flags—the lab blocks those ops and logs the reason. Write and read pointers wrap modulo depth; full is count equals depth, not wr equals rd unless you use the spare-slot trick. A FIFO fixes overrun only if software or DMA keeps draining—it is not infinite buffering. Almost-full at count depth minus one is a common interrupt threshold. And remember: this model is sync; crossing UART sample clock to sysclk needs an async FIFO, not this lab alone.

## Slide 6 — Your turn

Complete the checklist for at least one track—preferably both. In the browser, load starter depth four, push A5, pop A5, then fill to full and see push blocked. On paper, sketch wr and rd after two pushes and one pop. When you are ready, take the short quiz, then continue to handshake.
