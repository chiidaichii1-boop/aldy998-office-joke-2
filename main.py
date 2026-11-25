"""Make the AI Judge Laugh: the Office Joke Open — make.fun entry.

Writes one one-line office joke to /output/entry.txt.
"""

import os

JOKE = (
    "We held a meeting to decide if this meeting could have been "
    "an email. It could have been an email."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
