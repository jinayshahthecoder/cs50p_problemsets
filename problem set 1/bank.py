# Problem Set 1 Question 2
# To give user money based on their greetings as a reference to the popular show 'Seinfeld'

# Get user input containing greetings
greet = input("Greetings: ").lower()

# Check with given conditionals and print the assigned money
if greet.startswith("hello") == True:
    print("$0")
elif greet.startswith("h") == True:
    print("$20")
else:
    print("$100")