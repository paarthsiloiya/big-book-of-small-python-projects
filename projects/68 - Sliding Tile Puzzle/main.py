import random, sys, os

BLANK = '  '

def main():
    print('Sliding Tile Puzzle')
    print('Use WASD keys to move tiles.')
    input('Press Enter to begin...')

    gameBoard = getNewPuzzle()

    while True:
        displayBoard(gameBoard)
        playerMove = askForPlayerMove(gameBoard)
        makeMove(gameBoard, playerMove)

        if gameBoard == getNewBoard():
            print('You won!')
            sys.exit()

def getNewBoard():
    return [['1 ', '5 ', '9 ', '13'], ['2 ', '6 ', '10', '14'],
            ['3 ', '7 ', '11', '15'], ['4 ', '8 ', '12', BLANK]]

def displayBoard(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sliding Tile Puzzle')
    
    print('┌────┬────┬────┬────┐')
    for y in range(4):
        print('│', end='')
        for x in range(4):
            print(' ' + board[x][y] + ' │', end='')
        print()
        if y < 3:
            print('├────┼────┼────┼────┤')
    print('└────┴────┴────┴────┘')

def findBlankSpace(board):
    for x in range(4):
        for y in range(4):
            if board[x][y] == BLANK:
                return (x, y)

def askForPlayerMove(board):
    blankx, blanky = findBlankSpace(board)
    w = 'W' if blanky != 3 else ' '
    a = 'A' if blankx != 3 else ' '
    s = 'S' if blanky != 0 else ' '
    d = 'D' if blankx != 0 else ' '

    while True:
        print(f'                          ({w})')
        print(f'Enter WASD (or QUIT): ({a}) ({s}) ({d})')

        response = input('> ').upper()
        if response == 'QUIT':
            sys.exit()
        if response in (w + a + s + d).replace(' ', ''):
            return response

def makeMove(board, move):
    bx, by = findBlankSpace(board)
    if move == 'W':
        board[bx][by], board[bx][by+1] = board[bx][by+1], board[bx][by]
    elif move == 'A':
        board[bx][by], board[bx+1][by] = board[bx+1][by], board[bx][by]
    elif move == 'S':
        board[bx][by], board[bx][by-1] = board[bx][by-1], board[bx][by]
    elif move == 'D':
        board[bx][by], board[bx-1][by] = board[bx-1][by], board[bx][by]

def makeRandomMove(board):
    blankx, blanky = findBlankSpace(board)
    validMoves = []
    if blanky != 3: validMoves.append('W')
    if blankx != 3: validMoves.append('A')
    if blanky != 0: validMoves.append('S')
    if blankx != 0: validMoves.append('D')
    makeMove(board, random.choice(validMoves))

def getNewPuzzle(moves=200):
    board = getNewBoard()
    for i in range(moves):
        makeRandomMove(board)
    return board

if __name__ == '__main__':
    main()
