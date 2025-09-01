# Problem Set 2 Question 3
# To shorten tweets by removing vowels from user input of string

# Get user input of the string of tweet and initialize a list of vowels
twitter = input("Input: ")
vwl = "aeiouAEIOU"

# Create a loop to remove the vowels from the output
print("Output: ", end="")
for i in twitter:
    if i not in vwl:
        print(i, end="")