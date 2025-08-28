# Problem Set 4 Question 2
# To convert user input string to its ASCII art format by istalling and using pyfiglet

# Importing necessary components as stated in the question
from pyfiglet import Figlet
import sys

# Using figlet commands as advised
figlet = Figlet()

# Checking if user asked for another font style by use of command line arguements
if len(sys.argv) == 1:
    # Asking for input and printing the answer in ASCII format
    toTurn = input("Input: ")
    print(figlet.renderText(toTurn))
elif len(sys.argv) == 3:
    # Checking for errors in user command line input
    if sys.argv[1] == "-f" or "--font":
        # Checking if user mentioned font style exists in database
        if sys.argv[2] in figlet.getFonts():
            # Setting font style as user mentioned and printing the answer in that format
            figlet.setFont(font=sys.argv[2])
            toTurn = input("Input: ")
            print("Output:", figlet.renderText(toTurn), sep = "\n")
        # Else, informing user of error and closing the program
        else:
            print("Invalid usage")
            sys.exit()
    # Else, informing user of error and closing the program
    else:
        print("Invalid usage")
        sys.exit()