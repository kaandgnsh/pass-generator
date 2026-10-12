# Pass Generator

<p align="center">
  <strong>A lightweight command-line password generator built with Python's cryptographically secure random source.</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.10+">
  <a href="https://github.com/kaandgnsh/pass-generator/actions/workflows/tests.yml"><img src="https://github.com/kaandgnsh/pass-generator/actions/workflows/tests.yml/badge.svg?branch=main" alt="Tests"></a>
  <img src="https://img.shields.io/badge/Dependencies-Standard%20Library-444444?style=flat-square" alt="Standard library only">
</p>

## Overview

Pass Generator creates random passwords locally using Python's `secrets` module. It does not make network requests, send passwords to a service, or save generated passwords to disk.

## Features

- **Cryptographically secure randomness** using `secrets`, not the predictable `random` module.
- **Configurable length** from 8 to 256 characters (default: 20).
- **Character controls** for lowercase letters, uppercase letters, digits, and symbols.
- **Guaranteed character groups:** each enabled, non-empty group contributes at least one character.
- **Multiple passwords:** generate up to 10 in one run.
- **Ambiguous-character filter** for visually similar characters.
- **No third-party dependencies** and no network access.
- **Unit tests and CI** for generation rules and CLI validation.

## Requirements

- Python 3.10 or newer
- Git

## Installation

Clone the repository:

```bash
git clone https://github.com/kaandgnsh/pass-generator.git
cd pass-generator
```

No package installation is required.

## Usage

### Generate a password

From the repository root:

```bash
python pass-generator/m-generator.py
```

By default, it generates one 20-character password using lowercase letters, uppercase letters, digits, and symbols.

### Choose length and quantity

```bash
python pass-generator/m-generator.py --length 32
python pass-generator/m-generator.py --length 24 --count 5
```

### Customize the character set

```bash
# Letters and digits only
python pass-generator/m-generator.py --no-symbols

# Exclude uppercase letters
python pass-generator/m-generator.py --no-uppercase

# Exclude digits
python pass-generator/m-generator.py --no-digits

# Avoid visually ambiguous characters such as l, I, 1, O, and 0
python pass-generator/m-generator.py --exclude-ambiguous
```

Combine options as needed. At least one character group must remain enabled. The requested length must be between 8 and 256, and the count between 1 and 10.

### See all options

```bash
python pass-generator/m-generator.py --help
```

## Security notes

- Generated passwords are printed to the terminal. Be aware of shoulder-surfing, terminal recordings, screen sharing, and shell/session logging.
- The program does not automatically copy passwords to the clipboard or store them in files.
- Use a unique password for each account and store it in a reputable password manager.
- Strength depends on both the character set and length. Increasing length is generally preferable to relying on unusual substitutions.
- This utility is intended for generating passwords for accounts and systems you are authorized to use.

## Tests

Run the test suite from the repository root:

```bash
python -m unittest discover -s tests -v
```

The tests check length boundaries, enabled character groups, ambiguous-character filtering, multiple outputs, and invalid CLI arguments. GitHub Actions runs the suite on Python 3.10, 3.11, and 3.12.

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
