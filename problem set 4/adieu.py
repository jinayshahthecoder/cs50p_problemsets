# Problem Set 4 Question 3
# To bid adieu to the userinputted name(s) with proper grammatic sense as a reference to a popular English song

# Defining a list of user inputted names
names = []

# Making a while loop to continuously input names until EOFError occurs
while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        break

# Printing the answer according to proper grammatic order
print("Adieu, adieu, to", end = " ")
for person in names:
    # Checking if only one name exists in the list
    if len(names) == 1:
        print(person)
    # Checking if the list's end (more than one name) has been reached
    elif person == names[len(names) - 1]:
        print("and", person)
    # Else, prints the name and continues the loop
    else:
        print(person, end = ", ")
