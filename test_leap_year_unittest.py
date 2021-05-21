import unittest
import leap_year

class TestCase(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(leap_year.isLeapYear(8), "8 is a leap year!")
        self.assertEqual(leap_year.isLeapYear(200), "200 is not a leap year!")
        self.assertEqual(leap_year.isLeapYear(800), "800 is a leap year!")




#enables running directly
if __name__ == "__main__":
    unittest.main(verbosity=2)