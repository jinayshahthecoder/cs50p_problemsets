# Problem Set 1 Question 4
# To make an interpreter for maths in python

# Get the user input string then split it into the three components
x, y, z = input("Expression: ").strip().split(" ")

# Convert given strings to float datatype
x = float(x)
z= float(z)

# Check the given conditions and print the answer
if y == "+":
    print(f"{x + z:.1f}")
elif y == "-":
    print(f"{x - z:.1f}")
elif y == "*":
        print(f"{x * z:.1f}")
elif y == "/":
        # Check whether division is possible or not
        if z == 0:
            print("Not possible")
        else:
            print(f"{x / z:.1f}")
else:
    print("No")
