# Import the request and sys moudule
import requests
import sys

# get value from command line
if len(sys.argv) == 2:
    try:
        value = float(sys.argv[1])
    except:
         print("Missing command line argument")
         sys.exit(1)
else:
    print("Missing command line argument")
    sys.exit(1)
# Get the current price of the bitcoin with the value of command line
try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    response = r.json()
    bitcoin = response['bpi']['USD']['rate_float']
    total_amount = bitcoin * value
    print(f"${total_amount:,.4f}")
except requests.RequestException:
    print("RequestException")