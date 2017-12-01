# loeb kõik andmed
def loadAllData(fn):
    all_data = []
    with open(fn) as f:
        next(f) # esimest rida ei loe
        for line in f:
            all_data.append([line.strip()])
    return all_data

print(loadAllData("andmed.txt"))
