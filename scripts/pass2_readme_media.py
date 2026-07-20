#!/usr/bin/env python3
"""Update module README Media sections after module-slides pass 1."""
from __future__ import annotations

import re
from pathlib import Path

MEDIA_BLOCK = """## Media

| Artifact | Path |
|----------|------|
| Transcript | [transcript.md](transcript.md) |
| Outline | [outline.yaml](outline.yaml) |
| Slides | [slides.pptx](slides.pptx) · [slides.pdf](slides.pdf) |
| Video | [video.mp4](video.mp4) |
| Quiz | [quiz.json](quiz.json) |
"""

PLANNED = re.compile(
    r"## Media \(planned\)\s*\n\s*\n"
    r"\| Artifact \| Path \|\s*\n"
    r"\|[-| ]+\|\s*\n"
    r"\| Outline \| \[outline\.yaml\]\(outline\.yaml\) \|\s*\n"
    r"\| Transcript stub \| \[transcript\.md\]\(transcript\.md\) \|\s*\n"
    r"\| Slides / video \| generate later with \*\*module-slides\*\* \|",
    re.MULTILINE,
)


def main() -> None:
    course = Path(__file__).resolve().parents[1]
    updated = 0
    for readme in sorted(course.glob("module*/README.md")):
        text = readme.read_text(encoding="utf-8")
        original = text
        if "## Media (planned)" in text:
            text = PLANNED.sub(MEDIA_BLOCK, text)
        elif readme.parent.name == "module13-wrap" and "## Media" not in text:
            text = text.replace("## Checklist", MEDIA_BLOCK + "\n## Checklist", 1)
        if text != original:
            readme.write_text(text, encoding="utf-8")
            print(f"OK: {readme.parent.name}")
            updated += 1
    print(f"Updated {updated} README(s)")


if __name__ == "__main__":
    main()
