# perform machine learning on dataset
# purpose is to identify which skill bracket a player is from based on their stats

import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


# initialise medals list
medals = ["Null", "Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]

data = pd.read_csv("Data/finalPlayerData.csv")

X_train, X_test = train_test_split(data, test_size=0.2, random_state=int(time.time()))

gnb = GaussianNB()

used_features =[]

# fill the features list with the values
for i in data.head(1):
    used_features.append(i)

gnb.fit(
    X_train[used_features].values,
    X_train["rank_tier"]
)

gaussian_pred = gnb.predict(X_test[used_features])

# print sample predictions
for i in range(0,10):
    sample = data.sample(n=1)
    sample_pred = gnb.predict(sample)
    print("Sample Prediction", i+1)
    print("Predicted medal bracket:", medals[int(sample_pred[0])])
    print("Actual medal bracket:", medals[int(sample["rank_tier"].values[0])])
    print("\n")

print("Number of training points used :", len(X_train))
print("Number of test points used :", len(X_test))
print("Gaussian model")
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
      .format(
          X_test.shape[0],
          (X_test["rank_tier"] != gaussian_pred).sum(),
          100*(1-(X_test["rank_tier"] != gaussian_pred).sum()/X_test.shape[0])
))
