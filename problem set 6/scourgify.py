# Problem Set 6 Question 3
# To convert a given file's full names into first and last names and add them to another file

# Importing sys and csv to use to get arguments and edit .csv files
import sys, csv

# Defining main() to exit program or call readAndWrite() depending on input
def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        readAndWrite()
    else:
        sys.exit("Not a CSV file")

# Function to read file1 and print output into file2 (both in .csv)
def readAndWrite():
    # Checking if file exists
    try:
        # Reading file1 ad "before" file
        before = open(sys.argv[1])
        # Writing file2 as "after" file
        with open(sys.argv[2], "w", newline="") as after:
            # Using DictReader() to read file as a dictionary
            reader = csv.DictReader(before)
            # Using DictWriter() to write file as a dictionary by defining fieldnames and headers
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            # Adding rows to writer by use of loop
            for row in reader:
                fName, lName = row["name"].split(", ")
                writer.writerow({"first": fName.strip(),"last": lName.strip(),"house": row["house"].strip()})
    # Handling FileNotFoundError as requested by question
    except FileNotFoundError:
        print("Could not read,", sys.argv[1])

# To execute the program
if __name__ == "__main__":
    main()