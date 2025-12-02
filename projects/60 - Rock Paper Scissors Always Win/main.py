import time, sys

def main():
    wins = 0
    moves = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}
    losing_moves = {'ROCK': 'SCISSORS', 'PAPER': 'ROCK', 'SCISSORS': 'PAPER'}

    while True:
        print(f'{wins} Wins, 0 Losses, 0 Ties')
        while True:
            print('Enter your move: (R)ock (P)aper (S)cissors or (Q)uit')
            player_input = input('> ').upper()
            if player_input == 'Q':
                sys.exit()
            if player_input in moves:
                player_move = moves[player_input]
                break
            print('Type one of R, P, S, or Q.')

        print(f'{player_move} versus...')
        time.sleep(0.5)
        print('1...')
        time.sleep(0.25)
        print('2...')
        time.sleep(0.25)
        print('3...')
        time.sleep(0.25)

        computer_move = losing_moves[player_move]
        print(computer_move)
        time.sleep(0.5)

        print('You win!')
        wins += 1

if __name__ == '__main__':
    main()
