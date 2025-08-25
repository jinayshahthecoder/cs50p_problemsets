# Problem Set 0 Question 5
# To receive the bill amount payable by the customer in dollars and percentage
#  of tip payable on the bill and outputing the answer by use of functions

# Defining the main function
def main():

    # Get user input of the dollars and percentages
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    # Calculating the tip
    tip = dollars * percent

    # Print the answer
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    # To convert input to float type
    d = d.replace("$", "")
    d = float(d)

    # Return the variable
    return d


def percent_to_float(p):

    # To convert input to float type and then to percent required
    p = p.replace("%", "")
    p = float(p)
    p = p/100

    # Return the variable
    return p

# To execute the program
main()