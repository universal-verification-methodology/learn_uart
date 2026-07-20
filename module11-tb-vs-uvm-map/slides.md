---
marp: true
title: From pin wiggle to agents
paginate: true
---

# From pin wiggle to agents

You already built a self-checking UART testbench with clock, reset, and inline expects

---

## Six pairs on the map
- The lab lines up six classic pieces with six UVM roles
- Pin wiggle maps to driver plus virtual interface
- Hard-coded vector lists map to sequences and a sequencer
- A display peek maps to a monitor and analysis ports, observation splits from stimulus
- Inline expect maps to a scoreboard, checks happen on transactions, not only wires
- A flat module testbench maps to an environment and agents

---

## Browser lab
![Browser lab starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, restate the core idea in one sentence
- On paper, map these five classic pieces to UVM
- Scoreboard in a UART byte send
- You do not need a simulator for this beat, the mapping is the skill
- When you later read a real uart_agent

---

## Pitfalls to watch
- Do not treat this lab as a substitute for running self-checking RTL
- Do not assume UVM removes pin knowledge
- A scoreboard is not only display, it compares predicted versus observed transactions
- Sequences are not magic, they replace the vector lists you would have pasted into tasks
- And remember: literacy first
- Factory, objections, and RAL come later

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load starter, click through all six pairs, mark each mapped
- On paper, draw test to env to agent to DUT for UART TX
- When you are ready, take the short quiz, then continue to VIP anatomy

