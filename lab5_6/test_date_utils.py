# test_date_utils.py

import unittest
from date_utils import is_leap_year, days_between_dates, get_current_date, add_days_to_date, has_date_passed

class TestDateUtils(unittest.TestCase):

    def test_is_leap_year(self):
        self.assertTrue(is_leap_year(2020))
        self.assertFalse(is_leap_year(2019))
        self.assertTrue(is_leap_year(2000))
        self.assertFalse(is_leap_year(1900))

    def test_days_between_dates(self):
        self.assertEqual(days_between_dates("2020-01-01", "2020-01-02"), 1)
        self.assertEqual(days_between_dates("2020-01-02", "2020-01-01"), -1)
        self.assertEqual(days_between_dates("2020-01-01", "2020-01-01"), 0)

    def test_get_current_date(self):
        # Since this test will be run at an unknown time, we just check if it returns a string
        self.assertIsInstance(get_current_date(), str)

    def test_add_days_to_date(self):
        self.assertEqual(add_days_to_date("2020-01-01", 1), "2020-01-02")
        self.assertEqual(add_days_to_date("2020-01-01", -1), "2019-12-31")

    def test_has_date_passed(self):
        self.assertTrue(has_date_passed("2000-01-01"))
        self.assertFalse(has_date_passed("2999-01-01"))

if __name__ == '__main__':
    unittest.main()
