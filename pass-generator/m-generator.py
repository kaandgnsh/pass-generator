#!/usr/bin/env python3
"""Generate strong random passwords locally using Python's secrets module."""

from __future__ import annotations

import argparse
import secrets
import string
import sys

MIN_LENGTH = 8
MAX_LENGTH = 256
MAX_COUNT = 10

SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"
AMBIGUOUS_CHARACTERS = "lI1O0"


def _filter_characters(characters: str, exclude_ambiguous: bool) -> str:
    """Optionally remove visually ambiguous characters from a character set."""
    if not exclude_ambiguous:
        return characters
    return "".join(character for character in characters if character not in AMBIGUOUS_CHARACTERS)


def generate_password(
    length: int = 20,
    *,
    lowercase: bool = True,
    uppercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
    exclude_ambiguous: bool = False,
) -> str:
    """Generate one password with at least one character from each enabled group."""
    if not isinstance(length, int) or isinstance(length, bool):
        raise ValueError("Length must be an integer.")
    if not MIN_LENGTH <= length <= MAX_LENGTH:
        raise ValueError(f"Length must be between {MIN_LENGTH} and {MAX_LENGTH}.")

    groups: list[str] = []
    if lowercase:
        groups.append(_filter_characters(string.ascii_lowercase, exclude_ambiguous))
    if uppercase:
        groups.append(_filter_characters(string.ascii_uppercase, exclude_ambiguous))
    if digits:
        groups.append(_filter_characters(string.digits, exclude_ambiguous))
    if symbols:
        groups.append(_filter_characters(SYMBOLS, exclude_ambiguous))

    groups = [group for group in groups if group]
    if not groups:
        raise ValueError("Enable at least one non-empty character group.")
    if length < len(groups):
        raise ValueError(
            f"Length must be at least {len(groups)} to include every enabled character group."
        )

    alphabet = "".join(groups)
    password_characters = [secrets.choice(group) for group in groups]
    password_characters.extend(
        secrets.choice(alphabet) for _ in range(length - len(password_characters))
    )
    secrets.SystemRandom().shuffle(password_characters)
    return "".join(password_characters)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate cryptographically secure passwords locally.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-l", "--length", type=int, default=20,
        help=f"Password length ({MIN_LENGTH}–{MAX_LENGTH})",
    )
    parser.add_argument(
        "-c", "--count", type=int, default=1,
        help=f"Number of passwords to generate (1–{MAX_COUNT})",
    )
    parser.add_argument("--no-lowercase", action="store_true", help="Exclude lowercase letters.")
    parser.add_argument("--no-uppercase", action="store_true", help="Exclude uppercase letters.")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits.")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols.")
    parser.add_argument(
        "--exclude-ambiguous",
        action="store_true",
        help="Avoid visually ambiguous characters such as l, I, 1, O, and 0.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if not MIN_LENGTH <= args.length <= MAX_LENGTH:
        parser.error(f"--length must be between {MIN_LENGTH} and {MAX_LENGTH}.")
    if not 1 <= args.count <= MAX_COUNT:
        parser.error(f"--count must be between 1 and {MAX_COUNT}.")

    options = {
        "lowercase": not args.no_lowercase,
        "uppercase": not args.no_uppercase,
        "digits": not args.no_digits,
        "symbols": not args.no_symbols,
        "exclude_ambiguous": args.exclude_ambiguous,
    }
    try:
        passwords = [
            generate_password(args.length, **options) for _ in range(args.count)
        ]
    except ValueError as exc:
        parser.error(str(exc))

    for password in passwords:
        print(password)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
