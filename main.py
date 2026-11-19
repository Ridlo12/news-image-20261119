"""News image entry: copy the bundled infographic to the output path.

The image itself (entry.png, 1024x1024) lives in this repository next to
this file. This program only copies those exact bytes to
<output>/entry.png, so every run produces the same file.
"""
import os
import shutil
from pathlib import Path


def main():
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"entry.png missing next to {__file__}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, out_dir / "entry.png")


if __name__ == "__main__":
    main()
