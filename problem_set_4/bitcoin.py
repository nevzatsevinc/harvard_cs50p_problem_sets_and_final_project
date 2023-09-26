"""
Problem Set 4 - Bitcoin Price Index
https://cs50.harvard.edu/python/2022/psets/4/bitcoin/
"""

import sys
import requests

# Check command-line argument
if len(sys.argv) != 2:
    sys.exit("Missing command-line argument ")

# Convert the command-line argument to a float
try: 
    value = float(sys.argv[1])
except ValueError:
    print("Command-line argument is not a number")
# Make a request to api
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
except requests.RequestException:
    sys.exit("Unable to get url")

# Get the current price of Bitcoin
data = response.json()
per_bitcoin = float(data['bpi']['USD']['rate'].replace(',', ''))

# Calculate and print
cost = value * per_bitcoin
print(f"{cost:,.4f}")