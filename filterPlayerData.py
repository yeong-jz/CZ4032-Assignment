import json
import re

# purpose is to filter labelled and unlabelled player data
def filterLabelledData():
    with open('Data/playerData.json', 'r') as file, open('Data/labelPlayerData.json', 'w') as newfile:
        count = 0
        errorCount = 0
        buyback_count = 0
        teamfight_count = 0
        lane_efficiency_pct = 0
        rune_pickups = 0
        hero_healing = 0
        obs_placed = 0
        sen_placed = 0
        stuns = 0
        tower_damage = 0
        for i in file:
            try:
                playerData = json.loads(i)
                if playerData["rank_tier"] is not None:
                    json.dump(playerData, newfile)
                    newfile.write('\n')
                    count+=1
                    print(count, "records added.")
                if playerData["buyback_count"] != 0:
                    buyback_count +=1
                if playerData["teamfight_participation"] != 0:
                    teamfight_count+=1
                if playerData["lane_efficiency_pct"] != 0:
                    lane_efficiency_pct+=1
                if playerData["rune_pickups"] != 0:
                    rune_pickups+=1
                if playerData["hero_healing"] != 0:
                    hero_healing+=1
                if playerData["obs_placed"] != 0:
                    obs_placed+=1
                if playerData["sen_placed"] != 0:
                    sen_placed+=1
                if playerData["stuns"] != 0:
                    stuns+=1
                if playerData["tower_damage"] != 0:
                    tower_damage+=1
            except (json.decoder.JSONDecodeError,KeyError):
                errorCount+=1
        print(count)
        print(errorCount)
        print("buyback count:",buyback_count)
        print("teamfight_count:",teamfight_count)
        print("lane_efficiency_pct count:",lane_efficiency_pct)
        print("rune_pickups:",rune_pickups)
        print("hero_healing:",hero_healing)
        print("obs_placed:", obs_placed)
        print("sen_placed:", sen_placed)
        print("stuns:", stuns)
        print("tower_damage:",tower_damage)


filterLabelledData()
##with open('finalPlayerData.json', 'r') as file, open('labelPlayerData.json', 'a') as newfile:
##    for i in file:
##        try:
##            playerData = json.loads(i)
##            if playerData["rank_tier"] is not None:
##                json.dump(playerData, newfile)
##                newfile.write('\n')
##                count+=1
##                print(count, "records added.") 
##        except (json.decoder.JSONDecodeError,KeyError):
##            errorCount+=1
