# Problem Set 2 Question 5
# To assign calorific values to common fruits and display them as per requests of users

# Get user input string of fruit to check in dictionary
fruit = input("Fruit: ").lower()

# Creating a dictionary by use of given data
fruit_dict = {"apple" : 130, "avocado" : 50, "banana" : 110, "cantaloupe" : 50, "grapefruit" : 60, "grapes" : 90, 
              "honeydew melon" : 50, "kiwi fruit" : 90, "lemon" : 15, "lime" : 20, "nectarine" : 60, "orange" : 80, "peach" : 60, 
              "pear" : 100, "pineapple" : 50, "plums" : 70, "strawberries" : 50, 
              "sweet cherries" : 100, "tangerine" : 50, "watermelon" : 80}

# Check if fruit is in database or not and print the output
if fruit in fruit_dict:
    print(f"Calories in fruit: {fruit_dict[fruit]}")
else:
    print("Not in database")
