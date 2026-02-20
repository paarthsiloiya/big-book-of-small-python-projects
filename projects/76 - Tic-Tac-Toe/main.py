def print_board(board):
    print(f'\n {board[0]} | {board[1]} | {board[2]} ')
    print('---+---+---')
    print(f' {board[3]} | {board[4]} | {board[5]} ')
    print('---+---+---')
    print(f' {board[6]} | {board[7]} | {board[8]} \n')

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_board_full(board):
    return ' ' not in board

def main():
    board = [' '] * 9
    current_player = 'X'
    
    print('Welcome to Tic-Tac-Toe!')

    while True:
        print_board(board)

        while True:
            try:
                move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] == ' ':
                    board[move] = current_player
                    break
                else:
                    print("Invalid move or position taken. Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
