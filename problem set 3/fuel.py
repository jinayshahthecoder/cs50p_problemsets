# Problem Set 3 Question 1
# To make a fuel gauge checker by taking correct prompts from the user and returning valid output and handling errors

# Making a while loop to continuously ask the user if values are correct
while True:
    # Checking if user input is valid
    try:
        x, y = input("Fraction: ").split("/")
        # Converting string input to integer and checking if error occurs then passing errors to 'except' conditions
        x = int(x)
        y = int(y)
        # Printing output based on the given conditions
        if x < 0 or y < 0 or x > y:
            pass
        else:
            inTank = (x / y) * 100
            if inTank > 99:
                print("F")
            elif inTank < 1:
                print("E")
            else:
                print(f"{inTank:.0f}%")
            break
    # Handling ValueError and ZeroDivisionError by passing the code to the while loop prompt again
    except ValueError:
        pass
    except ZeroDivisionError:
        pass