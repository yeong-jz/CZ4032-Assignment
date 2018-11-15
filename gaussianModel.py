# perform machine learning on dataset
# purpose is to identify which skill bracket a player is from based on their stats

import numpy as np
import pandas as pd
import time
import pickle
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.externals import joblib
from sklearn import preprocessing
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

# initialise medals list
medals = ["Null", "Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]

# read the data into a dataframe
data = pd.read_csv("Data/finalPlayerData.csv")
X_train, X_test = train_test_split(data, test_size=0.2, random_state=int(time.time()))

gnb = GaussianNB()

used_features =[]

# fill the features list with the values
for i in data.head(1):
    if i != "rank_tier":
     used_features.append(i)

# train the model
gnb.fit(
    X_train[used_features].values,
    X_train["rank_tier"]
)

gaussian_pred = gnb.predict(X_test[used_features])

# save model for use next time
print("Saving trained model.")
joblib.dump(gnb, 'gaussianClassifier.joblib')
pickle.dump(gnb, open("gaussianClassifier.sav", 'wb'))

# print sample predictions
for i in range(0,10):
    sample = data.sample(n=1)
    sample_pred = gnb.predict(sample.drop("rank_tier", axis=1))
    print("Sample Prediction", i+1)
    print("Predicted medal bracket:", medals[int(sample_pred[0])])
    print("Actual medal bracket:", medals[int(sample["rank_tier"].values[0])])
    print("Euclidean distance:", abs(int(sample["rank_tier"].values[0])-int(sample_pred[0])))
    print("\n")

# print results of the training
print("Using {} features.".format(len(used_features)))
print("Number of training points used :", len(X_train))
print("Number of test points used :", len(X_test))
print("Gaussian model")
print("Number of mislabeled points out of a total {} points : {}, performance {:05.2f}%"
      .format(
          X_test.shape[0],
          (X_test["rank_tier"] != gaussian_pred).sum(),
          100*(1-(X_test["rank_tier"] != gaussian_pred).sum()/X_test.shape[0])
))
print("Average Euclidean distance :", abs(X_test["rank_tier"] - gaussian_pred).sum()/X_test.shape[0])
print("Overall score :", (100*(1-(X_test["rank_tier"] != gaussian_pred).sum()/X_test.shape[0])*(1/(abs(X_test["rank_tier"] - gaussian_pred).sum()/X_test.shape[0]))))

# display a heatmap
sns.heatmap(confusion_matrix(X_test["rank_tier"], gaussian_pred), xticklabels=medals[1:], yticklabels=medals[1:], annot=True, fmt="d")
plt.xlabel("Actual")
plt.ylabel("Predicted")
plt.title("Gaussian Naive Bayes")
plt.tight_layout()
plt.show()
