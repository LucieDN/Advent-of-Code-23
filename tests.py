import unittest

from Day1 import get_calibration_value

class TestMain(unittest.TestCase):
    def test_day1(self):
        test_text="""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
        self.assertEqual(get_calibration_value(test_text), 142)