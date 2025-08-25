# Problem Set 1 Question 5
# To implement a program to tell the user what type of meal has to be eaten at a given time
# in a country where it is customary to eat at a given time

def main():

    # Get user input string as time and then use a function convert() to make it into a decimal number
    time = input("What time is it? ")
    time = convert(time)

    # Use if conditional to print out the answer
    if 7 <= time < 8:
        print("Breakfast Time")
    elif 12 <= time < 13:
        print("Lunch Time")
    elif 18 <= time < 19:
        print("Dinner Time")
    else:
        print("Fatty")


def convert(time):

    # To convert string into a decimal number
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    minute = minute / 60
    return hour + minute


main()