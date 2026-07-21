---
marp: true
title: Valid and ready
paginate: true
---

# Valid and ready

On-chip streaming interfaces move one beat per cycle when source and sink agree

---

## Starter both assert
- Starter preset: Both assert, valid and ready both high on cycle zero, data hex A5
- Fire is one at cycle zero and exactly one beat transfers in the eight-cycle window
- Step through cycles and watch the verdict panel
- The fire row in the wave table marks every cycle where valid and ready overlap
- Toggle valid or ready cells to see fire disappear
- This is the same beat handshake you would use between a UART byte source and a FIFO sink

---

## Browser lab
![Handshake starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, write the fire equation and explain valid and ready in one sentence each
- Sketch three cycles where valid is held high but ready is zero
- Optional: peek at streaming or AXI-Stream examples in this module’s examples and name the
- This lab is interface literacy, not a full protocol VIP or UART line driver

---

## Pitfalls to watch
- Do not treat valid alone as a transfer, both must be one
- Do not assume the source drops valid every cycle; it may hold through a sink stall
- Real designs separate those paths
- Back-to-back bursts need ready high on consecutive cycles, not just one pulse
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser
- On paper, draw valid and ready for two cycles that fire and one that does not
- When you are ready, take the short quiz, then continue to self-check TB

