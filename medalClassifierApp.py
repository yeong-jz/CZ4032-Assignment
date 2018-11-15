# A simple app that utilises the model trained to classify a player's game data
# enter user data to be predicted by classifier

from sklearn.externals import joblib
from sklearn.naive_bayes import GaussianNB
import pickle
import requests
import json
import pandas as pd
from collections import OrderedDict


# initialise medal list
medals = ["Null", "Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]
heroInfo = json.load(open("Data/heroInfo.json", "r"))

# get the classifier
try:
    print("Loading classifier...")
    mc = joblib.load(open("randomForestClassifier.joblib", "rb"))
    print("Classifier loaded.")
    matchID = input("Enter your match id :")
    userID = input("Enter your user id :")
    print("Getting match info...")
    url = "https://api.opendota.com/api/matches/" + matchID
    try:
        requestMatchData = requests.get(url).json()
        # find player info
        players = requestMatchData["players"]
        found = False
        playerAttributesKeys = ["kills", "assists", "deaths", "total_gold", "gold_per_min", "last_hits_per_min", "hero_heal_damage", "wards_placed",
             "tower_damage", "xp_per_min", "rank_tier"]
        playerAttributeValues = []
        for i in players:
            try:
                if userID.lower() in i["personaname"].lower():
                    print("User found. Extracting data...")
                    hero_id = i["hero_id"]
                    try:
                        lane_role = i["lane_role"]
                    except KeyError:
                        lane_role = "Not found."
                    kills = i["kills"]
                    assists = i["assists"]
                    deaths = i["deaths"]
                    total_gold = i["total_gold"]
                    gold_per_min = i["gold_per_min"]
                    last_hits_per_min = i["last_hits"]/i["duration"]
                    hero_damage = i["hero_damage"]
                    hero_healing = i["hero_healing"]
                    hero_heal_damage = hero_damage + hero_healing
                    obs_placed = i["obs_placed"]
                    sen_placed = i["sen_placed"]
                    if obs_placed is None:
                        obs_placed = 0
                    if sen_placed is None:
                        sen_placed = 0
                    wards_placed = obs_placed + sen_placed
                    tower_damage = i["tower_damage"]
                    xp_per_min = i["xp_per_min"]
                    rank_tier = i["rank_tier"]
                    playerAttributeValues.extend((kills, assists, deaths, total_gold, gold_per_min, last_hits_per_min, hero_heal_damage, wards_placed,
             tower_damage, xp_per_min, rank_tier))
                    for index, data in enumerate(playerAttributeValues):
                        if data is None:
                            playerAttributeValues[index] = 0
                        else:
                            # standardising all values to a 2dp format
                            playerAttributeValues[index] = float("{0:.2f}".format(data))
                    found = True
                    playerAttributes = OrderedDict(zip(playerAttributesKeys, playerAttributeValues))
                    print("Your stats are :")
                    print("Kills :", kills)
                    print("Assists :", assists)
                    print("Deaths :", deaths)
                    print("Total gold :", total_gold)
                    print("Gold per minute :", gold_per_min)
                    print("Last hits per minute : {0:.3f}".format(last_hits_per_min))
                    print("Hero damage :", hero_damage)
                    print("Hero healing :", hero_healing)
                    print("Observers placed :", obs_placed)
                    print("Sentries placed :", sen_placed)
                    print("Tower damage :", tower_damage)
                    print("Exp per minute :", xp_per_min)
                    if rank_tier != 0:
                        print("Rank :", medals[int(rank_tier//10)], int(rank_tier%10))
                    else:
                        print("Rank : Unknown")
                    for i in heroInfo:
                        if i["id"] == hero_id:
                            print("Hero played :", i["localized_name"])
                    print("Lane role :", lane_role)
                    playerDataFrame = pd.DataFrame.from_records([playerAttributes])
                    estimatedBracket = mc.predict(playerDataFrame.drop("rank_tier", axis=1))
                    print("Estimated performance in game:", medals[int(estimatedBracket)])
                    break
            except KeyError:
                print("Player name not found. Trying again...")
        if found == False:
            print("Username was not found. Please expose public match data in your Dota client.")  
    except json.decoder.JSONDecodeError:
        print("JSON decode error.")
    
except FileNotFoundError:
    print("File was not found. Please make sure file is in the right directory.")

