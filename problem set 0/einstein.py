# Problem Set 0 Question 4
# To convert user inputted mass in kg and convert to energy using Einstein's Formula e = mc^2

# Get user input containing mass
mass = int(input("Enter mass in kg: "))

# Convert to Energy by using given formula
energy = mass * pow(300000000, 2)

# Print the answer
print(f"The energy is joules is: {energy}J")