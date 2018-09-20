import json
import re

# purpose is to filter labelled and unlabelled player data
with open('finalPlayerData.json', 'r') as file:#, open('labelPlayerData.json', 'a') as newfile:
    count = 0
    errorCount = 0
    buyback_count = 0
    teamfight_count = 0
    lane_efficiency_pct = 0
    
    for i in file:
        try:
            playerData = json.loads(i)
            if playerData["rank_tier"] is not None:
##                json.dump(playerData, newfile)
##                newfile.write('\n')
                count+=1
##                print(count, "records added.")
            if playerData["buyback_count"] == 0:
                buyback_count +=1
            if playerData["teamfight_participation"] == 0:
                teamfight_count+=1
            if playerData["lane_efficiency_pct"] == 0:
                lane_efficiency_pct+=1
        except (json.decoder.JSONDecodeError,KeyError):
            errorCount+=1
    print(count)
    print(errorCount)
    print("buyback count:",buyback_count)
    print("teamfight_count:",teamfight_count)
    print("lane_efficiency_pct count:",lane_efficiency_pct)
    
