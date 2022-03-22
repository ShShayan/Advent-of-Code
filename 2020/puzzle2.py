def correctOrNot(po, pa):
    a = int(po.split(' ')[0].split('-')[0])
    b = int(po.split(' ')[0].split('-')[1])
    c = po.split(' ')[1]
    if pa.count(c) >= a and pa.count(c) <= b:
        return 1
    else:    
        return 0

def correctOrNot2(po, pa):
    a = int(po.split(' ')[0].split('-')[0])
    b = int(po.split(' ')[0].split('-')[1])
    c = po.split(' ')[1]
    if b > len(pa):
        return 0
    if (pa[a-1] is c and pa[b-1] is not c) or (pa[a-1] is not c and pa[b-1] is c):
        return 1
    else:    
        return 0

def main():
    data = open('Data/puzzle2.txt').read().split('\n')
    policies = [x.split(': ')[0] for x in data]
    passwords = [x.split(': ')[1] for x in data]
    answer1 = 0
    for i in range(len(policies)):
        answer1 += correctOrNot(policies[i], passwords[i])
    print('Part 1 answer is: ', answer1)
    answer2 = 0
    for i in range(len(policies)):
        answer2 += correctOrNot2(policies[i], passwords[i])
    print('Part 2 answer is: ', answer2)

main()