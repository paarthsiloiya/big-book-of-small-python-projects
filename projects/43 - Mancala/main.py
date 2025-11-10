import sys
import os

PLAYER_1_PITS = ('A', 'B', 'C', 'D', 'E', 'F')
PLAYER_2_PITS = ('G', 'H', 'I', 'J', 'K', 'L')

OPPOSITE_PIT = {'A': 'G', 'B': 'H', 'C': 'I', 'D': 'J', 'E': 'K',
                'F': 'L', 'G': 'A', 'H': 'B', 'I': 'C', 'J': 'D',
                'K': 'E', 'L': 'F'}

NEXT_PIT = {'A': 'B', 'B': 'C', 'C': 'D', 'D': 'E', 'E': 'F', 'F': '1',
            '1': 'L', 'L': 'K', 'K': 'J', 'J': 'I', 'I': 'H', 'H': 'G',
            'G': '2', '2': 'A'}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    clear_screen()
    print('🏺 ' + '=' * 60 + ' 🏺')
    print('|' + ' ' * 64 + '|')
    print('|' + '          🌟 MANCALA - The Ancient Seed Game 🌟         '.center(62) + '|')
    print('|' + ' ' * 64 + '|')
    print('|' + '  Grab seeds from your pit and sow counterclockwise!  '.center(64) + '|')
    print('|' + '  Land in your store for a free turn! 🎯               '.center(63) + '|')
    print('|' + '  Capture opponent seeds from empty pit landings! ⚡   '.center(63) + '|')
    print('|' + ' ' * 64 + '|')
    print('🏺 ' + '=' * 60 + ' 🏺')
    print()

def get_difficulty():
    while True:
        print('Choose difficulty:')
        print('1. Easy (3 seeds per pit)')
        print('2. Normal (4 seeds per pit)')  
        print('3. Hard (6 seeds per pit)')
        print('4. Extreme (8 seeds per pit)')
        
        choice = input('\nEnter choice (1-4): ').strip()
        if choice == '1':
            return 3
        elif choice == '2':
            return 4
        elif choice == '3':
            return 6
        elif choice == '4':
            return 8
        else:
            print('Invalid choice! Please enter 1-4.')

def get_new_board(starting_seeds):
    return {'1': 0, '2': 0, 'A': starting_seeds, 'B': starting_seeds, 
            'C': starting_seeds, 'D': starting_seeds, 'E': starting_seeds,
            'F': starting_seeds, 'G': starting_seeds, 'H': starting_seeds, 
            'I': starting_seeds, 'J': starting_seeds, 'K': starting_seeds, 
            'L': starting_seeds}

def display_board(board, player_turn, move_count):
    clear_screen()
    
    print('🏺 ' + '=' * 70 + ' 🏺')
    print(f'   Turn: Player {player_turn} {"🔥" if player_turn == "1" else "❄️"}' + 
          f'                                 Move: {move_count}')
    print()

    seed_amounts = []
    for pit in 'GHIJKL21ABCDEF':
        num_seeds = str(board[pit]).rjust(2)
        seed_amounts.append(num_seeds)

    print('<<- PLAYER 2'.center(57))
    print('┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐')
    print('│      │  G   │  H   │  I   │  J   │  K   │  L   │      │')
    print('│  P2  ├──────┼──────┼──────┼──────┼──────┼──────┤  P1  │')
    print(f'│ 🏪   │  {seed_amounts[0]}  │  {seed_amounts[1]}  │  {seed_amounts[2]}  │  {seed_amounts[3]}  │  {seed_amounts[4]}  │  {seed_amounts[5]}  │  🏪  │')
    print(f'│ {seed_amounts[6]}   ├──────┼──────┼──────┼──────┼──────┼──────┤  {seed_amounts[7]}  │')
    print(f'│      │  {seed_amounts[8]}  │  {seed_amounts[9]}  │  {seed_amounts[10]}  │  {seed_amounts[11]}  │  {seed_amounts[12]}  │  {seed_amounts[13]}  │      │')
    print('│      ├──────┼──────┼──────┼──────┼──────┼──────┤      │')
    print('│      │  A   │  B   │  C   │  D   │  E   │  F   │      │')
    print('└──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘')
    print('PLAYER 1 ->>'.center(57))
    print(f'      Player 1: {board["1"]} seeds 🔥     Player 2: {board["2"]} seeds ❄️')
    print()

