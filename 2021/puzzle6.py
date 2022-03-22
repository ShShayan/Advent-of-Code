# # puzzle 6 with lists!
# # this works fine for part 1 with only 80 days
# # but for part to it took 34 minutes to reach a memory error!
# # not recommended

# f = open('data/puzzle6.txt', 'r')
# data = [int(s) for s in f.read().split(',')]
# numberOfDays = 80
# for i in range(numberOfDays):
#     for n in range(len(data)):
#         if data[n] == 0:
#             data.append(8)
#             data[n] = 6
#         else:
#             data[n] -= 1

# len(data)

#######

# not my answer sadly!

from collections import Counter

def part1(fishes):
    for day in range(80):
        for idx, fish in enumerate(fishes):
            if fish == 0:
                fishes[idx] = 7
                fishes.append(9)
        fishes = [fish - 1 for fish in fishes]
    return len(fishes)

def part2(fishes):
    timers = Counter({timer: 0 for timer in range(10)})
    fishes = Counter(fishes)
    fishes.update(timers)
    
    for day in range(256):
        fishes[7] += fishes.get(0, 0)
        fishes[9] += fishes.get(0, 0)
        fishes = {fish: fishes.get(fish + 1, 0) for fish in fishes}
        
    return sum(fishes.values())

def main():
    with open("data/puzzle6.txt") as f:
        fishes = f.read().strip().split(',')
        fishes = list(map(int, fishes))
        
    print(f"Part 1 Answer: {part1(fishes)}")
    print(f"Part 2 Answer: {part2(fishes)}")

if __name__ == "__main__":
    main()