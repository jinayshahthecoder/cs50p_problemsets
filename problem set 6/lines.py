# Problem Set 6 Question 1
# To count the number of lines inside a program while ignoring whitespace and comments

# Importing sys to get cmd-line argument from user
import sys

# Defining main() to exit program or call lineCounter() depending on input
def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".py"):
        lineCounter()
    else:
        sys.exit("Not a python file")

# Function to count the number of lines in given file by the use of loops, if statements and file i/o
def lineCounter():
    # Defining line count to increment in loop
    lineCount = 0
    # Checking if file exists
    try:
        # Reading the given file by treating name as "file"
        with open(sys.argv[1]) as file:
            # Making a loop to check the line
            for line in file:
                # Checking if line is a comment or blan
                if line.lstrip().startswith("#") or line.strip() == "":
                    continue
                # Else updating the lineCount
                else:
                    lineCount += 1
            # Printing the final answer
            print(f"{lineCount}")
    # Handling FileNotFoundError as requested by question
    except FileNotFoundError:
        print("File does not exist")

# To execute the program
if __name__ == "__main__":
    main()