# Problem Set 7 Question 3
# To show time in 24-Hour format for input being 12-hour formatted time

# Importing convert() to be tested
from working import convert
import sys

# Calling all functions
def main():
    test_convert()
    test_rm()
    test_outsideScope()

# To test for proper conversion
def test_convert():
    assert convert("9:00 AM to 5:00 PM") == "9:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 8:00"

# To test for removal of a part
def test_rm():
    assert convert("7 AM 8 PM") == "Error in input"
    assert convert("9 to 8 PM") == "Error in input"

# To test for error in 12-Hour time format
def test_outsideScope():
    assert convert("13:00 AM to 19:00 PM") == "ValueError in hours"
    assert convert("9:70 AM to 5:00 PM") == "ValueError in minutes"
    assert convert("9:00 AM to 5:70 PM") == "ValueError in minutes"

# To execute the program
if __name__ == "__main__":
    main()
