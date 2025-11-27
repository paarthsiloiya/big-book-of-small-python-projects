import random, time, sys

def main():
    wins = 0
    losses = 0
    ties = 0
    
    moves = {'R': 'ROCK', 'P': 'PAPER', 'S': 'SCISSORS'}
    
    while True:
        print(f'{wins} Wins, {losses} Losses, {ties} Ties')
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

        computer_move = random.choice(list(moves.values()))
        print(computer_move)
        time.sleep(0.5)

        if player_move == computer_move:
            print('It\'s a tie!')
            ties += 1
        elif (player_move == 'ROCK' and computer_move == 'SCISSORS') or \
             (player_move == 'PAPER' and computer_move == 'ROCK') or \
             (player_move == 'SCISSORS' and computer_move == 'PAPER'):
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1

if __name__ == '__main__':
    main()
