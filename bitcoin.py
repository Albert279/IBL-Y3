import requests
import json
import sys
import ast

if len(sys.argv) != 2:
    sys.exit('Missing command-line argument')

try:
    qty = ast.literal_eval(sys.argv[1])
except Exception as err:
    sys.exit('Command-line argument is not a number')

response = requests
o = response.json()
#print(o)
rate = o["bpi"]["USD"]["rate"]

print(qty*float(rate.replace(",","")))