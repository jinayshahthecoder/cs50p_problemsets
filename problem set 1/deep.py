# Problem Set 1 Question 1
# To  output yes to the uder inputted answer the Great Question of Life, the Univere and Everything 
# from The Hitchhiker’s Guide to the Galaxy

# Get user input containing the answer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

# Checking the answer though the use of if, elif and else conditionals and printing the answer
if answer == "42" :
    print("Yes")
elif answer == "fourty two":
    print("Yes")
elif answer == "fourty-two":
    print("Yes")
else:
    print("No")