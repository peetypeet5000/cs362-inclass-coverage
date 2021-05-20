#Leap Year Checker:
import sys


#Takes string input and checks if it is a leap year
# Input - String that is an integer
# Output - returns string saying if year is leap or not
def isLeapYear(input):
    valid = True
    output = ""

    # See if user entered an integer
    try:
        year = int(input)
    except ValueError:
        output = "Please enter a valid integer"
        valid = False

    #If it was an int, run the leap year calc
    if(valid):
        if(year % 4 == 0):
            if(year % 100 == 0 and year % 400 != 0 and valid):
                output = str(year) + " is not a leap year!"
            else:
                output = str(year) + " is a leap year!"
        else:
            output = str(year) + " is not a leap year!"

    return output



