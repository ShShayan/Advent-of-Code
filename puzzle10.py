# puzzle 10!

from copy import deepcopy

def corruptionChecker(data):
    for i in range(len(data)):
        if data[i] == ']' or data[i] == ')' or data[i] == '}' or data[i] == '>':
            n = 0
            for n in range(i):
                if (data[i] == ')' and data[i-n-1] == '(') or (data[i] == '}' and data[i-n-1] == '{') or (data[i] == ']' and data[i-n-1] == '[') or (data[i] == '>' and data[i-n-1] == '<'):
                    data[i] = 0
                    data[i-n-1] = 0
                elif data[i-n-1] != 0:
                    if data[i] == ')':
                        return 3
                    elif data[i] == ']':
                        return 57
                    elif data[i] == '}':
                        return 1197
                    elif data[i] == '>':
                        return 25137
        else:
            continue

def main():
    data = open('data\puzzle10.txt', 'r').read().split('\n')
    data = [list(s) for s in data]
    totalSyntaxError = []
    for s in data:
        totalSyntaxError.append(corruptionChecker(s))
    answerP1 = 0
    for s in totalSyntaxError:
        if s is not None:
            answerP1 += s
    print('part 1 answer: ', answerP1)

    dataP2 = deepcopy(data)
    n = 0
    for i in range(len(totalSyntaxError)):
        if totalSyntaxError[i] != None:
            dataP2.pop(i - n)
            n += 1
    for s in dataP2:
        m = 0
        for i in range(len(s)):
            if s[i - m] == 0:
                s.pop(i - m)
                m += 1
    scores = []
    for s in dataP2:
        score = 0
        for i in range(len(s)):
            x = len(s)
            score *= 5
            if s[x-i-1] == '(':
                score += 1
            elif s[x-i-1] == '[':
                score += 2
            elif s[x-i-1] == '{':
                score += 3
            elif s[x-i-1] == '<':
                score += 4
        scores.append(score)
    scores.sort()
    print('Part 2 answer is: ', scores[int(len(scores) / 2)])

main()