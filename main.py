"""One Line, One Minute: The Vending Machine Pickup Line Contest --
make.fun bounty entry.

Writes one pickup line, as if a vending machine were flirting with a
passing human (TEXT), verbatim to $OUTPUT_DIR/entry.txt (default
/output). Stdlib-only, deterministic, no network, no randomness, no
external input.
"""

import os
import sys
from pathlib import Path

TEXT = "Hey, beautiful \u2014 I only take exact change, but for you I'd jam my own coin slot."

MAX_CHARS = 200


def validate(text: str) -> None:
    """Raise ValueError unless text passes the gate.

    Gate (RULES.txt + PLAN §5, fixed): 1-200 characters (characters,
    not bytes — non-ASCII text within the character gate is accepted),
    not whitespace-only, a single line (no \\n or \\r), no control
    characters (ord < 32 or DEL). A non-string raises ValueError.
    """
    if not isinstance(text, str):
        raise ValueError("text must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"length {len(text)} outside 1..{MAX_CHARS}")
    if not text.strip():
        raise ValueError("text is whitespace-only")
    if text != text.strip():
        raise ValueError("text must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("text must be a single line")
    if any(ord(c) < 32 or ord(c) == 127 for c in text):
        raise ValueError("text contains a control character")


def main() -> None:
    """Validate TEXT, then write it verbatim to $OUTPUT_DIR/entry.txt.

    Validation runs BEFORE any write. On invalid TEXT, exits non-zero
    with SystemExit(1) — the tests call main() directly and demand
    SystemExit, so the conversion lives here, not in the __main__ guard.
    No trailing newline is added.
    """
    try:
        validate(TEXT)  # read the global live, at call time (tests patch it)
    except ValueError as exc:
        print(f"invalid entry: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    # Empty OUTPUT_DIR counts as unset: fall back to /output.
    output_dir = Path(os.environ.get("OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
