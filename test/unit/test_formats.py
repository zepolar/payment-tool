import unittest
from unittest import TestCase

from exception.file_exception import FormatError, EmptyError
from formats import RegexFormat


class TestRegexFormat(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.regex_format = RegexFormat()

    def test_should_throw_an_exception_when_lines_without_format(self):
        lines = ['PEPE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00',
                 'RENE=SA14:00-18:00,SU20:00']
        with self.assertRaises(FormatError):
            self.regex_format.validate(lines)

    def test_should_throw_an_exception_when_lines_are_empty(self):
        with self.assertRaises(EmptyError):
            self.regex_format.validate(list())


if __name__ == '__main__':
    unittest.main()
