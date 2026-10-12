import contextlib
import importlib.util
import io
import string
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT_PATH = Path(__file__).resolve().parents[1] / "pass-generator" / "m-generator.py"
SPEC = importlib.util.spec_from_file_location("password_generator", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
password_generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(password_generator)


class PasswordGenerationTests(unittest.TestCase):
    def test_default_password_has_requested_length_and_all_groups(self):
        password = password_generator.generate_password(32)
        self.assertEqual(len(password), 32)
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.ascii_uppercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertTrue(any(char in password_generator.SYMBOLS for char in password))

    def test_each_enabled_group_is_included(self):
        password = password_generator.generate_password(
            12, lowercase=True, uppercase=False, digits=True, symbols=False
        )
        self.assertTrue(any(char in string.ascii_lowercase for char in password))
        self.assertTrue(any(char in string.digits for char in password))
        self.assertFalse(any(char in string.ascii_uppercase for char in password))
        self.assertFalse(any(char in password_generator.SYMBOLS for char in password))

    def test_no_symbols_option_produces_no_symbols(self):
        password = password_generator.generate_password(40, symbols=False)
        self.assertTrue(all(char.isalnum() for char in password))

    def test_exclude_ambiguous_removes_selected_characters(self):
        password = password_generator.generate_password(100, exclude_ambiguous=True)
        for character in password_generator.AMBIGUOUS_CHARACTERS:
            self.assertNotIn(character, password)

    def test_single_character_group_is_supported(self):
        password = password_generator.generate_password(
            16, lowercase=False, uppercase=False, digits=True, symbols=False
        )
        self.assertEqual(len(password), 16)
        self.assertTrue(password.isdigit())

    def test_length_must_be_within_bounds(self):
        for length in (0, 7, 257, -1):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    password_generator.generate_password(length)

    def test_length_must_be_integer_and_not_boolean(self):
        for length in (20.5, "20", True):
            with self.subTest(length=length):
                with self.assertRaises(ValueError):
                    password_generator.generate_password(length)

    def test_at_least_one_group_must_be_enabled(self):
        with self.assertRaisesRegex(ValueError, "at least one"):
            password_generator.generate_password(
                20, lowercase=False, uppercase=False, digits=False, symbols=False
            )

    def test_cli_outputs_requested_number_of_passwords(self):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            result = password_generator.main(["--length", "24", "--count", "3"])
        passwords = output.getvalue().splitlines()
        self.assertEqual(result, 0)
        self.assertEqual(len(passwords), 3)
        self.assertTrue(all(len(password) == 24 for password in passwords))

    def test_cli_rejects_out_of_range_count(self):
        with self.assertRaises(SystemExit) as error:
            password_generator.main(["--count", "11"])
        self.assertEqual(error.exception.code, 2)

    def test_cli_rejects_when_every_group_disabled(self):
        with self.assertRaises(SystemExit) as error:
            password_generator.main([
                "--no-lowercase", "--no-uppercase", "--no-digits", "--no-symbols"
            ])
        self.assertEqual(error.exception.code, 2)


if __name__ == "__main__":
    unittest.main()
