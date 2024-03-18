import requests
import sys
import json
#Check if command line arguments have been provided
if(sys.argv.__len__() < 2):
    sys.exit("Missing Command Line Arguments")
else:
    try:
        userInput = float(sys.argv[1])
        
        #print(f"{output:,.4f}")
    except ValueError:
        sys.exit("Command Line Argument provided is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    if(response.status_code == requests.codes.ok):
        jsonResponse = response.json()
        dollar_rate = jsonResponse['bpi']['USD']['rate_float']
        output = dollar_rate * userInput
        print(f"${output:,.4f}")
    else:
        sys.exit(f"Something went wrong, {response.status_code}")
    
except requests.RequestException :
    print("There was an ambiguous exception that occurred while handling your request")