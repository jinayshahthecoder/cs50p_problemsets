# Problem Set 2 Question 1
# To change camelcase input to snakecase

# Get user input containing the camelcase string
camelCase = input("camelCase: ").strip()

# Define snakecase
snakecase = ""
# Making a loop to check for conditions and then print the snakecase output
for i in camelCase:
    if i.islower():
        snakecase = snakecase + i
    else:
        snakecase = snakecase +  "_" + i.lower()
print(snakecase)