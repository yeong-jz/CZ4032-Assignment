import json
import re

# purpose is to filter labelled and unlabelled player data
with open('playerData.json', 'r') as file, open('labelPlayerData.json', 'a') as newfile:
    count = 0
    errorCount = 0
    try:
        for i in file:
            playerData = json.loads(i)
            if playerData["rank_tier"] is not None:
                json.dump(playerData, newfile)
                newfile.write('\n')
                count+=1
                print(count, "records added.")
    except json.decoder.JSONDecodeError:
        errorCount+=1
    print(count)
    print(errorCount)
