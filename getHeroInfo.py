# get dota heroes information

import json
import requests

with open("Data/heroInfo.json", "w") as file:
    r = requests.get("https://api.opendota.com/api/heroes")
    data = r.json()
    json.dump(data,file)
