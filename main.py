"""Entry point for the News Image 19 November 2026 make.fun entry.

The artwork is a finished 1024x1024 newspaper-style infographic stored
in ``entry.png`` next to this script. This program does not regenerate the
image; it simply places an exact copy of it into the output directory so
the evaluation harness can pick it up.

The output directory comes from the ``MAKEFUN_OUTPUT_DIR`` environment
variable and defaults to ``/output`` when the variable is not set. Every
run writes the identical bytes, because the file is copied byte for byte.
"""

import os
import shutil
import sys

SOURCE_NAME = "entry.png"
OUTPUT_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def resolve_paths():
    """Return the (source, destination) paths for this run."""
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", DEFAULT_OUTPUT_DIR)
    destination = os.path.join(output_dir, OUTPUT_NAME)
    return source, output_dir, destination


def main():
    source, output_dir, destination = resolve_paths()

    if not os.path.isfile(source):
        print(
            f"error: source image not found: {source} "
            "(entry.png must sit next to main.py)",
            file=sys.stderr,
        )
        return 1

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, destination)

    expected = os.path.getsize(source)
    actual = os.path.getsize(destination)
    if actual != expected:
        print(
            f"error: copied file size {actual} bytes does not match "
            f"source size {expected} bytes",
            file=sys.stderr,
        )
        return 1

    print(f"wrote {destination} ({actual} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
