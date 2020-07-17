import requests
import json
from pprint import pprint

# address = "http://api.postcodes.io/postcodes/LS18 5LG"
# req_response = requests.get(address)

# print(req_response.status_code)
# print(req_response.headers)
# pprint(req_response.json())

# result = req_response.json()['result']
# print(f"Eastings: {result['eastings']}; Northings: {result['northings']}")

# print(f"NUTS Code: {result['codes']['nuts']}")

dict_body = {'postcodes': ["B7 4BB", "OX49 5NU", "M32 OJG", "NE30 1DP"]}
json_body = json.dumps(dict_body)
headers = {'Content-Type': 'application/json'}

address = "https://api.postcodes.io/postcodes/"
req_response = requests.post(address, headers=headers, data=json_body)
# pprint(req_response.json()['result'])

# result = req_response.json()['result']

for postcode in req_response.json()['result']:
    result = postcode['result']
    print(f"Postcode: {result['postcode']}; Eastings: {result['eastings']}; Northings: {result['northings']}; NUTS Code: {result['codes']['nuts']}")


    