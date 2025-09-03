# Problem Set 8 Question 1
# To take the user's DOB as input and calculate and display the minutes since DOB and today

from seasons import getDOB
from datetime import date

# Calling all functions
def main():
    test_getDOB()

# To test for valid DOB
def test_getDOB():
    assert getDOB("1970-01-01") == date(1970, 1, 1)
    assert getDOB("jan 1") == "Invalid Date"

# To execute the program
if __name__ == "__main__":
    main()