def ask_for_player_move(player_turn, board):
    while True:
        if player_turn == '1':
            print('🔥 Player 1, choose your move: A-F (or QUIT) 🔥')
        elif player_turn == '2':
            print('❄️  Player 2, choose your move: G-L (or QUIT) ❄️')
        
        response = input('> ').upper().strip()

        if response == 'QUIT':
            print('\n👋 Thanks for playing Mancala! 👋')
            sys.exit()

        if response == 'HELP':
            print('\n📋 HELP:')
            print('- Choose a pit letter (A-F for Player 1, G-L for Player 2)')
            print('- Seeds will be distributed counterclockwise')
            print('- Land in your store (rightmost) for another turn!')
            print('- Land in empty pit on your side to capture opposite seeds!')
            print()
            continue

        if (player_turn == '1' and response not in PLAYER_1_PITS) or (
            player_turn == '2' and response not in PLAYER_2_PITS):
            print('❌ Please pick a letter on your side of the board!')
            continue
        
        if board.get(response) == 0:
            print('❌ Please pick a pit with seeds!')
            continue
        
        return response

def make_move(board, player_turn, pit):
    seeds_to_sow = board[pit]
    board[pit] = 0
    
    print(f'\n🌱 Sowing {seeds_to_sow} seeds from pit {pit}...')
    
    while seeds_to_sow > 0:
        pit = NEXT_PIT[pit]
        if (player_turn == '1' and pit == '2') or (player_turn == '2' and pit == '1'):
            continue
        board[pit] += 1
        seeds_to_sow -= 1

    if (pit == player_turn == '1') or (pit == player_turn == '2'):
        print('🎯 Last seed in your store! FREE TURN! 🎯')
        input('Press Enter to continue...')
        return player_turn

    if player_turn == '1' and pit in PLAYER_1_PITS and board[pit] == 1:
        opposite_pit = OPPOSITE_PIT[pit]
        captured = board[opposite_pit]
        if captured > 0:
            board['1'] += captured + 1
            board[opposite_pit] = 0
            board[pit] = 0
            print(f'⚡ CAPTURE! Took {captured} seeds from pit {opposite_pit}! ⚡')
    elif player_turn == '2' and pit in PLAYER_2_PITS and board[pit] == 1:
        opposite_pit = OPPOSITE_PIT[pit]
        captured = board[opposite_pit]
        if captured > 0:
            board['2'] += captured + 1
            board[opposite_pit] = 0
            board[pit] = 0
            print(f'⚡ CAPTURE! Took {captured} seeds from pit {opposite_pit}! ⚡')

    input('Press Enter to continue...')
    return '2' if player_turn == '1' else '1'

def check_for_winner(board):
    player1_total = sum(board[pit] for pit in PLAYER_1_PITS)
    player2_total = sum(board[pit] for pit in PLAYER_2_PITS)

    if player1_total == 0:
        board['2'] += player2_total
        for pit in PLAYER_2_PITS:
            board[pit] = 0
    elif player2_total == 0:
        board['1'] += player1_total
        for pit in PLAYER_1_PITS:
            board[pit] = 0
    else:
        return 'no winner'

    if board['1'] > board['2']:
        return '1'
    elif board['2'] > board['1']:
        return '2'
    else:
        return 'tie'

def display_final_results(board, winner):
    clear_screen()
    print('🏆 ' + '=' * 50 + ' 🏆')
    print()
    
    if winner == '1':
        print('🔥 🎉 PLAYER 1 WINS! 🎉 🔥')
    elif winner == '2':
        print('❄️  🎉 PLAYER 2 WINS! 🎉 ❄️')
    else:
        print('🤝 IT\'S A TIE! GREAT GAME! 🤝')
    
    print()
    print(f'Final Score:')
    print(f'Player 1: {board["1"]} seeds 🔥')
    print(f'Player 2: {board["2"]} seeds ❄️')
    print()
    print('🏆 ' + '=' * 50 + ' 🏆')

def play_again():
    while True:
        choice = input('\nPlay another game? (y/n): ').lower().strip()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print('Please enter y or n.')

def main():
    while True:
        display_welcome()
        starting_seeds = get_difficulty()
        
        game_board = get_new_board(starting_seeds)
        player_turn = '1'
        move_count = 0
        
        while True:
            move_count += 1
            display_board(game_board, player_turn, move_count)
            player_move = ask_for_player_move(player_turn, game_board)
            player_turn = make_move(game_board, player_turn, player_move)
            
            winner = check_for_winner(game_board)
            if winner != 'no winner':
                display_board(game_board, player_turn, move_count)
                display_final_results(game_board, winner)
                break
        
        if not play_again():
            print('\n👋 Thanks for playing Mancala! Goodbye! 👋')
            break

if __name__ == '__main__':
    main()