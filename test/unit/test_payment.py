from datetime import datetime
from unittest import TestCase

from exception.file_exception import EmptyError, TimeError
from utils.payment import total_pay_calculation, daily_pay_calculation


class Test(TestCase):

    def test_should_throw_an_exception_when_list_is_empty(self):
        with self.assertRaises(EmptyError):
            total_pay_calculation(list())

    def test_total_payment_is_the_expected_value(self):
        lines = [
            'RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00'
        ]
        expected = {'RENE': 215}
        result = total_pay_calculation(lines)
        self.assertEqual(expected, result, "Boot elements are similar")

    def test_should_throw_an_exception_when_time_format_has_error(self):
        lines = [
            'RENE=MO25:00-26:00'
        ]
        with self.assertRaises(TimeError):
            total_pay_calculation(lines)

    def test_should_throw_an_error_when_day_is_invalid(self):
        with self.assertRaises(ValueError):
            start = datetime(1990, 1, 1, 10, 00)
            end = datetime(1990, 1, 1, 12, 00)
            daily_pay_calculation('LU', start, end)

    def test_should_throw_an_error_when_start_greater_than_end(self):
        with self.assertRaises(ValueError):
            start = datetime(1990, 1, 1, 12, 00)
            end = datetime(1990, 1, 1, 10, 00)
            daily_pay_calculation('MO', start, end)
