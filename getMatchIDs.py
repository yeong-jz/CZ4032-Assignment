import json
import requests
import pandas as pd
import csv
import time

with open('match_id.csv', 'a', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(1,500):
        r = requests.get("https://api.opendota.com/api/publicMatches")
        data = r.json()
        for j in data:
            try:
                writer.writerow([str(j["match_id"])])
            except TypeError:
                continue
        print("Record", i, "added.")
        time.sleep(1.1)




        
