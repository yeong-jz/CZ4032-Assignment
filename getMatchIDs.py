import json
import requests
import pandas as pd
import csv
import time
import uniqueMatchIDs as umd

# open match id csv file in write mode
with open('match_id.csv', 'w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for i in range(0,100):
        # call opendota's public match api(gives 100 randomly sampled match ids)
        r = requests.get("https://api.opendota.com/api/publicMatches")
        data = r.json()
        for j in data:
            try:
                # write the match id into the csv file
                writer.writerow([str(j["match_id"])])
            except TypeError:
                continue
        print("Record", i, "added.")
        time.sleep(1.1)

umd.uniqueMatchIDs()


        
