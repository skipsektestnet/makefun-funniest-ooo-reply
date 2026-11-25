"""Funniest One-Line Out-of-Office Reply: writes the entry to /output/entry.txt.

Why this line: a plain out-of-office setup, then a slow escalation of
abandonment — laptop at home, phone in a drawer — landing on the punch that
the email has been entrusted to literally no one. Specific, concrete, and
the joke is the last five words.
"""

import os

# The entry itself: one line, one out-of-office auto-reply.
ENTRY = (
    "Out of office until Monday. I left my laptop at home, my phone in a "
    "drawer, and your email in the capable hands of no one."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()
