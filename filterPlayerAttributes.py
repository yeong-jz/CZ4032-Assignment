# purpose is to get each json object to only have the attributes desired

import json
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
## "lose": 1,
## "buyback_count": 1,
## "lane_efficiency_pct": 25,
## "rank_tier": 63,

# read each player's num of kills, deaths and assists from json file
attr_keys = ["kda", "gold_efficiency", "camps_stacked", "last_hits", "denies", "hero_damage", "hero_healing",
            "obs_placed", "sen_placed", "stuns", "tower_damage", "rune_pickups",
             "teamfight_participation", "xp_per_min", "win", "buyback_count", "lane_efficiency_pct", "rank_tier"]

with open("labelPlayerData.json", "r") as file, open("finalPlayerData.json", "w") as newfile:
    count = 0
    for i in file:
        playerData = json.loads(i)
        attr_values = []
        kda = (playerData["kills"] + playerData["assists"])/(playerData["deaths"] + 1)
        gold_efficiency = playerData["total_gold"]/playerData["gold_per_min"]
        camps_stacked = playerData["camps_stacked"]
        last_hits = playerData["last_hits"]
        denies = playerData["denies"]
        hero_damage = playerData["hero_damage"]
        hero_healing = playerData["hero_healing"]
        obs_placed = playerData["obs_placed"]
        sen_placed = playerData["sen_placed"]
        stuns = playerData["stuns"]
        tower_damage = playerData["tower_damage"]
        rune_pickups = playerData["rune_pickups"]
        teamfight_participation = playerData["teamfight_participation"]
        xp_per_min = playerData["xp_per_min"]
        win = playerData["win"]
        try:
            buyback_count = playerData["buyback_count"]
        except KeyError:
            buyback_count = 0
            continue
        try:
            lane_efficiency_pct = playerData["lane_efficiency_pct"]
        except KeyError:
            lane_efficiency_pct = 0
            continue
        rank_tier = playerData["rank_tier"]
        attr_values.extend((kda, gold_efficiency, camps_stacked, last_hits, denies, hero_damage, hero_healing, obs_placed,
              sen_placed, stuns, tower_damage, rune_pickups, teamfight_participation, xp_per_min, win, buyback_count,
                           lane_efficiency_pct, rank_tier))
        for index, data in enumerate(attr_values):
            if data is None:
                attr_values[index] = 0
            else:
                attr_values[index] = float("{0:.2f}".format(data))
        attr_dict = dict(zip(attr_keys, attr_values))
        json.dump(attr_dict, newfile)
        newfile.write('\n')
        count+=1
        print(count, "records written to file.")
