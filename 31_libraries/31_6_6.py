import re
from pprint import pprint

import requests

req = requests.get("http://www.columbia.edu/~fdc/sample.html")
pattern = r">.*</h3>"
result = re.findall(pattern, req.text)
for i, j in enumerate(result):
    result[i] = j[1:-5]
pprint(result)
