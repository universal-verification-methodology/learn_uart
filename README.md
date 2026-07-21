# learn_uart

[![GitHub](https://img.shields.io/badge/GitHub-learn__uart-181717?logo=github)](https://github.com/universal-verification-methodology/learn_uart)
[![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-green?logo=creativecommons&logoColor=white)](LICENSE)
[![Role](https://img.shields.io/badge/role-Git%20submodule-orange)](https://github.com/universal-verification-methodology/learning)
[![Parent](https://img.shields.io/badge/parent-learning%20monorepo-0A9EDC)](https://github.com/universal-verification-methodology/learning)
[![Labs](https://img.shields.io/badge/labs-GitHub%20Pages-222?logo=githubpages)](https://universal-verification-methodology.github.io/learning/tools/)
[![Domain](https://img.shields.io/badge/domain-UART%20%7C%20protocol%20%7C%20RTL-purple)](https://github.com/universal-verification-methodology/learn_uart)

**learn_uart** is the open learning path for *UART: spec → RTL → TB → waves → VIP map*.

Readers and students usually **open a module README** (or the live tools) or clone this public repo. Authors edit content here (or via the parent monorepo checkout), rebuild slides/audio with **module-slides** in the parent, and push; the parent repo only stores a pinned submodule commit.


## Table of contents

- [Contents](#contents)
- [Browse or clone](#browse-or-clone)
- [Consume from the parent](#consume-from-the-parent)
- [Author: publish or update](#author-publish-or-update)
- [Two learning tracks](#two-learning-tracks)
- [Module landings](#module-landings)
- [Browser labs](#browser-labs)
- [License](#license)

## Contents

```text
learn_uart/
├── README.md
├── LICENSE
├── docs/
│   ├── MODULES.md       # full module index (00–13)
│   └── TWO_TRACKS.md
├── scripts/
│   └── module.sh
├── module00-intro/
├── module06-fifo-lab/     # shipped shared lab
├── …
└── module13-wrap/
```

Videos and decks are optional per module. Generate with the **module-slides** skill in the parent monorepo when ready.

## Browse or clone

- **Browser labs:** [https://universal-verification-methodology.github.io/learning/tools/](https://universal-verification-methodology.github.io/learning/tools/)
- **Syllabus (parent):** [`syllabus.md` § learn_uart](https://github.com/universal-verification-methodology/learning/blob/main/syllabus.md#11-learn_uart)

```bash
git clone https://github.com/universal-verification-methodology/learn_uart.git
cd learn_uart
chmod +x scripts/*.sh
./scripts/module.sh 06 --check
```

Then open [module00-intro/README.md](module00-intro/README.md).

## Consume from the parent

```bash
git clone --recurse-submodules \
  git@github.com:universal-verification-methodology/learning.git
ls courses/learn_uart
```

## Author: publish or update

```bash
cd courses/learn_uart
# … edit module README / CHECKLIST / EXAMPLES / transcript …
cd ../..
python .cursor/skills/module-slides/scripts/transcript_to_outline.py \
  courses/learn_uart/moduleNN-slug
bash .cursor/skills/module-slides/scripts/narrate_clips.sh \
  courses/learn_uart/moduleNN-slug
```

## Two learning tracks

Details: [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md).

| Track | Practice surface | Start here |
|-------|------------------|------------|
| **A — Real RTL/TB** | Paper + `.v` (archive; prefer **learn_uart** / **learn_spi** / **learn_i2c**) | [docs/TWO_TRACKS.md](docs/TWO_TRACKS.md) |
| **B — Browser lab** | Platform tools | [uart-frame](https://universal-verification-methodology.github.io/learning/tools/uart-frame/) · [spec-to-rtl](https://universal-verification-methodology.github.io/learning/tools/spec-to-rtl/) · [baud-divider](https://universal-verification-methodology.github.io/learning/tools/baud-divider/) · [uart-oversample](https://universal-verification-methodology.github.io/learning/tools/uart-oversample/) · [uart-errors](https://universal-verification-methodology.github.io/learning/tools/uart-errors/) · [fifo-lab](https://universal-verification-methodology.github.io/learning/tools/fifo-lab/) · [handshake](https://universal-verification-methodology.github.io/learning/tools/handshake/) · [waveform-lab](https://universal-verification-methodology.github.io/learning/tools/waveform-lab/) |

Lab status snapshot: **12 shipped** · **0 planned** (see [docs/MODULES.md](docs/MODULES.md)).

## Module landings

Full status table: **[docs/MODULES.md](docs/MODULES.md)**. Clusters: 00 intro · 01–05 UART timing/errors · 06–07 datapath · 08–10 TB/waves · 11–12 VIP map · 13 wrap.

| Module | Landing |
|--------|---------|
| 00 — Welcome to UART | [module00-intro](module00-intro/README.md) |
| 01 — UART frame | [module01-uart-frame](module01-uart-frame/README.md) |
| 02 — Spec → RTL checklist | [module02-spec-to-rtl](module02-spec-to-rtl/README.md) |
| 03 — Baud / divider | [module03-baud-divider](module03-baud-divider/README.md) |
| 04 — Oversampling | [module04-uart-oversample](module04-uart-oversample/README.md) |
| 05 — UART errors | [module05-uart-errors](module05-uart-errors/README.md) |
| 06 — FIFO in the datapath | [module06-fifo-lab](module06-fifo-lab/README.md) |
| 07 — Handshake | [module07-handshake](module07-handshake/README.md) |
| 08 — Self-check TB | [module08-self-check-tb](module08-self-check-tb/README.md) |
| 09 — TB clock / reset | [module09-tb-clock-reset](module09-tb-clock-reset/README.md) |
| 10 — Waves | [module10-waveform-lab](module10-waveform-lab/README.md) |
| 11 — TB vs UVM map | [module11-tb-vs-uvm-map](module11-tb-vs-uvm-map/README.md) |
| 12 — VIP anatomy | [module12-vip-anatomy](module12-vip-anatomy/README.md) |
| 13 — UART complete | [module13-wrap](module13-wrap/README.md) |

## Browser labs

**Shipped:** [uart-frame](https://universal-verification-methodology.github.io/learning/tools/uart-frame/) · [spec-to-rtl](https://universal-verification-methodology.github.io/learning/tools/spec-to-rtl/) · [baud-divider](https://universal-verification-methodology.github.io/learning/tools/baud-divider/) · [uart-oversample](https://universal-verification-methodology.github.io/learning/tools/uart-oversample/) · [uart-errors](https://universal-verification-methodology.github.io/learning/tools/uart-errors/) · [fifo-lab](https://universal-verification-methodology.github.io/learning/tools/fifo-lab/) · [handshake](https://universal-verification-methodology.github.io/learning/tools/handshake/) · [waveform-lab](https://universal-verification-methodology.github.io/learning/tools/waveform-lab/) · [tb-vs-uvm-map](https://universal-verification-methodology.github.io/learning/tools/tb-vs-uvm-map/) · [self-check-tb](https://universal-verification-methodology.github.io/learning/tools/self-check-tb/) · [tb-clock-reset](https://universal-verification-methodology.github.io/learning/tools/tb-clock-reset/) · [vip-anatomy](https://universal-verification-methodology.github.io/learning/tools/vip-anatomy/). Use Track A +  (archive; prefer **learn_uart** / **learn_spi** / **learn_i2c**) for offline fidelity.

## License

[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — see [`LICENSE`](LICENSE).

