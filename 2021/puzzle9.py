# Puzzle 9!

def checkSurrounding(data, i, n):
    if i == 0 and n != 0 and n != 99:
        if data[i][n] < data[i][n-1] and data[i][n] < data[i][n+1] and data[i][n] < data[i+1][n]:
            return 1
        else:
            return 0
    elif i == 99 and n != 0 and n != 99:
        if data[i][n] < data[i][n-1] and data[i][n] < data[i][n+1] and data[i][n] < data[i-1][n]:
            return 1
        else:
            return 0
    elif n == 0 and i != 0 and i != 99:
        if data[i][n] < data[i-1][n] and data[i][n] < data[i+1][n] and data[i][n] < data[i][n+1]:
            return 1
        else:
            return 0
    elif n == 99 and n != 0 and i != 99:
        if data[i][n] < data[i-1][n] and data[i][n] < data[i+1][n] and data[i][n] < data[i][n-1]:
            return 1
        else:
            return 0
    elif i == 0 and n == 0:
        if data[i][n] < data[1][0] and data[i][n] < data[0][1]:
            return 1
        else:
            return 0
    elif i == 0 and n == 99:
        if data[i][n] < data[i+1][n] and data[i][n] < data[i][n-1]:
            return 1
        else:
            return 0
    elif i == 99 and n == 0:
        if data[i][n] < data[i-1][n] and data[i][n] < data[i][n+1]:
            return 1
        else:
            return 0
    elif i == 99 and n == 99:
        if data[i][n] < data[i-1][n] and data[i][n] < data[i][n-1]:
            return 1
        else:
            return 0
    else:
        if data[i][n] < data[i-1][n] and data[i][n] < data[i+1][n] and data[i][n] < data[i][n+1] and data[i][n] < data[i][n-1]:
            return 1
        else:
            return 0

def basinSizer(data, i, n, basinPoints):
    basinPoints.append([i,n])
    b = [i+1,n]
    c = [i-1,n]
    d = [i,n+1]
    e = [i,n-1]
    a = [b,c,d,e]
    for s in a:
        if s[0] > 99 or s[0] == -1 or s[1] > 99 or s[1] == -1:
            continue
        elif data[s[0]][s[1]] == '9':
            continue
        elif [s[0],s[1]] in basinPoints:
            continue
        else:
            basinSizer(data, s[0], s[1], basinPoints)

def main():
    data = open('data\puzzle9.txt', 'r').read().split('\n')
    data = [list(s) for s in data]
    allBasins = []
    risk = 0
    for i in range(100):
        for n in range(100):
            basins = []
            if checkSurrounding(data, i, n) == 1:
                risk += checkSurrounding(data, i, n) * (int(data[i][n]) + 1)
                basinSizer(data, i, n, basins)
                allBasins.append(basins)
                
    print('part 1 answer: ', risk)
    basinSizes = [len(s) for s in allBasins]
    basinSizes.sort()
    x = len(basinSizes)
    answer = basinSizes[x - 1] * basinSizes[x - 2] * basinSizes[x - 3]
    print('part 2 answer: ', answer)

main()