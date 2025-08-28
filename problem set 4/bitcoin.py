# Problem Set 4 Question 6
# To fetch and display the price of 'n' BTC inputted as a command line arguement by user

# Importing necessary files
import requests
import sys

# Checking if user has inputted the number of bitcoins' price that they want to be shown
if len(sys.argv) == 2:
    # Checking for any errors with the input or API fetching
    try:
        sys.argv[1] = float(sys.argv[1])
        result = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd")
    # Handling errors by exiting the program as asked
    except ValueError:
        sys.exit("Command-line argument is not a number.")
    except requests.RequestException:
        sys.exit("Error occured while fetching results, please try again later.")
    # Decodes the json() file received and the prints the answer requested
    file = result.json()
    oneBTC = float(file["bitcoin"]["usd"])
    price = oneBTC * sys.argv[1]
    print(f"${price:,.4f}")
# Else, exits the program
else:
    sys.exit("Missing command-line argument.")
