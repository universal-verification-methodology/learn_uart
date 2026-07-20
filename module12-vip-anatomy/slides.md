---
marp: true
title: What a VIP package is
paginate: true
---

# What a VIP package is

Module eleven mapped classic testbench habits onto UVM roles

---

## Starter and incomplete presets
- Starter loads a complete UART VIP
- Scenario presets show what breaks handoff
- Missing checker keeps agent, coverage, and docs but drops protocol rules, INCOMPLETE
- Missing coverage drops bins while stimulus and checks remain, INCOMPLETE
- Missing docs drops the self-test handoff even when code pieces exist, INCOMPLETE
- Agent only is useful scaffolding, not a VIP yet

---

## Browser lab
![Browser lab starter](assets/lab-starter.png)

---

## Real RTL/TB practice
- In Track A, restate the four VIP deliverables in one sentence each
- Docs should stay blank
- Optional: peek at the linked UART RTL or TB sketch and label which folders would hold
- Remember: scoreboard payload compare often lives in the environment
- Your job is to read a block diagram and know what a consumer still has to wire in the env

---

## Pitfalls to watch
- Do not call an agent folder a finished VIP, handoff needs checker, coverage, and docs too
- Do not confuse checker with scoreboard, the checker flags protocol legality
- Coverage is not optional decoration, it proves which bins your VIP scenarios actually hit
- Docs are not README fluff, they include a self-test so integration does not stall
- And remember: this lab teaches package anatomy
- Factory overrides, RAL, and full UVM env wiring come in later courses, not here

---

## Your turn
- Complete the checklist for at least one track, preferably both
- In the browser, load starter, then Demo incomplete and name the missing piece
- On paper, draw uart_vip with four subfolders and mark which are empty for agent-only
- When you are ready

