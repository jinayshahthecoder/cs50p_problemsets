# Problem Set 2 Question 2
# To simulate a coke vending machine and manage the cost of a 50 cent bottle

# Defining the cost and creating a loop to ensure function of machine
cost  = 50
while True:
    # Get the user input of the coin submitted and permit its use
    coke = int(input("Input coin: "))
    if coke in [5, 10, 25]:
        cost = cost - coke
    else:
        print("We only accept 5, 10 or 25 cent coins.")
        break
    # Breaking the loop if conditions are met i.e. if coke can be released with change or not etc and printing the answer
    if cost == 0:
        print("Here's a coke!")
        break
    elif cost < 0:
        print("Here's a coke!")
        print("Change to give back:", cost * -1)
        break
    else:
        print("Amount left to pay for a coke:", cost)