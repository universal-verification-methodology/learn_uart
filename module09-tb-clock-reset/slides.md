---
marp: true
title: TB clock and reset
paginate: true
---

# TB clock and reset

Every RTL testbench needs a clock and a reset before stimulus runs

---

## Starter classic assert times two
- Starter preset: classic assert times two, sync release
- Free-running clk toggles every half-cycle
- Rst_n stays low through two posedges
- Cursor starts at h4, the release point
- Click Analyze and the flags show assert_posedges equals two
- The TB sketch shows repeat two at posedge clk, then rst_n equals one

---

## Browser lab
![TB clock reset starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, write a minimal initial block
- State why sync deassert is preferred for flops clocked on posedge clk
- Optional: peek at a UART TB in the legacy combined materials and name where reset ends
- This lab is literacy, not a full simulator or metastability proof

---

## Pitfalls to watch
- Do not confuse TB clock generation with the UART baud divider, they serve different roles
- Assert means rst_n equals zero, not one
- Counting reset cycles means posedges while rst_n is low, not arbitrary half-cycles
- Releasing reset mid-cycle can work but is not the same as sync release at the edge
- Hold forever means the DUT never leaves reset, useful to see the wave, not a passing test
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser
- On paper, sketch clk and rst_n for two cycles in reset and one cycle out
- When you are ready, take the short quiz, then continue to waves

