# convert json to csv
import json
import csv

with open("Data/finalPlayerData.json", "r") as file, open("Data/finalPlayerData.csv", "w",  newline='') as newfile:
    count = 0
    errorCount = 0
    writer = csv.writer(newfile)
    for i in file:
        try:
            i = i.rstrip()
            data = json.loads(i)
            for i in data.keys():
                if i == "rank_tier":
                    data[i] = data[i]//10
            if count < 1:
                writer.writerow(data.keys())
                writer.writerow(data.values())
                count+=1
            else:
                writer.writerow(data.values())
        except json.decoder.JSONDecodeError:
            print("JSON decode error.")
            errorCount+=1
        
