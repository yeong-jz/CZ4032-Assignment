import requests
import json
import csv
import time

def getPlayerData():
    with open('unique_match_id.csv', 'r') as csvfile, open('playerData.json', 'w') as file:
        reader = csv.reader(csvfile, delimiter=',')
        matchCount = 1
        errorCount = 0
        for i in reader:
            # payload is the match id read from match id csv
            payload = i[0]
            url = "https://api.opendota.com/api/matches/" + payload
            try:
                # attempt to call their api with the match id
                requestMatchData = requests.get(url).json()
            except json.decoder.JSONDecodeError:
                # dont want the script to stop running because of the below error so
                # wrapped it in a try except
                print("JSON decode error.")
                errorCount +=1
                continue
            print("Writing match", i,"to file.")
            print(matchCount,"records written.")
            try:
                # sometimes might encounter multiple instances of this data
                for j in requestMatchData["players"]:
                    # write to json file the player data from the match
                    json.dump(j, file)
                    file.write('\n')
            except KeyError:
                # same as above, wrapped in try except to avoid stopping the script
                print("Key error.")
                errorCount+=1
                continue
            matchCount +=1
            time.sleep(1.1)
            
        print(errorCount,"errors.")

getPlayerData()
