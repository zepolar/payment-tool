import os
import unittest
from unittest import TestCase

from exception.file_exception import FormatError, EmptyError
from files import RegexFile

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TestRegexFile(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.file = RegexFile()

    def test_should_throw_an_exception_when_filename_is_empty(self):
        with self.assertRaises(ValueError):
            self.file.read_file("")

    def test_should_throw_an_exception_when_filename_is_none(self):
        with self.assertRaises(ValueError):
            self.file.read_file(None)

    def test_should_throw_an_exception_when_filename_not_exist(self):
        with self.assertRaises(FileExistsError):
            self.file.read_file("algo.txt")

    def test_should_fail_when_format_is_not_valid(self):
        with self.assertRaises(FormatError):
            self.file.read_file(os.path.join(__location__, "invalidFile.txt"))

    def test_should_fail_when_files_is_emtpy(self):
        with self.assertRaises(EmptyError):
            self.file.read_file(os.path.join(__location__, "emptyFile.txt"))

    def test_should_calculate_values(self):
        self.file.read_file(os.path.join(__location__, "validFile.txt"))


if __name__ == '__main__':
    unittest.main()
