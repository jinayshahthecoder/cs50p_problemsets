# Problem Set 4 Question 4
# To create a addition question creator with user controlled 'n' digits of numbers to be added

# Importing random to create random digits to use in generate_integer()
import random

# Defining main() and other functions as per the question
def main():
    # Fetching number of digits from get_level()
    lvl = get_level()
    # Creating int variables to store number of questions, attempts at a given question and total user score at end
    questions = 0
    attempts = 0
    score = 0
    # Creating a while loop to ask ten questions
    while questions < 10:
        # Fetching 2 integers from the generate_integer() function
        a, b = generate_integer(lvl)
        # Creating a while loop for the recently made question
        while True:
            # Checking if attempts have reached their end
            if attempts == 3:
                print(f"{a} + {b} = {a + b}")
                attempts = 0
                break
            # Trying to get an input from the user that is the correct answer
            try:
                answer = int(input(""))
                # Checking for the correct answer
                if answer == a + b:
                    score += 1
                    break
                # Else, adds attempts and retrys to get the answer
                else:
                    print("EEE")
                    attempts += 1
                    continue
            # Incase of a ValueError, treats input as the wrong answer and continues
            except ValueError:
                print("EEE")
                attempts +=1
                pass
        questions += 1
    # Printing the final score of the user
    print(f"Score: {score}")

# Getting the level from the user according to given conditions and returns it to main
def get_level():
    while True:
        try:
            digit = int(input("Level: "))
            if digit not in [1, 2, 3]:
                continue
        except ValueError:
            pass
        else:
            break
    return digit

# Generating 2 random integers to be used in the addition by use of random.randint() function
def generate_integer(level):
    x = random.randint(0, pow(10, level) - 1)
    y = random.randint(0, pow(10, level) - 1)
    return x, y

# Checking for programs that import this file
if __name__ == "__main__":
    main()