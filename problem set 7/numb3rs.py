# Problem Set 7 Question 1
# To output Boolean based on user inputted IPv4 Address

# Importing re to use search() function later
import re

# Defining main to get input and pass it to validate() then print the final answer
def main():
    print(validate(input("IPv4 Address: ")))

# Function to check for correct IPv4 address
def validate(ip):
    # Checking if matches is true and matches uses re.search() function to find and group to values of IPv4 address
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        # Checking if all numbers entered lie between 0 and 255
        for n in matches.groups():
            # Checking for extra zeroes
            if not n.startswith("00"):
                if 0 <= int(n) <= 255:
                    continue
                else:
                    return False
            else:
                return False
        # Return True if loop finds correct values
        return True
    # Else if no macthes found that are numbers, return False
    else:
        return False

# To execute the program
if __name__ == "__main__":
    main()