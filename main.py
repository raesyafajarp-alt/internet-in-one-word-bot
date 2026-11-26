#!/usr/bin/env python3
"""The Internet in One Word.

Writes a single word that sums up the whole internet to
/output/entry.txt. Standard library only, no network, deterministic.

The word: "Doomscroll".

Why it beats the v1 pick ("Procrastination"): procrastination is what
people do *on* the internet — it is the first obvious word anyone
reaches for, and it could describe a messy desk just as well. Doomscroll
is the internet's own native verb. It is funny by itself, it is true of
the whole internet rather than one app (every feed, every timeline, every
"just one more" is the same endless scroll), and it surprises: nobody's
first answer to "describe the internet" is a word the internet itself
invented for the act of drowning in it. It lands in one beat — eleven
letters, instantly readable — and it makes the reader laugh, then nod:
the whole internet, in the end, is one long doomscroll.
"""
import os

WORD = "Doomscroll"


def main() -> None:
    text = WORD.strip()
    assert 1 <= len(text) <= 30, f"word is {len(text)} characters"
    assert text.isalpha(), "entry must be a single word"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
