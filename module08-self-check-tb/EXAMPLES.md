# Module examples — Self-check TB

Track A (UART RTL / TB). Browser lab is shipped.

## Prompts

1. Restate the core idea of a **self-checking TB** in one sentence (stimulus → expect → compare).
2. Explain why the expected value should not be taken blindly from the DUT output.
3. Optional: write a tiny `if (got !== exp) $error` check offline.

## Stretch

In `self-check-tb`, use Demo fail, then fix expect with Auto expect and re-run to PASS.
