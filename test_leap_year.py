import pytest
import leap_year

class TestPalindrome:
    def test_simple(self):
        assert leap_year.isLeapYear(4) == True
        assert leap_year.isLeapYear(100) == False
        assert leap_year.isLeapYear(400) == True

    def test_advanced(self):
        assert leap_year.isLeapYear("four") == True
        assert leap_year.isLeapYeah("2000") == False
        assert leap_year.isLeapYeah("2000!") == False