#!/usr/bin/env python3
"""Currently Wilting — entry program.

writes one line, a houseplant's out-of-office auto-reply, to
/output/entry.txt. Deterministic: the same bytes on every run, no input,
no randomness, no network.

The auto-reply: the plant is currently wilting, and it turns the classic
OOO line — "your message is important to me" — back on its owner. The
joke is driven by the plant's own life: water, neglect, and long stretches
of being ignored. No office cliche, no worn-out auto-reply line — the plant files its complaint as a status update.
"""

from pathlib import Path

ENTRY = (
    "Thank you for your email. I'm currently wilting. Your message is important to me — unlike me to my owner.\n"
)

# The gate: /output/entry.txt must be UTF-8 text of 1 to 120 characters,
# not only white space. Refuse to write anything that would fail it.
assert 1 <= len(ENTRY.strip()) <= 120, "entry must be 1-120 characters"
assert ENTRY.strip(), "entry must not be only white space"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
