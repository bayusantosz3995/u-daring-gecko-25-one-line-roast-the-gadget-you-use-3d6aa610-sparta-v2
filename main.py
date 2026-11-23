"""One-line roast entry for make.fun's "One-Line Roast: The Gadget You Use Every Day" bounty.

The entry is a single roast line about wireless earbuds: they promised
freedom, and the left one took the promise literally — it walked out on
its owner — for the dust. The sting is the betrayal: the earbud chose
dust over the person who bought it.
"""

import os
import sys

TEXT = "My wireless earbuds promised freedom — the left one ditched me for the dust under the sofa."


def main() -> int:
    if not (1 <= len(TEXT) <= 200) or not TEXT.strip():
        print("gate failed: entry must be 1-200 non-whitespace characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != TEXT:
        print("gate failed: entry.txt does not match TEXT byte-for-byte", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(TEXT)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
