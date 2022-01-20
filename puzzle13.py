# Puzzle 13!
import numpy as np

def folder(Direction, Position, dotList):
    if Direction == 'x':
        newpage = dotList[:Position,:]
        folded = dotList[Position + 1:,:]
        for i in range(folded.shape[0]):
            for n in range(folded.shape[1]):
              if folded[i,n] == 1:
                  newpage[Position-i-1, n] = 1 
    if Direction == 'y':
        newpage = dotList[:,:Position]
        folded = dotList[:,Position + 1:]
        for i in range(folded.shape[0]):
            for n in range(folded.shape[1]):
              if folded[i,n] == 1:
                  newpage[i, Position-n-1] = 1 
    return newpage

def pageMaker(dots):
    max1 = dots[:,0].max()
    max2 = dots[:,1].max()
    page = np.zeros((max1 + 1,max2 + 1))
    for i in dots:
        page[i[0],i[1]] = 1
    return page

data = open('data\puzzle13.txt', 'r').read().split('\n\n')
dots = [x.split(',') for x in data[0].split('\n')]
for i in dots:
    i[0] = int(i[0])
    i[1] = int(i[1])
dots = np.array(dots)
page = pageMaker(dots)
folds = [x.split('=') for x in data[1].split('\n')]
for i in folds:
    i[0] = i[0].strip('fold along ')
    i[1] = int(i[1])
for i in folds:
    page = folder(i[0], i[1], page)
page.T

# page.T is the answer but reading it as is, is really hard :))
# I suggest copying the answer in notepad and something