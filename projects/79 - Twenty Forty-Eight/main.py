import random
import sys

def new_game():
    board = [[0] * 4 for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        r, c = random.choice(empty_cells)
        board[r][c] = 2 if random.random() < 0.9 else 4

def print_board(board):
    print('\n' + '-' * 29)
    for row in board:
        print('|', end='')
        for cell in row:
            if cell == 0:
                print(f"{' ':^6}", end='|')
            else:
                print(f"{cell:^6}", end='|')
        print('\n' + '-' * 29)

def merge(row):
    new_row = [i for i in row if i != 0]
    for i in range(len(new_row) - 1):
        if new_row[i] == new_row[i+1]:
            new_row[i] *= 2
            new_row[i+1] = 0
    new_row = [i for i in new_row if i != 0]
    return new_row + [0] * (4 - len(new_row))

def transpose(board):
    return [list(row) for row in zip(*board)]

def reverse(board):
    return [row[::-1] for row in board]

def move_left(board):
    new_board = []
    for row in board:
        new_board.append(merge(row))
    return new_board

def move_right(board):
    return reverse(move_left(reverse(board)))

def move_up(board):
    return transpose(move_left(transpose(board)))

def move_down(board):
    return transpose(move_right(transpose(board)))

def get_game_state(board):
    for r in range(4):
        for c in range(4):
            if board[r][c] == 2048:
                return 'WON'
    for r in range(4):
        for c in range(4):
            if board[r][c] == 0:
                return 'PLAYING'
    for r in range(4):
        for c in range(3):
            if board[r][c] == board[r][c+1]:
                return 'PLAYING'
    for r in range(3):
        for c in range(4):
            if board[r][c] == board[r+1][c]:
                return 'PLAYING'
    return 'LOST'

def main():
    board = new_game()
    print("Welcome to 2048!")
    print_board(board)

    while True:
        move = input("Enter move (WASD or Q to quit): ").upper().strip()
        if move == 'Q':
            print("Thanks for playing!")
            break
        
        if move not in ('W', 'A', 'S', 'D'):
            print("Invalid move.")
            continue
            
        new_board = []
        if move == 'W':
            new_board = move_up(board)
        elif move == 'S':
            new_board = move_down(board)
        elif move == 'A':
            new_board = move_left(board)
        elif move == 'D':
            new_board = move_right(board)
            
        if new_board != board:
            board = new_board
            add_new_tile(board)
            print_board(board)
            
            state = get_game_state(board)
            if state == 'WON':
                print("You reached 2048! You Win!")
                break
            elif state == 'LOST':
                print("Game Over! No more moves.")
                break
        else:
            print("No moves possible in that direction!")

if __name__ == "__main__":
    main()
