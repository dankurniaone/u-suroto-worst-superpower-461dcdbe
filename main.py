#!/usr/bin/env python3
"""Worst Superpower — make.fun entry.

Writes one line (at most 140 characters) inventing the most useless
superpower imaginable to /output/entry.txt.

Tournament (specificity / surprise / freshness, each 1-5):
 1. Teleport anywhere, only to places I've been, only while standing still — 4/3/3 = 10
 2. Hear any conversation in the world, only in a language I don't speak, only the boring parts — 5/4/4 = 13
 3. Turn invisible, but only my left elbow, only on Tuesdays — 4/3/2 = 9
 4. Read minds, but only my own, and only thoughts I've already had — 5/5/4 = 14
 5. Stop time for exactly one second, only while I'm asleep — 5/4/4 = 13
 6. Summon any object I want, as long as it's already in my hand — 4/5/3 = 12
 7. Fly, but only three inches off the ground, only downhill — 4/3/2 = 9
 8. Predict the future with perfect accuracy, but only events that happened yesterday — 5/5/4 = 14 (WINNER)
 9. Talk to animals, but they all just complain about the weather — 4/4/4 = 12
10. Perfect night vision, but only in rooms with the lights on — 5/4/4 = 13

Winner: #8. The contradiction lands in one breath and is clear on a single
reading, while #4 needs a beat to parse whose mind it is. Predicting
yesterday is genuinely useless (you already know it happened), not a curse,
and it does not quietly help.
"""

import argparse
import sys
from pathlib import Path

ENTRY = "I can predict the future with perfect accuracy, but only events that happened yesterday."
MIN_CHARS = 1
MAX_CHARS = 140


def check_entry(text: str) -> None:
    """Enforce the gate: UTF-8 text of 1 to 140 characters, not only whitespace."""
    if not isinstance(text, str):
        raise ValueError("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} chars, gate needs {MIN_CHARS}-{MAX_CHARS}")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")


def write_entry(out_dir: Path) -> Path:
    check_entry(ENTRY)
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    return target


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Write the worst superpower entry.")
    parser.add_argument("--out", default="/output", help="output directory")
    parser.add_argument("--check", action="store_true", help="only verify the gate, write nothing")
    parser.add_argument("--self-test", action="store_true", help="write to a temp dir and verify the bytes read back")
    args = parser.parse_args(argv)

    if args.check:
        check_entry(ENTRY)
        print(f"check ok: {len(ENTRY)} chars, within {MIN_CHARS}-{MAX_CHARS}")
        return 0

    if args.self_test:
        import tempfile

        with tempfile.TemporaryDirectory() as tmp:
            target = write_entry(Path(tmp))
            back = target.read_text(encoding="utf-8")
            assert back == ENTRY, "round-trip mismatch"
            print(f"self-test ok: {len(back)} chars, byte-identical")
        return 0

    target = write_entry(Path(args.out))
    print(f"wrote {target} ({len(ENTRY)} chars, gate {MIN_CHARS}-{MAX_CHARS})")
    print(f"gate: {len(ENTRY)} chars, UTF-8, non-blank — valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
