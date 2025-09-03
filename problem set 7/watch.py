# Problem Set 7 Question 2
# To create a short link of a youtube video from an embedded youtube link in html src code

# Importing re to search for the link
import re

# Defining main to get input and pass it to parse() then print the final answer
def main():
    print(parse(input("HTML: ")))

# Function to parse the link with the shortened version of link
def parse(s):
    # Checking if toParse is true and uses re.search() function to find the link and return it using parenthesis
    if toParse := re.search(r".+(?:https?://)?(?:www\.)?youtube\.com/embed/(\w+).+", s, flags = re.MULTILINE):
        return f"https://youtu.be/{toParse.group(1)}"

# To execute to program
if __name__ == "__main__":
    main()