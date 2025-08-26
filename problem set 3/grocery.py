# Problem Set 3 Question 3
# To impliment a simple grocery list wherein items and number of items entered are displayed in alphabetic order

# Creating a dictionary to store the inputs and amount of times same input occurs
bill = {}

# Making a while loop to continuously input items until EOFError occurs
while True:
    # Checking for Error incase user wants list to end
    try:
        # Inputs the item from the user and converts it into uppercase
        item = input().upper()

        # Checking if item already exists in the bill then increasing amount of times entered
        if item in bill:
            bill[item] += 1
        
        # Else, adding it automatically
        else:
            bill[item] = 1

    # Printing the bill as commanded when EOFError occurs
    except EOFError:
        print()
        for num in sorted(bill):
            print(bill[num], num)
        break