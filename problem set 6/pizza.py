# Problem Set 6 Question 2
# To make a tabular menu for a restaurant using given .csv files

# Importing sys to get cmd-line argument, tabulate() to make the tabular menu, csv to read .csv files
import sys
from tabulate import tabulate
import csv

# Defining main() to exit program or call printMenu() depending on input
def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv"):
        printMenu()
    else:
        sys.exit("Not a CSV file")

# Function to print the .csv file in a tabular format by the use of loops and file i/o
def printMenu():
    # Defining the table to be printed
    table = []
    # Checking if file exists
    try:
        # Reading the given file by treating name as "file"
        with open(sys.argv[1]) as file:
            # Using DictReader() to read file as a dictionary
            reader = csv.DictReader(file)
            # Making a loop to append each dictionary row to table
            for row in reader:
                table.append(row)
            # Printing the menu
            print(tabulate(table, tablefmt= "grid", headers="keys"))
    # Handling FileNotFoundError as requested by question
    except FileNotFoundError:
        print("Menu not found")

# To execute the program
if __name__ == "__main__":
    main()