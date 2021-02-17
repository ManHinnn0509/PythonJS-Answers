import os
import csv
from sklearn import svm

os.system("cls")

true = True
false = False

trainCSV_FileName = "train.csv"
testCSV_FileName = "test.csv"

ageSum = 0
pplSum = 0

def floatAge(age):
    if (age == "" or age == "male" or age == "female"):
        return -1
    else:
        global ageSum
        ageSum += float(age)

        global pplSum
        pplSum += 1

        return float(age)

def floatFare(fare):
    return 0 if fare == "" else float(fare)

def intSex(sex):
    return 0 if sex == "male" else 1

def intEmbarked(embarked):
    if (embarked == "C"):
        return 1
    elif (embarked == "Q"):
        return 2
    elif (embarked == "S"):
        return 3
    else:       # Other case (Maybe empty case :/)
        return 4

def getData(csvFileName, isPrediction):
    features = []
    labels = []
    survivedIndex = 0 if (isPrediction == true) else 1

    with open(csvFileName) as f:
        csvFile = csv.reader(f)
        headers = next(csvFile)
        
        # Format:
        # ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
        for row in csvFile:
            # print(row)

            if (isPrediction == false):
                survived = int(row[1])
                labels.append(survived)

            pClass = float(row[survivedIndex + 1])
            sex = intSex(row[survivedIndex + 3])
            age = floatAge(row[survivedIndex + 4])
            sibSp = float(row[survivedIndex + 5])
            parch = float(row[survivedIndex + 6])
            fare = floatFare(row[survivedIndex + 8])
            embarker = intEmbarked(row[survivedIndex + 10])
            features.append([pClass, sex, age, sibSp, parch, fare, embarker])
        
        averageAge = ageSum / pplSum
        for f in features:
            if (f[2] == -1):
                f[2] = averageAge
    
    return features, labels
    # features as X and labels as Y

def printPrediction(features, prediction):
    lenF = len(features)
    lenP = len(prediction)
    
    if (lenF != lenP):
        return
    
    for x in range (0, lenF):
        f = features[x]
        p = prediction[x]

        print(str(f) + " | " + str(p) + "")

# End of functions etc

print("--- Start of Program ---")

x, y = getData(trainCSV_FileName, false)

clf = svm.SVC()
clf.fit(x, y)

# Reset the previous data
ageSum = 0
pplSum = 0

# predictY will be empty (?)
predictX, predictY = getData(testCSV_FileName, true)

prediction = clf.predict(predictX)
printPrediction(predictX, prediction)

print("--- End of Program ---")