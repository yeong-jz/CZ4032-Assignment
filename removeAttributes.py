import json
import csv
import pandas as pd
##with open('Data/finalPlayerData.json', 'r') as file, open('Data/temp.json', 'w') as newfile:
##    count = 0
##    errorCount = 0
##    buyback_count = 0
##    teamfight_count = 0
##    lane_efficiency_pct = 0
##    rune_pickups = 0
##    hero_healing = 0
##    obs_placed = 0
##    sen_placed = 0
##    stuns = 0
##    tower_damage = 0
##    for i in file:
##        try:
##            playerData = json.loads(i)
##            if playerData["rank_tier"] is not None:
##                count+=1
##            if "buyback_count" in playerData:
##                del playerData["buyback_count"]
##            if "denies" in playerData:
##                del playerData["denies"]
##            if "lane_efficiency_pct" in playerData:
##                del playerData["lane_efficiency_pct"]
##            if "win" in playerData:
##                del playerData["win"]
##            if playerData["teamfight_participation"] != 0:
##                teamfight_count+=1
##            if playerData["rune_pickups"] != 0:
##                rune_pickups+=1
##            if playerData["hero_healing"] != 0:
##                hero_healing+=1
##            if playerData["obs_placed"] != 0:
##                obs_placed+=1
##            if playerData["sen_placed"] != 0:
##                sen_placed+=1
##            if playerData["stuns"] != 0:
##                stuns+=1
##            if playerData["tower_damage"] != 0:
##                tower_damage+=1
##            json.dump(playerData, newfile)
##            print("Record written.")
##            newfile.write("\n")
##        except (json.decoder.JSONDecodeError,KeyError):
##            errorCount+=1
##    print(count)
##    print(errorCount)
##    print("buyback count:",buyback_count)
##    print("teamfight_count:",teamfight_count)
##    print("lane_efficiency_pct count:",lane_efficiency_pct)
##    print("rune_pickups:",rune_pickups)
##    print("hero_healing:",hero_healing)
##    print("obs_placed:", obs_placed)
##    print("sen_placed:", sen_placed)
##    print("stuns:", stuns)
##    print("tower_damage:",tower_damage)

data = pd.read_csv("Data/finalPlayerData2.csv")
column = data["gold_efficiency"]
count = 0
minimum = 0
maximum = 0
for i in column:
    if count == 0:
        minimum = i
        maximum = i
        count+=1
    elif count > 0:
        if i > maximum:
            maximum = i
        if i < minimum:
            minimum = i
print(minimum)
print(maximum)

column = (column-minimum)/(maximum-minimum).column

