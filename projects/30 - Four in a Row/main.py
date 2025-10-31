import sys
import os

BOARD_WIDTH = 7
BOARD_HEIGHT = 6
EMPTY_TILE = "○"
PLAYER1_TILE = "\x1b[91m●\x1b[0m"
PLAYER2_TILE = "\x1b[94m●\x1b[0m"

TOP_LEFT = "┌"
TOP_RIGHT = "┐"
BOTTOM_LEFT = "└"
BOTTOM_RIGHT = "┘"
HORIZONTAL = "─"
VERTICAL = "│"
TOP_JUNCTION = "┬"
BOTTOM_JUNCTION = "┴"
LEFT_JUNCTION = "├"
RIGHT_JUNCTION = "┤"
CROSS_JUNCTION = "┼"


def main():
    print("Welcome to Four in a Row (Connect 4)!")
    print("The objective is to connect four of your tiles in a row.")
    print("You can connect horizontally, vertically, or diagonally.")
    print()

    player1_name = input("Enter name for Player 1: ")
    player2_name = input("Enter name for Player 2: ")

    board = get_new_board()
    current_player = 1

    while True:
        display_board(board)

        if current_player == 1:
            player_name = player1_name
            player_tile = PLAYER1_TILE
        else:
            player_name = player2_name
            player_tile = PLAYER2_TILE

        print(f"{player_name}'s turn ({player_tile})")
        column = get_player_move(board)

        if column is None:
            print("Thanks for playing!")
            sys.exit()

        drop_tile(board, column, current_player)

        if is_winner(board, current_player):
            display_board(board)
            print(f"🎉 Congratulations {player_name}! You won! 🎉")
            break

        if is_board_full(board):
            display_board(board)
            print("It's a tie! The board is full.")
            break

        current_player = 3 - current_player


def get_new_board():
    board = []
    for row in range(BOARD_HEIGHT):
        board.append([EMPTY_TILE] * BOARD_WIDTH)
    return board


def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    print()

    print("   ", end="")
    for col in range(BOARD_WIDTH):
        print(f" {col + 1}  ", end="")
    print()

    print("  " + TOP_LEFT, end="")
    for col in range(BOARD_WIDTH):
        print(HORIZONTAL * 3, end="")
        if col < BOARD_WIDTH - 1:
            print(TOP_JUNCTION, end="")
    print(TOP_RIGHT)

    for row in range(BOARD_HEIGHT):
        print("  " + VERTICAL, end="")
        for col in range(BOARD_WIDTH):
            print(f" {board[row][col]} ", end="")
            print(VERTICAL, end="")
        print()

        if row < BOARD_HEIGHT - 1:
            print("  " + LEFT_JUNCTION, end="")
            for col in range(BOARD_WIDTH):
                print(HORIZONTAL * 3, end="")
                if col < BOARD_WIDTH - 1:
                    print(CROSS_JUNCTION, end="")
            print(RIGHT_JUNCTION)

    print("  " + BOTTOM_LEFT, end="")
    for col in range(BOARD_WIDTH):
        print(HORIZONTAL * 3, end="")
        if col < BOARD_WIDTH - 1:
            print(BOTTOM_JUNCTION, end="")
    print(BOTTOM_RIGHT)
    print()


def get_player_move(board):
    while True:
        print(f"Choose a column (1-{BOARD_WIDTH}) or 'quit' to exit: ", end="")
        choice = input().strip().lower()

        if choice == 'quit' or choice == 'q':
            return None

        try:
            column = int(choice) - 1
        except ValueError:
            print("Please enter a valid number or 'quit'.")
            continue

        if column < 0 or column >= BOARD_WIDTH:
            print(f"Please enter a number between 1 and {BOARD_WIDTH}.")
            continue

        if board[0][column] != EMPTY_TILE:
            print("That column is full. Choose another column.")
            continue

        return column


def drop_tile(board, column, player):
    for row in range(BOARD_HEIGHT - 1, -1, -1):
        if board[row][column] == EMPTY_TILE:
            if player == 1:
                board[row][column] = PLAYER1_TILE
            else:
                board[row][column] = PLAYER2_TILE
            return


def is_winner(board, player):
    if player == 1:
        tile = PLAYER1_TILE
    else:
        tile = PLAYER2_TILE

    for row in range(BOARD_HEIGHT):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == tile and
                board[row][col + 1] == tile and
                board[row][col + 2] == tile and
                board[row][col + 3] == tile):
                return True

    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH):
            if (board[row][col] == tile and
                board[row + 1][col] == tile and
                board[row + 2][col] == tile and
                board[row + 3][col] == tile):
                return True

    for row in range(BOARD_HEIGHT - 3):
        for col in range(BOARD_WIDTH - 3):
            if (board[row][col] == tile and
                board[row + 1][col + 1] == tile and
                board[row + 2][col + 2] == tile and
                board[row + 3][col + 3] == tile):
                return True

    for row in range(BOARD_HEIGHT - 3):
        for col in range(3, BOARD_WIDTH):
            if (board[row][col] == tile and
                board[row + 1][col - 1] == tile and
                board[row + 2][col - 2] == tile and
                board[row + 3][col - 3] == tile):
                return True

    return False


def is_board_full(board):
    for col in range(BOARD_WIDTH):
        if board[0][col] == EMPTY_TILE:
            return False
    return True


if __name__ == '__main__':
    main()