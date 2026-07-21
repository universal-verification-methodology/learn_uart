---
marp: true
title: Self-checking testbench
paginate: true
---

# Self-checking testbench

A useful testbench does not stop at dumping waves for eyeball review

---

## Starter and2 PASS
- Starter preset
- The flow row reads stimulus, DUT, got, compare, PASS
- The compare box shows y equals one matches expect one
- History lists one passing vector
- Try Run check again to refresh the TB sketch
- Set expect to zero on the same stimulus and Run check again

---

## Browser lab
![Self-check TB starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, write the five-step self-check loop in order
- Sketch dollar-error versus dollar-display for one UART-style byte check, even on paper
- Optional: peek at a UART testbench in this module’s examples and name where expect
- This lab uses tiny DUTs; the discipline is the same for full serial VIP later

---

## Pitfalls to watch
- Do not set expect by reading the DUT output you are testing
- Waves help debug but are not the pass criterion, automate the compare
- One passing vector is not coverage
- Wrong expect on purpose is good practice, you must see FAIL paths in sim logs
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser
- On paper, write the compare line for got not equal expect
- When you are ready, take the short quiz, then continue to TB clock and reset

