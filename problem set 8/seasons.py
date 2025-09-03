# Problem Set 8 Question 1
# To take the user's DOB as input and calculate and display the minutes since DOB and today

# Importing necessary libraries and classes
from datetime import date
import sys
import inflect

# As per documentation of inflect
p = inflect.engine()

# Defining the main function
def main():
    dob = input("Date of Bith: ")
    dob = getDOB(dob)
    if dob == "Invalid Date":
        sys.exit("Invalid Date")
    # Getting the current time from date
    current = date.today()
    # Printing the final answer
    print(findTime(current, dob))

# Function to check and validate the DOB inputted
def getDOB(dob):
    # Checks for correct format
    try:
        dob = date.fromisoformat(dob)
        return dob
    # Else exits early and informs user of error
    except ValueError:
        return "Invalid Date"

# Function to find the minutes passed
def findTime(curr, dob):
    # Overloading as mentioned in documentation and converting time into days
    time = (curr - dob).days
    # Converting time to minutes
    time = int(time) * 60 *24
    # Using "p" to return minutes in correct word format
    return p.number_to_words(time,andword="").capitalize() + " minutes"

# To execute the program
if __name__ == "__main__":
    main()