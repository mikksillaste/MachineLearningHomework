from sklearn import tree
from sklearn.metrics import accuracy_score


# loeb kõik andmed
def loadAllData(fn):
    all_data = []
    with open(fn) as f:
        next(f)  # esimest rida ei loe
        for line in f:
            # Enne int'iks ja siis listi listis
            all_data.append([int(x) for x in line.split(',')])
    return all_data


# poolita list
def split_list(a_list):
    half = len(a_list) // 2
    return a_list[:half], a_list[half:]


# andmetests ainult data osa ilma resuldita, esimesed 9
def getOnlyDataFromAllData(fulllist):
    onlyData = []
    for i in fulllist:
        onlyData.append(i[0:9])
    return onlyData


# andmetest ainult target osa
def getOnlyTargetFromAllData(fulllist):
    targets = []
    for i in fulllist:
        targets.append(i[9])
    return targets


# kõik andmed
allData = loadAllData("andmed.txt")
# poolita andmed
trainAllData, testAllData = split_list(allData)
# andmedest ainult data osa
trainData = getOnlyDataFromAllData(trainAllData)
testData = getOnlyDataFromAllData(testAllData)
# andmedest ainult target osa
trainDataTarget = getOnlyTargetFromAllData(trainAllData)
testDataTarget = getOnlyTargetFromAllData(testAllData)
# otsustuspuu klassifitseerimine
my_classifier = tree.DecisionTreeClassifier()
my_classifier.fit(trainData, trainDataTarget)
prediction = my_classifier.predict(testData)

print(accuracy_score(testDataTarget, prediction))
