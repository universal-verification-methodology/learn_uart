---
marp: true
title: UART frame
paginate: true
---

# UART frame

Asynchronous serial UART sends one byte as a timed bit sequence, no shared clock wire on the link

---

## Starter 0xA5 as 8N1
- Starter: byte hex A5 as eight-N-one, eight data bits, no parity, one stop bit
- Idle high, start zero, then D0 through D7 LSB first, then stop one, then idle again
- For A5 the LSB is one
- Step bit by bit or play to end to watch the cursor move through twelve slots
- Rebuild after changing width, parity, or stop count

---

## Browser lab
![UART frame starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, sketch the same frame on paper
- Write what eight-N-one means in words
- Optional: peek at UART examples in the legacy combined materials and name one signal you
- This lab is frame literacy, not a full synthesizable UART yet

---

## Pitfalls to watch
- Do not send MSB first on the wire
- Do not confuse baud with the system clock
- Parity changes the slot count; eight-E-one is not eight-N-one
- And remember

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, step through starter A5 eight-N-one and land on start, D0, and stop
- On paper, draw one complete frame with bit values labeled
- When you are ready, take the short quiz, then continue to spec-to-RTL checklist

