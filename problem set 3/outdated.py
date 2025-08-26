# Problem Set 3 Question 4
# To convert user inputted mm-dd-yyyy or m d, yyyy date format to ISO 8601 standard date format

# Creating a list of months to check for later
writtenMonths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]

# Making a while loop to continuously ask the user for the date
while True:
    # Checking for correct date or value errors
    try:
        date = input("Date: ")
        # Checking if user inputs format 1 or 2 then printing correct answer if so
        if "/" in date:
            month, day, year = map(int, date.split("/"))
            if month <= 12 and day <= 31:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                continue
        elif "," in date:
            monthday, year = date.split(",")
            month, day = monthday.split(" ")
            if month in writtenMonths:
                month = writtenMonths.index(month) + 1
                day = int(day)
                year = int(year)
                if day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
        # Else, prompting user again for input
        else:
            pass
    # Checking for ValueError or if user wants to end program then continuing as per the needs
    except ValueError:
        pass
    except EOFError:
        break
