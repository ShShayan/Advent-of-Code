from matplotlib import pyplot

# for visualization
def plotData(data,function):
    fuelCosts = []
    for i in range(1200):
        fuelCosts.append(function(data,i))

    pyplot.plot(fuelCosts)

def fuelCost(positions, goal):
    fuel = 0
    for i in range(len(positions)):
        fuel += abs(positions[i] - goal)
    return fuel

def fuelCost2(positions, goal):
    fuel = 0
    for i in range(len(positions)):
        fasele = abs(positions[i] - goal)
        fuelYeki = (fasele + 1) * fasele / 2
        fuel += fuelYeki
    return fuel

def optimizer(data, initialGoal, function):
    # decide on direction
    a = function(data, initialGoal)
    b = function(data, initialGoal - 1)
    c = function(data, initialGoal + 1)
    if a > b:
        for i in range(initialGoal - 1):
            b = function(data, initialGoal - 1 - i)
            d = function(data, initialGoal - 2 - i)
            if d > b:
                return b
    else:
        for i in range(initialGoal - 1):
            c = function(data, initialGoal + 1 + i)
            d = function(data, initialGoal + 2 + i)
            if d > c:
                return c

def main():
    f = open('data/puzzle7.txt', 'r')
    data = [int(s) for s in f.read().split(',')]
    initialGoal1 = int(sum(data) / len(data))
    initialGoal2 = 400
    # plotData(data, fuelCost)
    # plotData(data, fuelCost2)
    fuel1 = optimizer(data, initialGoal1, fuelCost)
    fuel2 = optimizer(data, initialGoal2, fuelCost2)
    print(f'Part 1 answer is: {fuel1}\nPart 2 answer is: {fuel2}')



main()