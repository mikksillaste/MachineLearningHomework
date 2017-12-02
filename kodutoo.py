# loeb kõik andmed
def loadAllData(fn):
    all_data = []
    with open(fn) as f:
        next(f)  # esimest rida ei loe
        # all_data = [[int(s) for s in l.split()] for l in open('andmed.txt').readlines()]
        for line in f:
            all_data.append([line.strip()])
    return all_data


test = loadAllData("andmed.txt")[0]
str1 = ''.join(test)
mylist = [int(x) for x in str1.split(',')]

print(mylist)
