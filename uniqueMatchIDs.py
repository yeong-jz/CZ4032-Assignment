import csv

def uniqueMatchIDs():
    # purpose is to check the match_id csv for unique match ids
    with open("match_id.csv", "r") as file:
        reader = csv.reader(file, delimiter=',')
        uniqueIDs = []
        count = 0
        for i in reader:
            if i not in uniqueIDs:
                uniqueIDs.append(i)
        for i in uniqueIDs:
            count+=1
        # display number of unique match ids
        print("No. of new unique match IDs:", count)
        
    print("Checking unique match id file.")

    # we want to make sure that the new match ids pulled from the api dont overlap
    # with what we already have
    with open("unique_match_id.csv", "r", newline='') as newfile:
        reader2 = csv.reader(newfile, delimiter=',')
        uniqueIDs2 = []
        count2 = 0
        for i in reader2:
            if i not in uniqueIDs2:
                uniqueIDs2.append(i)
        for i in uniqueIDs2:
            count2+=1
        print("No. of existing unique match IDs :", count2)
        print("New total :",count+count2)

    # after checking then we write to file
    with open("unique_match_id.csv", "a", newline='') as newfile:
        writer = csv.writer(newfile, delimiter=',')
        for i in uniqueIDs:
            if i not in uniqueIDs2:
                writer.writerow(i)