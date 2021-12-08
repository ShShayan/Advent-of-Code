import pandas as pd
from copy import deepcopy

def tedadShomar(data, jaygah):
    temp = deepcopy(data)
    tedad = len(temp)
    tedadyek = 0
    for n in range(tedad):
        tedadyek = tedadyek + int(temp.iloc[n][0][jaygah])
    return tedadyek

def tedadShomarlist(data, jaygah):
    temp = deepcopy(data)
    tedad = len(temp)
    tedadyek = 0
    for n in range(tedad):
        tedadyek = tedadyek + int(temp[n][jaygah])
    return tedadyek

def gammaYab(data):
    ragham = len(data.iloc[0][0])
    tedad = len(data)
    gamma = 0
    for i in range(ragham):
        temp = 0
        for n in range(tedad):
            temp = temp + int(data.iloc[n][0][i])
        if temp > 500:
            gamma = gamma + 10 ** (ragham - i - 1)
    return gamma

def epsilonYab(gamma, ragham):
    adad = 0
    for i in range(ragham):
        adad += 10 ** i
    epsilon = adad - gamma
    return epsilon

def fuel(x, y):
    x = int(str(x),2)
    y = int(str(y),2)
    return x * y


def main():
    f = open('puzzle3.txt', 'r')
    data = f.read().split('\n')
    data = pd.DataFrame(data)

    gamma = gammaYab(data)
    epsilon = epsilonYab(gamma, 12)

    javab1 = fuel(epsilon, gamma)

    listOxy = []
    listCo = []

    tedad = len(data)
    tedadyek = tedadShomar(data, 0)
    if tedadyek >= 500:
        for n in range(tedad):
            if data.iloc[n][0][0] == '1':
                listOxy.append(data.iloc[n][0])
            else: listCo.append(data.iloc[n][0])
    elif tedadyek < 500:
        for n in range(tedad):
            if data.iloc[n][0][0] == '0':
                listOxy.append(data.iloc[n][0])
            else: listCo.append(data.iloc[n][0])

    for i in range(11):
        tedadyek = tedadShomarlist(listOxy, i + 1)
        if len(listOxy) == 1:
            break
        x = 0
        if tedadyek >= len(listOxy) / 2:
            for n in range(len(listOxy)):
                if listOxy[n - x][i + 1] == '0':
                    listOxy.pop(n - x)
                    x += 1
        else:
            for n in range(len(listOxy)):
                if listOxy[n - x][i + 1] == '1':
                    listOxy.pop(n - x)
                    x += 1

    for i in range(11):
        tedadyek = tedadShomarlist(listCo, i + 1)
        if len(listCo) == 1:
            break
        x = 0
        if tedadyek < len(listCo) / 2:
            for n in range(len(listCo)):
                if listCo[n - x][i + 1] == '0':
                    listCo.pop(n - x)
                    x += 1
        else:
            for n in range(len(listCo)):
                if listCo[n - x][i + 1] == '1':
                    listCo.pop(n - x)
                    x += 1

    javab2 = int(listOxy[0],2) * int(listCo[0],2)
    print(f'javab 1 is: {javab1}\njavab 2 is: {javab2}')

main()