# Problem Set 4 Question 1
# To convert user input into corresponting emoji using packaged functions

# Importing downloaded python file emoji to convert the input
import emoji

# Getting user input
toemojize = str(input("Input: "))

# If user enters something along with the part to emojize, code deals with it
if " " in toemojize:
    sent, actEmoji = toemojize.split(" ")
    print(sent, emoji.emojize(actEmoji, language = "alias"))
# Else, just converts the input to emoji using .emojize() function
else:
    print(emoji.emojize(toemojize, language = "alias"))