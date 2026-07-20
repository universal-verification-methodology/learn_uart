---
marp: true
title: Spec to RTL
paginate: true
---

# Spec to RTL

Before you write bit-level logic, translate the spec into structure

---

## UART TX starter
- Starter preset: UART transmit eight-N-one
- Tx busy, plus baud parameter BAUD_DIV
- Required blocks still waiting
- Check the block rows, then click Generate skeleton to grow a uart_tx module outline

---

## Browser lab
![Spec to RTL starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, from the UART TX spec list every port name and one parameter
- Name three blocks you would draw on paper before coding
- Optional: compare your list to a UART sketch in the legacy combined materials
- Write one sentence on what belongs in the skeleton versus what belongs in the FSM

---

## Pitfalls to watch
- Do not skip ports and jump straight to the FSM
- Parameters are not optional when baud or mode defines behavior
- A skeleton with TODO is not done RTL, this lab separates planning from implementation
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, finish required UART checks and generate the skeleton once
- On paper, list ports, parameters, and three blocks for UART TX
- When you are ready, take the short quiz, then continue to baud divider

