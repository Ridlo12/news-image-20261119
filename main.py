"""Entry point for the News Image 19 November 2026 entry.

The artwork itself is the pre-rendered file ``entry.png`` that sits next to
this script (a 1024x1024 newspaper-style infographic drawn with Pillow).
This program does nothing creative at run time: it simply copies the bytes
of ``entry.png`` into the output directory requested by make.fun, so every
run produces exactly the same file.

The destination directory is taken from the ``MAKEFUN_OUTPUT_DIR``
environment variable and falls back to ``/output`` when it is not set.
"""

import os
import shutil
import sys
from pathlib import Path


def _source_path() -> Path:
    """Return the path of the artwork bundled next to this script."""
    return Path(__file__).resolve().parent / "entry.png"


def _output_dir() -> Path:
    """Return the output directory from the environment, default /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> int:
    source = _source_path()
    if not source.is_file():
        print(f"error: entry.png not found next to this script ({source})", file=sys.stderr)
        return 1

    destination_dir = _output_dir()
    destination_dir.mkdir(parents=True, exist_ok=True)

    destination = destination_dir / "entry.png"
    shutil.copyfile(source, destination)
    if destination.stat().st_size != source.stat().st_size:
        print("error: copied file size does not match entry.png", file=sys.stderr)
        return 1
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
