---
marp: true
title: Oversampling
paginate: true
---

# Oversampling

UART RX cannot rely on one sample per bit, the line transitions are noisy and slow

---

## Starter sixteen times
- Starter preset: sixteen times oversampling of a clean zero bit cell, ideal skew zero
- Sixteen sample ticks numbered zero through fifteen
- Mid sample is tick eight, half of sixteen, away from both edges
- Step tick to watch the cursor move, or jump to mid in one click
- The verdict should show mid sample equals zero and decide equals zero
- Try eight times oversample and mid moves to tick four

---

## Browser lab
![UART oversample starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, restate oversampling in one sentence, how many sample clocks fit in one bit at
- Draw tick zero through fifteen for a zero bit and circle the mid sample
- Write what Start-bit hunt does after idle goes to zero
- Optional: peek at UART RX examples in the legacy combined materials and name where a
- This lab is sampling literacy, not a full synchronizer or metastability treatment yet

---

## Pitfalls to watch
- Do not sample on the first tick after an edge, that is where skew and rise time hurt most
- Mid equals OS divided by two; at eight times that is tick four, not eight
- Majority vote helps a noisy mid but does not fix a completely wrong baud divider
- Start-bit hunt centers on the start bit
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load starter sixteen times, jump to mid at tick eight
- On paper, draw sixteen ticks and mark the mid sample for a zero bit
- When you are ready, take the short quiz, then continue to UART errors

