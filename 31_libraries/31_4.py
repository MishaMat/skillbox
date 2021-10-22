from pprint import pprint

import requests
import json

my_req = requests.get("https://swapi.dev/api/people/10/")
res = json.loads(my_req.text)
res['name'] = "misha matviykiv"

with open("json.json", 'w') as file:
    json.dump(res, file)

hw = requests.get(res['homeworld'])
res = json.loads(hw.text)
pprint(res)