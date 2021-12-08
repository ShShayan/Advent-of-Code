def boardYab(boards):
    n = 0
    board = []
    tedadBoards = int((len(boards) + 1)/6)
    for i in range(tedadBoards):
        board.append([boards[5 * i + n],boards[5*i +1+n], boards[5 * i + 2+n],
                        boards[5*i+3+n],boards[5*i+4+n]])
        n += 1
    return board

def stringToNumber(boards):
    tedadBoards = len(boards)
    tedadRadif = len(boards[0])
    for i in range(tedadBoards):
        for n in range(tedadRadif):
            boards[i][n] = boards[i][n].split(' ')
            tedadChar = len(boards[i][n])
            if tedadChar > 5:
                x = 0
                for m in range(tedadChar):
                    if boards[i][n][m - x] == '':
                        boards[i][n].pop(m - x)
                        x += 1
            boards[i][n] = [int(s) for s in boards[i][n]]
    return boards

def checkBoards(boards, number):
    for i in range(len(boards)):
        for n in range(5):
            for m in range(5):
                if boards[i][n][m] == number:
                   boards[i][n][m] = -1 

def checkForWinner(boards):
    # check every row
    for i in range(len(boards)):
        for n in range(len(boards[i])):
            if boards[i][n][0] == -1 and boards[i][n][1] == -1 and boards[i][n][2] == -1 and boards[i][n][3] == -1 and boards[i][n][4] == -1:
                print('We have a winner!!!')
                return i
        for m in range(5):
            if boards[i][0][m] == -1 and boards[i][1][m] == -1 and boards[i][2][m] == -1 and boards[i][3][m] == -1 and boards[i][4][m] == -1:
                print('We have a winner!!!')
                return i
    return -1

def bingo(boards, numbers):
    winnerID = -1
    for i in range(len(numbers)):
        checkBoards(boards, numbers[i])
        print(numbers[i])
        if i > 4:
            winnerID = checkForWinner(boards)
            if winnerID != -1:
                return winnerID, i

def calcScore(board, number):
    sum = 0
    for i in range(5):
        for n in range(5):
            if board[i] != -1:
                sum += board[i][n]
    score = sum * number
    return score

def main():
    f = open('data/puzzle4.txt', 'r')
    data = f.read().split('\n')
    numbers = data[0]
    numbers = [int(s) for s in numbers.split(',')]
    boards = data[2:]
    boards = stringToNumber(boardYab(boards))
    print(len(boards))
    winnerID, numberID = bingo(boards, numbers)
    score = calcScore(boards[winnerID], numbers[numberID])
    print('This is score of the winner: ', score)

main()