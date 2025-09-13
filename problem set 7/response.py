# Problem Set 7 Question 5
# To validate user's email id using validators library

# Importing email() from validators to check validity
from validators import email

# Getting input from user
inp = input("What's your email address? ")

# If valid, print valid
if email(inp) == True:
    print("Valid")
# Else, print invalid
else:
    print("Invalid")
