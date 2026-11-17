"""Write one short settling text to $MAKEFUN_OUTPUT_DIR/entry.txt."""

import os

TEXT = (
    "An hour since the rain, and the garden is still turning it over. "
    "Drops gather along the underside of the leaves and fall when they are ready, "
    "one at a time, back to the soil. "
    "A watering can stands by the shed, half full, with nowhere to be. "
    "You have carried a long line of sentences today, and put each one down again. "
    "These are lighter. "
    "A wren on the fence is trying one note, then trying it again a little lower, "
    "the way someone turns a key in a lock to see if it fits. "
    "It does not need the whole song yet. "
    "The afternoon is long, and nothing in it is asking to be finished."
)


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
