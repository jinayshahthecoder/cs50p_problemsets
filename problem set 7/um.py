# Problem Set 7 Question 4
# To return the number of "um" in the given string input

# Importing re to find the count
import re

# Defining main to get input and pass it to count() then print the final answer
def main():
    print(count(input("Text: ")))

# Function to count using re.findall() function
def count(s):
    matches = re.findall(r"\bum\b", s, re.IGNORECASE)
    # Returning the count
    return len(matches)

# To execute the program
if __name__ == "__main__":
    main()