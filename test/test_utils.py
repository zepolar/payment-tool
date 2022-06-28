import unittest
from datetime import datetime as dt
from unittest import TestCase

from utils.constants import fmt_hour, schedule
from utils.payment import daily_pay_calculation


class Test(TestCase):

    def test_should_fail_when_day_is_empty(self):
        with self.assertRaises(ValueError):
            daily_pay_calculation("", start=dt.now(), end=dt.now())

    def test_should_fail_when_end_time_is_greater_than_start_time(self):
        start_date = dt(2022, 1, 1, 10, 0, 0)  # 10am
        end_date = dt(2022, 1, 1, 9, 0, 0)  # 9am
        with self.assertRaises(ValueError):
            daily_pay_calculation("MO", start_date, end_date)

    def test_should_accept_valid_days(self):
        valid_days = schedule.keys()
        start_date = dt.strptime("10:00", fmt_hour)  # 10am
        end_date = dt.strptime("12:00", fmt_hour)  # 12am
        self.assertIsNotNone([daily_pay_calculation(day, start_date, end_date) for day in valid_days])


if __name__ == '__main__':
    unittest.main()
