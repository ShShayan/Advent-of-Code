from copy import deepcopy
import numpy as np

def straightLineCheck(pointList):
    x = 0
    straightList = deepcopy(pointList)
    for i in range(len(straightList)):
        if straightList[i - x][0][0] != straightList[i - x][1][0] and straightList[i - x][0][1] != straightList[i - x][1][1]:
            straightList.pop(i - x)
            x += 1
    return straightList

def naghsheKesh(naghshe, lineList):
    for i in range(len(lineList)):
        if lineList[i][0][0] == lineList[i][1][0]:
            a = lineList[i][0][1]
            b = lineList[i][1][1]
            if a > b:
                c = a
                a = b
                b = c
            for n in range(b - a + 1):
                naghshe[lineList[i][0][0]][a + n] += 1
        elif lineList[i][0][1] == lineList[i][1][1]:
            a = lineList[i][0][0]
            b = lineList[i][1][0]
            if a > b:
                c = a
                a = b
                b = c
            for n in range(b - a + 1):
                naghshe[a + n][lineList[i][0][1]] += 1
        else:
            xA = lineList[i][0][0]
            xB = lineList[i][1][0]
            yA = lineList[i][0][1]
            yB = lineList[i][1][1]
            if xA > xB:
                c = xA
                d = yA
                xA = xB
                yA = yB
                xB = c
                yB = d
            for n in range(xB - xA + 1):
                if yB > yA:
                    naghshe[xA + n][yA + n] += 1
                else:
                    naghshe[xA + n][yA - n] += 1
    return naghshe

def danger(naghshe):
    danger = 0
    for i in range(len(naghshe)):
        for n in range(len(naghshe[i])):
            if naghshe[i][n] > 1:
                danger += 1
    return danger

f = open('data/puzzle5.txt', 'r')
data = [s.split(' -> ') for s in f.read().split('\n')]
for i in range(len(data)):
    data[i] = [s.split(',') for s in data[i]]
    for n in range(len(data[i])):
        data[i][n] = [int(s) for s in data[i][n]]
lineList = straightLineCheck(data)
naghshe = np.zeros((1000,1000), dtype = int)
naghshe = naghsheKesh(naghshe, lineList)
answer1 = danger(naghshe)

naghshe2 = np.zeros((1000,1000), dtype = int)
naghshe2 = naghsheKesh(naghshe2, data)
answer2 = danger(naghshe2)

print(answer1, answer2)
