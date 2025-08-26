# Problem Set 3 Question 2
# To create a billing program for 'Felipe's Taqueria' and handling any user errors

# Adding given dictionary to be used in the program
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

# Creating a bill int variable to store amount
bill = 0

# Making a while loop to continuously ask the user for menu items
while True:
    # Checking for correct items
    try:
        item = input("Item: ").title()
        # Checking for KeyErrors or printing the correct output
        try:
            if item in menu:
                bill += menu[item]
                print(f"${bill:.2f}")
        except KeyError:
            pass
    # Handling for EOFErrors to end program when user exhausts item input
    except EOFError:
        print()
        break
