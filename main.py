"""The One-Line Exit — a one-line resignation letter.

The joke: the office Wi-Fi has been down for six weeks, and the writer
announces that, as of today, so has he. One word — "down" — does double
duty: first as a dead network, then as a person who has finally stopped
functioning. The formal opening ("Please accept my resignation") grounds
it as a real letter, so the collapse into the punchline feels like a
genuine sendable note rather than a gag — the reader expects a reason
and gets a confession instead. It names a specific, recognizable
workplace misery, and lands the punchline in the
last three words, where the reader least expects it.
"""

import os
from pathlib import Path

LINE = "Please accept my resignation: the office Wi-Fi has been down for six weeks, and as of today, so have I."


def output_dir() -> Path:
    """Return the output directory, honouring MAKEFUN_OUTPUT_DIR."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> int:
    """Write the one-line resignation letter to entry.txt."""
    assert 1 <= len(LINE) <= 140, "line must be 1-140 characters"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only whitespace"
    assert LINE == LINE.strip(), "line must not have leading/trailing whitespace"
    LINE.encode("utf-8")

    out_dir = output_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "entry.txt"
    out_path.write_text(LINE, encoding="utf-8", newline="")
    # Round-trip check: what landed on disk must be exactly the line.
    assert out_path.read_text(encoding="utf-8") == LINE
    assert not out_path.read_bytes().endswith(b"\n")
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
