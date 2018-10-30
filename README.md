# CZ4032-Assignment
Assignment for CZ4032
## Getting started
1. Have Python 3.6 installed

## Instructions
1. Run getMatchIDs.py to generate a list of match ids.

2. Run uniqueMatchIDs.py to check if the generated list of match ids are unique or already exist in the file.

3. Run getPlayerData.py to call the OpenDota API with the list of match ids to get player information from those matches.

4. Run filterLabelledData.py to remove unlabeled records as they are not useful for our training purposes.

5. Run filterPlayerAttributes.py to select only those attributes that are wanted and write them to another json file for processing.

6. Run csv_generator.py to generate a csv file from the json file that was produced.

7. Run either gaussianModel.py or randomForestModel.py to train on the csv file that was produced.

8. Run medalClassifierApp.py to use the model on actual match data.

## File Descriptions
### csv_generator.py
Generates a CSV file from a json file for easier processing with pandas.

### filterLabelledData.py
Checks records in playerData.json for labels. If the record has a label, it is written to labelPlayerData.json

### filterPlayerAttributes.py
After deciding which attributes we wish to use, this script is run to select only those attributes and write the selected attributes as a json record to finalPlayerData.json.

### gaussianClassifier.joblib
The joblib file that the Gaussian model is saved to after training.

### gaussianClassifier.sav
The pickle file that the Gaussian model is saved to after training.

### gaussianModel.py
Machine learning file that implements the Gaussian Naive Bayes model. Creates a joblib and pickle file after it has trained on the data.

### getHeroInfo.py
This script calls the OpenDota API for the list of heroes and their information and stores the information for future retrieval in heroInfo.json.

### getMatchIDs.py
This script calls the OpenDota API for 100 random match IDs which are then stored in match_id.csv.

### getPlayerData.py
This script reads match IDs from unique_match_id.csv and calls the OpenDota API for the match information and stores it in playerData.json.

### medalClassifierApp.py
An application that loads the saved trained model and uses it to estimate the performance of a player given a specific match ID and username.

### randomForestClassifier.joblib
The joblib file that the Random Forest model is saved to after training.

### randomForestClassifier.sav
The pickle file that the Random Forest model is saved to after training.

### randomForestModel.py
Machine learning file that implements the Random Forest model. Creates a joblib and pickle file after it has trained on the data.

### removeAttributes.py
This script was used to remove attributes from already created json files. It is now deprecated.

### uniqueMatchIDs.py
This script is used to check if the match ids in match_id.csv were already retrieved before and if they were not, it would store the match id in unique_match_id.csv.
