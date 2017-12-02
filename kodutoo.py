# loeb kõik andmed
def loadAllData(fn):
    all_data = []
    with open(fn) as f:
        next(f)  # esimest rida ei loe
       # all_data = [[int(s) for s in l.split()] for l in open('andmed.txt').readlines()]
        for line in f:
            all_data.append([line.strip()])
            # all_data = list(map(int, all_data))
    return all_data


print(loadAllData("andmed.txt"))