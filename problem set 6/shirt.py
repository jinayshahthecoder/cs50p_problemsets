# Problem Set 6 Question 4
# To overlay an image over another and output that overlay as a file

# Importing sys, os, Image() and ImageOps() to use to get arguments, find if input is a file and edit images
import sys, os
from PIL import Image, ImageOps

# Opening an image and getting its width and height
shirt = Image.open("shirt.png")
size = shirt.size

# Defining main() to exit program or call overlay() depending on input
def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if os.path.isfile(sys.argv[1]):
        if sys.argv[1].split(".")[1] == sys.argv[2].split(".")[1]:
                overlay(sys.argv[1], sys.argv[2])
        else:
                sys.exit("Input and output have different extensions")
    else:
        sys.exit("Invalid input")

# Function to overlay the shirt over the image as per the question
def overlay(before, after):
    # Checking if file exists
    try:
        # Opening the before image as answer
        with Image.open(before) as answer:
            # Cropping as per shirt size
            answer = ImageOps.fit(answer, size)
            # Overlaying shirt over mask
            answer.paste(shirt, shirt)
            # Saving the answer
            answer.save(after)
    # Handling FileNotFoundError as requested by question
    except FileNotFoundError:
        sys.exit("File Not Found")

# To execute the program
if __name__ == "__main__":
    main()