# Problem Set 5 Question 2
# To make a unit test code for PS1Q2

# Re-entering the same code in block and function format as stated
def main():
    greeting = input("Greetings: ").lower()
    print(value(greeting))

def value(greeting):
    if greeting.startswith("hello") == True:
        return "$0"
    elif greeting.startswith("h") == True:
        return "$20"
    else:
        return "$100"
    
if __name__ == "__main__":
    main()