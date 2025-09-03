# Problem Set 7 Question 3
# To show time in 24-Hour format for input being 12-hour formatted time

# Importing re to search for the times
import re

# Defining main to get input and pass it to convertN() then print the final answer
def main():
    print(convert(input("Hours: ")))

# Function using re.search() function for answer
def convert(s):
    # Searching for below variables and assigning them
    if matches := re.search(r"(1[0-9]|[0-9]):?([0-9][0-9]|\s)\s?(AM|PM)\sto\s(1[0-9]|[0-9]):?([0-9][0-9]|\s)\s?(AM|PM)", s):
        t1, m1, mer1, t2, m2, mer2 = matches.groups()
        # Checking and managing minutes inputted
        if m1 == " ":
            m1 = ":00"
        elif m1.isdigit():
            if 0 <= int(m1) <= 59:
                m1 = ":" + m1
            else:
                return "ValueError in minutes"
        if m2 == " ":
            m2 = ":00"
        elif m2.isdigit():
            if 0 <= int(m2) <= 59:
                m2 = ":" + m2
            else:
                return "ValueError in minutes"
        # Checking for any error in hours inputted
        if int(t1) > 12 or int(t2) > 12:
            return "ValueError in hours"
        # Converting into 24-hour format
        if mer1 == "AM":
            t2 = str(int(t2) + 12)
        elif mer2 == "AM":
            t1 = str(int(t1) + 12)
        # Returning answer
        return f"{t1}{m1} to {t2}{m2}"
    else:
        return "Error in input"

# To execute the program
if __name__ == "__main__":
    main()