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

# get the classifier
try:
    print("Loading classifier...")
    mc = pickle.load(open("medalClassifier.sav", "rb"))
##    mc = joblib.load('medalClassifier.joblib')
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
        playerAttributesKeys = ["kda", "gold_efficiency", "camps_stacked", "last_hits", "hero_damage", "hero_healing",
            "obs_placed", "sen_placed", "stuns", "tower_damage", "rune_pickups",
             "teamfight_participation", "xp_per_min", "rank_tier"]
        playerAttributeValues = []
        for i in players:
            try:
                if userID.lower() == i["personaname"].lower():
                    print("User found. Extracting data...")
                    kda = (i["kills"] + i["assists"])/(i["deaths"] + 1)
                    gold_efficiency = i["total_gold"]/i["gold_per_min"]
                    camps_stacked = i["camps_stacked"]
                    last_hits = i["last_hits"]
                    hero_damage = i["hero_damage"]
                    hero_healing = i["hero_healing"]
                    obs_placed = i["obs_placed"]
                    sen_placed = i["sen_placed"]
                    stuns = i["stuns"]
                    tower_damage = i["tower_damage"]
                    rune_pickups = i["rune_pickups"]
                    teamfight_participation = i["teamfight_participation"]
                    xp_per_min = i["xp_per_min"]
                    rank_tier = i["rank_tier"]
                    playerAttributeValues.extend((kda, gold_efficiency, camps_stacked, last_hits, hero_damage, hero_healing, obs_placed,
                          sen_placed, stuns, tower_damage, rune_pickups, teamfight_participation, xp_per_min, rank_tier))
                    for index, data in enumerate(playerAttributeValues):
                        if data is None:
                            playerAttributeValues[index] = 0
                        else:
                            # standardising all values to a 2dp format
                            playerAttributeValues[index] = float("{0:.2f}".format(data))
                    found = True
                    playerAttributes = OrderedDict(zip(playerAttributesKeys, playerAttributeValues))
                    print("Your stats are :")
                    for key,value in playerAttributes.items():
                        print(key,":", value)
                    playerDataFrame = pd.DataFrame.from_records([playerAttributes])
                    estimatedBracket = mc.predict(playerDataFrame.drop("rank_tier", axis=1))
                    print("Estimated medal bracket:", medals[int(estimatedBracket)])
                    break
            except KeyError:
                print("Player name not found. Trying again...")
        if found == False:
            print("Username was not found. Please expose public match data in your Dota client.")  
    except json.decoder.JSONDecodeError:
        print("JSON decode error.")
    
except FileNotFoundError:
    print("File was not found. Please make sure file is in the right directory.")

