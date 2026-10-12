# Pass Generator

<p align="center">
  <strong>A lightweight, offline password generator powered by Python's cryptographically secure randomness.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <a href="https://github.com/kaandgnsh/pass-generator/actions/workflows/tests.yml"><img src="https://github.com/kaandgnsh/pass-generator/actions/workflows/tests.yml/badge.svg?branch=main" alt="Automated tests"></a>
  <img src="https://img.shields.io/badge/Dependencies-Standard%20Library-444444?style=flat-square" alt="Standard library only">
</p>

## Overview

**Pass Generator** is a command-line utility that creates passwords locally using Python's `secrets` module. It makes no network requests and does not automatically copy or save generated passwords.

## Features

- **Secure randomness:** uses `secrets` rather than the non-cryptographic `random` module.
- **Flexible length:** generate passwords from 8 to 256 characters.
- **Character-set controls:** enable or disable lowercase, uppercase, digits, and symbols.
- **Group guarantees:** every enabled character group contributes at least one character.
- **Batch generation:** create up to 10 passwords in one run.
- **Ambiguous-character filter:** optionally omit visually similar characters such as `l`, `I`, `1`, `O`, and `0`.
- **Offline and dependency-free:** uses only the Python standard library.
- **Tested:** includes unit tests and a Python 3.10–3.12 GitHub Actions workflow.

## Quick start

Requirements: Python 3.10 or newer and Git.

```bash
git clone https://github.com/kaandgnsh/pass-generator.git
cd pass-generator
python pass-generator/m-generator.py
```

This generates one 20-character password using lowercase letters, uppercase letters, digits, and symbols. No package installation is required.

## Examples

### Set the length and number of passwords

```bash
# Generate one 32-character password
python pass-generator/m-generator.py --length 32

# Generate five 24-character passwords
python pass-generator/m-generator.py --length 24 --count 5
```

### Customize the character set

```bash
# Letters and digits only
python pass-generator/m-generator.py --no-symbols

# Lowercase letters, digits, and symbols
python pass-generator/m-generator.py --no-uppercase

# Exclude digits
python pass-generator/m-generator.py --no-digits

# Avoid visually ambiguous characters
python pass-generator/m-generator.py --exclude-ambiguous
```

Options can be combined. At least one non-empty character group must remain enabled. The requested length must be between 8 and 256, and the count must be between 1 and 10.

## CLI reference

| Option | Default | Description |
|---|---:|---|
| `-h`, `--help` | — | Show help and exit |
| `-l`, `--length` | `20` | Password length (8–256) |
| `-c`, `--count` | `1` | Number of passwords (1–10) |
| `--no-lowercase` | Off | Exclude lowercase letters |
| `--no-uppercase` | Off | Exclude uppercase letters |
| `--no-digits` | Off | Exclude digits |
| `--no-symbols` | Off | Exclude symbols |
| `--exclude-ambiguous` | Off | Omit visually ambiguous characters |

View the built-in help:

```bash
python pass-generator/m-generator.py --help
```

## Security notes

- Passwords are printed to your terminal. Consider screen sharing, shoulder-surfing, terminal recording, and session logging.
- The program does not automatically write passwords to disk or copy them to the clipboard.
- Generate a unique password for every account and store it in a reputable password manager.
- Longer passwords generally provide more protection than relying on unusual character substitutions.
- This utility does not assess account security, manage credentials, or replace a password manager.

## Tests

Run the unit tests from the repository root:

```bash
python -m unittest discover -s tests -v
```

Tests cover input validation, length constraints, character groups, ambiguous-character filtering, batch output, and invalid CLI options. The GitHub Actions workflow runs them on Python 3.10, 3.11, and 3.12.

## Project structure

```text
pass-generator/
├── .github/
│   └── workflows/
│       └── tests.yml
├── pass-generator/
│   └── m-generator.py
├── tests/
│   └── test_password_generator.py
└── Readme.md
```

## Author

**Kaan DOĞAN** · [GitHub](https://github.com/kaandgnsh) · [LinkedIn](https://www.linkedin.com/in/kaan-do%C4%9Fan-911663280/) · [Instagram](https://instagram.com/kaandgn.sh)
