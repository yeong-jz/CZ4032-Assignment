# purpose is to get each json object to only have the attributes desired

# list of attributes we want :
## kda :kill+assists/deaths+1
## Networth/Gold_per_min: how effective you are at getting gold
## Camps_stacked
## Denies : allied heroes (e.g own creeps)
## Hero damage
## Hero healing
## Last hits
## Obs_placed : "observer_uses": 3
## Rune_pickups (total runes picked up) 
## Sen_placed: "sentry_uses": 9,
## Stuns
## Tower Damage 
## Teamfight_participation
## XP_per_min
## "win": 0,
## "buyback_count": 1,
## "lane_efficiency_pct": 25,
## "rank_tier": Tens place indicates rank, ones place indicates stars.
## ranks : herald, guardian, crusader, archon, legend, ancient, divine, immortal
## ranks have different grades from 1 to 5
## eg archon 4 would be 44 in the rank tier

import json
from collections import OrderedDict

# initialise a list of keys which comes from the attributes that we decided on previously
attr_keys = ["kills", "assists", "deaths", "total_gold", "gold_per_min", "last_hits_per_min","hero_heal_damage", "wards_placed",
             "tower_damage", "xp_per_min", "rank_tier"]

# open the files 
with open("Data/labelPlayerData.json", "r") as file, open("Data/finalPlayerData.json", "w") as newfile:
    count = 0
    for i in file:
        playerData = json.loads(i)
        # initialise a list of values to be paired with the keys we have initialised earlier
        attr_values = []
        # get the values from each player's data 
        kills = playerData["kills"]
        assists = playerData["assists"]
        deaths = playerData["deaths"]
        total_gold = playerData["total_gold"]
        gold_per_min = playerData["gold_per_min"]
        last_hits_per_min = playerData["last_hits"]/playerData["duration"]
        hero_heal_damage = playerData["hero_damage"] + playerData["hero_healing"]
        if playerData["obs_placed"] is None:
            obs_placed = 0
        else:
            obs_placed = playerData["obs_placed"]
        if playerData["sen_placed"] is None:
            sen_placed = 0
        else:
            sen_placed = playerData["sen_placed"]
        wards_placed = obs_placed + sen_placed
        tower_damage = playerData["tower_damage"]
        xp_per_min = playerData["xp_per_min"]
        rank_tier = playerData["rank_tier"]
        # add the values that we have gotten to the list of values initialised earlier
        attr_values.extend((kills, assists, deaths, total_gold, gold_per_min, last_hits_per_min, hero_heal_damage, wards_placed,
             tower_damage, xp_per_min, rank_tier))
        
        # to eliminate the existence of null values, we replace them with a zero
        for index, data in enumerate(attr_values):
            if data is None:
                attr_values[index] = 0
            else:
                # standardising all values to a 2dp format
                attr_values[index] = float("{0:.2f}".format(data))
        # create the dictionary which is our json object to be written to the file
        attr_dict = OrderedDict(zip(attr_keys, attr_values))
        json.dump(attr_dict, newfile)
        newfile.write('\n')
        count+=1
        print(count, "records written to file.")
