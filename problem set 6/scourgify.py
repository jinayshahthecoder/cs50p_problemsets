import sys, csv

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv"):
        readAndWrite()
    else:
        sys.exit("Not a CSV file")

def readAndWrite():
    try:
        before = open(sys.argv[1])
        with open(sys.argv[2], "w", newline="") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for row in reader:
                fName, lName = row["name"].split(", ")
                writer.writerow({"first": fName.strip(),"last": lName.strip(),"house": row["house"].strip()})
    except FileNotFoundError:
        print("Could not read,", sys.argv[1])

# To execute the program
if __name__ == "__main__":
    main()