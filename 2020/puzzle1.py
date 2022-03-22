def main():
    data =  [int(x) for x in open('Data/puzzle1.txt').read().split('\n')]
    for i in data:
        if 2020 - i in data:
            break
    print('part 1 answer is: ', i * (2020 - i))
    for m in data:
        for n in data:
            if 2020 - m - n in data:
                break
        if 2020 - m - n in data:
            break
    print('part 2 answer is: ', m * n * (2020 - m - n))

main()