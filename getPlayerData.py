import requests
import json
import csv
import time

with open('match_id.csv', 'r') as csvfile, open('playerData.json', 'w') as file:
    reader = csv.reader(csvfile, delimiter=',')
    matchCount = 0
    errorCount = 0
    for i in reader:
        payload = i[0]
        url = "https://api.opendota.com/api/matches/" + payload
        try:
            requestMatchData = requests.get(url).json()
        except json.decoder.JSONDecodeError:
            print("JSON decode error.")
            errorCount +=1
            continue
        print("Writing match", i,"to file.")
        count = 1
        try:
            for j in requestMatchData["players"]:
                print("Player",count)
                json.dump(j, file)
                count+=1
        except KeyError:
            print("Key error.")
            errorCount+=1
            continue
        time.sleep(1.1)
        matchCount +=1
    print(matchCount,"matches written to file.")
    print(errorCount,"errors.")
