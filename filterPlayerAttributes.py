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

# initialise a list of keys which comes from the attributes that we decided on previously
attr_keys = ["kda", "gold_efficiency", "camps_stacked", "last_hits", "hero_damage", "hero_healing",
            "obs_placed", "sen_placed", "stuns", "tower_damage", "rune_pickups",
             "teamfight_participation", "xp_per_min", "rank_tier"]

# open the files 
with open("labelPlayerData.json", "r") as file, open("finalPlayerData.json", "a") as newfile:
    count = 0
    for i in file:
        playerData = json.loads(i)
        # initialise a list of values to be paired with the keys we have initialised earlier
        attr_values = []
        # get the values from each player's data 
        kda = (playerData["kills"] + playerData["assists"])/(playerData["deaths"] + 1)
        gold_efficiency = playerData["total_gold"]/playerData["gold_per_min"]
        camps_stacked = playerData["camps_stacked"]
        last_hits = playerData["last_hits"]
        hero_damage = playerData["hero_damage"]
        hero_healing = playerData["hero_healing"]
        obs_placed = playerData["obs_placed"]
        sen_placed = playerData["sen_placed"]
        stuns = playerData["stuns"]
        tower_damage = playerData["tower_damage"]
        rune_pickups = playerData["rune_pickups"]
        teamfight_participation = playerData["teamfight_participation"]
        xp_per_min = playerData["xp_per_min"]
        rank_tier = playerData["rank_tier"]
        # add the values that we have gotten to the list of values initialised earlier
        attr_values.extend((kda, gold_efficiency, camps_stacked, last_hits, hero_damage, hero_healing, obs_placed,
              sen_placed, stuns, tower_damage, rune_pickups, teamfight_participation, xp_per_min, rank_tier))
        
        # to eliminate the existence of null values, we replace them with a zero
        for index, data in enumerate(attr_values):
            if data is None:
                attr_values[index] = 0
            else:
                # standardising all values to a 2dp format
                attr_values[index] = float("{0:.2f}".format(data))
        # create the dictionary which is our json object to be written to the file
        attr_dict = dict(zip(attr_keys, attr_values))
        json.dump(attr_dict, newfile)
        newfile.write('\n')
        count+=1
        print(count, "records written to file.")
