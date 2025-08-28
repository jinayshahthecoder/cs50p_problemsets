# Problem Set 4 Question 4
# To create a guessing game with the user prompted range and guess 
# and printing correct information reguarding the guess

# Importing randint function from random
from random import randint

# Making a while loop to get a positive number to use in range from the user
while True:
    try:
        n = int(input("Level: "))
        if n <= 0:
            continue
    except ValueError:
        pass
    else:
        break

# Creating a random number to be guessed
number = randint(1, n)

# Making a while loop to get a positive guess from the user
while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        # Printing the correct statement as per the question
        if guess < number:
            print("Too small!")
            continue
        elif guess > number:
            print("Too large!")
            continue
    except ValueError:
        pass
    else:
        # If guess is correct, ends the loop and the program
        print("Just right!")
        break
