import pytest
import leap_year

class TestPalindrome:
    def test_simple(self):
        assert leap_year.isLeapYear(4) == "4 is a leap year!"
        assert leap_year.isLeapYear(100) == "100 is not a leap year!"
        assert leap_year.isLeapYear(400) == "400 is a leap year!"

    def test_advanced(self):
        assert leap_year.isLeapYear("four") == "Please enter a valid integer"
        assert leap_year.isLeapYear("2000") == "2000 is a leap year!"
        assert leap_year.isLeapYear("2000!") == "2000 is a leap year!"