import random
import sys
import os
import time

ALL_CLOSED = """
+------+  +------+  +------+
|      |  |      |  |      |
|   1  |  |   2  |  |   3  |
|      |  |      |  |      |
|      |  |      |  |      |
|      |  |      |  |      |
+------+  +------+  +------+"""

FIRST_GOAT = """
+------+  +------+  +------+
|  ((  |  |      |  |      |
|  oo  |  |   2  |  |   3  |
| /_/|_|  |      |  |      |
|    | |  |      |  |      |
|GOAT|||  |      |  |      |
+------+  +------+  +------+"""

SECOND_GOAT = """
+------+  +------+  +------+
|      |  |  ((  |  |      |
|   1  |  |  oo  |  |   3  |
|      |  | /_/|_|  |      |
|      |  |    | |  |      |
|      |  |GOAT|||  |      |
+------+  +------+  +------+"""

THIRD_GOAT = """
+------+  +------+  +------+
|      |  |      |  |  ((  |
|   1  |  |   2  |  |  oo  |
|      |  |      |  | /_/|_|
|      |  |      |  |    | |
|      |  |      |  |GOAT|||
+------+  +------+  +------+"""

FIRST_CAR = """
+------+  +------+  +------+
| CAR! |  |  ((  |  |  ((  |
|    __|  |  oo  |  |  oo  |
|  _/  |  | /_/|_|  | /_/|_|
| /_ __|  |    | |  |    | |
|   O  |  |GOAT|||  |GOAT|||
+------+  +------+  +------+"""

SECOND_CAR = """
+------+  +------+  +------+
|  ((  |  | CAR! |  |  ((  |
|  oo  |  |    __|  |  oo  |
| /_/|_|  |  _/  |  | /_/|_|
|    | |  | /_ __|  |    | |
|GOAT|||  |   O  |  |GOAT|||
+------+  +------+  +------+"""

THIRD_CAR = """
+------+  +------+  +------+
|  ((  |  |  ((  |  | CAR! |
|  oo  |  |  oo  |  |    __|
| /_/|_|  | /_/|_|  |  _/  |
|    | |  |    | |  | /_ __|
|GOAT|||  |GOAT|||  |   O  |
+------+  +------+  +------+"""

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_welcome():
    clear_screen()
    print('🎪 ' + '=' * 70 + ' 🎪')
    print('|' + ' ' * 70 + '|')
    print('|' + '     🎯 THE MONTY HALL PROBLEM - Probability Game 🎯    '.center(70) + '|')
    print('|' + ' ' * 70 + '|')
    print('|' + '   Test the famous probability paradox that stumped    '.center(70) + '|')
    print('|' + '   mathematicians! Will you swap doors or stay put?    '.center(70) + '|')
    print('|' + ' ' * 70 + '|')
    print('🎪 ' + '=' * 70 + ' 🎪')
    print()

def show_rules():
    print('📋 GAME RULES:')
    print('1. Choose one of three doors - one has a car 🚗, two have goats 🐐')
    print('2. Host opens a door with a goat that you didn\'t pick')
    print('3. You can STAY with your choice or SWAP to the other door')
    print('4. Mathematical theory says swapping gives you 67% win rate!')
    print()
    print('🎯 Let\'s test this theory with real gameplay!')
    print()

def get_game_mode():
    while True:
        print('🎮 Choose game mode:')
        print('1. 📚 Tutorial mode (with explanations)')
        print('2. 🚀 Quick play mode')
        print('3. 🧪 Auto-simulation (1000 games)')
        
        choice = input('\nEnter choice (1-3): ').strip()
        if choice in ['1', '2', '3']:
            return int(choice)
        print('❌ Please enter 1, 2, or 3!')

def animate_door_reveal(door_num):
    animations = ['🚪', '📂', '🔍', '👀']
    for anim in animations:
        print(f'\rOpening door {door_num}... {anim}', end='', flush=True)
        time.sleep(0.3)
    print()

def get_door_choice():
    while True:
        print(ALL_CLOSED)
        print('\n🎯 Pick a door 1, 2, or 3 (or "quit" to stop, "stats" for statistics):')
        response = input('> ').upper().strip()
        
        if response == 'QUIT':
            return 'QUIT'
        elif response == 'STATS':
            return 'STATS'
        elif response in ['1', '2', '3']:
            return int(response)
        else:
            print('❌ Please enter 1, 2, 3, "quit", or "stats"!')

def find_goat_door(car_door, player_door):
    doors = [1, 2, 3]
    doors.remove(car_door)
    if player_door in doors:
        doors.remove(player_door)
        return doors[0] if doors else random.choice([d for d in [1, 2, 3] if d != car_door and d != player_door])
    return doors[0]

def display_goat_door(goat_door, tutorial_mode=False):
    goat_displays = {1: FIRST_GOAT, 2: SECOND_GOAT, 3: THIRD_GOAT}
    
    if tutorial_mode:
        animate_door_reveal(goat_door)
    
    print(goat_displays[goat_door])
    print(f'🐐 Door {goat_door} contains a goat!')
    
    if tutorial_mode:
        print('\n💡 Now you have a choice: STAY with your original door or SWAP to the other unopened door.')
        print('   Mathematical theory suggests swapping improves your odds from 33% to 67%!')

def get_swap_choice(original_door, goat_door, tutorial_mode=False):
    remaining_door = [d for d in [1, 2, 3] if d != original_door and d != goat_door][0]
    
    while True:
        if tutorial_mode:
            print(f'\n🤔 You picked door {original_door}. Door {goat_door} has a goat.')
            print(f'   Do you want to SWAP to door {remaining_door} or STAY with door {original_door}?')
        
        print('🔄 Swap doors? (Y)es / (N)o / (E)xplain:')
        choice = input('> ').upper().strip()
        
        if choice in ['Y', 'YES']:
            return True
        elif choice in ['N', 'NO']:
            return False
        elif choice in ['E', 'EXPLAIN']:
            explain_probability()
        else:
            print('❌ Please enter Y, N, or E!')

def explain_probability():
    print('\n📊 PROBABILITY EXPLANATION:')
    print('• Initially, each door has a 1/3 (33.33%) chance of having the car')
    print('• Your chosen door keeps its 1/3 probability')
    print('• The other two doors combined have 2/3 (66.67%) probability') 
    print('• When host opens one goat door, the remaining door gets the full 2/3!')
    print('• Therefore: STAY = 33% chance, SWAP = 67% chance')
    print('• This is why swapping doubles your chances of winning! 🎯')
    input('\nPress Enter to continue...')

def display_final_result(car_door):
    car_displays = {1: FIRST_CAR, 2: SECOND_CAR, 3: THIRD_CAR}
    print(car_displays[car_door])
    print(f'🚗 Door {car_door} had the car!')

def calculate_win_percentage(wins, total):
    return round((wins / total * 100), 1) if total > 0 else 0.0

def display_statistics(swap_wins, swap_total, stay_wins, stay_total, game_mode):
    total_games = swap_total + stay_total
    
    print('\n📊 GAME STATISTICS')
    print('=' * 50)
    print(f'Total Games Played: {total_games}')
    
    if swap_total > 0:
        swap_percentage = calculate_win_percentage(swap_wins, swap_total)
        print(f'🔄 SWAPPING:   {swap_wins:>3}/{swap_total:<3} wins ({swap_percentage:>5.1f}%) Expected: ~67%')
    
    if stay_total > 0:
        stay_percentage = calculate_win_percentage(stay_wins, stay_total)
        print(f'🚪 STAYING:    {stay_wins:>3}/{stay_total:<3} wins ({stay_percentage:>5.1f}%) Expected: ~33%')
    
    if total_games >= 10:
        if swap_total > 0 and stay_total > 0:
            difference = calculate_win_percentage(swap_wins, swap_total) - calculate_win_percentage(stay_wins, stay_total)
            print(f'📈 Swap Advantage: {difference:+.1f}%')
        
        if total_games >= 100:
            theoretical_convergence = abs(calculate_win_percentage(swap_wins, swap_total) - 66.67) if swap_total > 0 else 100
            print(f'🎯 Theory Accuracy: {100 - theoretical_convergence:.1f}%')

def run_auto_simulation():
    print('\n🧪 Running 1000 game simulation...')
    
    swap_wins = stay_wins = 0
    
    for i in range(1000):
        if i % 100 == 0:
            print(f'Progress: {i//10}%', end='\r')
        
        car_door = random.randint(1, 3)
        player_door = random.randint(1, 3)
        goat_door = find_goat_door(car_door, player_door)
        
        should_swap = random.choice([True, False])
        
        if should_swap:
            final_door = [d for d in [1, 2, 3] if d != player_door and d != goat_door][0]
            if final_door == car_door:
                swap_wins += 1
        else:
            if player_door == car_door:
                stay_wins += 1
    
    print('Progress: 100%')
    print('\n🎊 SIMULATION COMPLETE!')
    display_statistics(swap_wins, 500, stay_wins, 500, 3)
    
    expected_swap_wins = 500 * (2/3)
    expected_stay_wins = 500 * (1/3)
    
    print(f'\n🔬 THEORETICAL vs ACTUAL:')
    print(f'Swap wins: {swap_wins} (expected: ~{expected_swap_wins:.0f})')
    print(f'Stay wins: {stay_wins} (expected: ~{expected_stay_wins:.0f})')

def play_single_game(tutorial_mode):
    car_door = random.randint(1, 3)
    
    player_door = get_door_choice()
    if player_door in ['QUIT', 'STATS']:
        return player_door, None
    
    goat_door = find_goat_door(car_door, player_door)
    
    clear_screen()
    display_goat_door(goat_door, tutorial_mode)
    
    swapped = get_swap_choice(player_door, goat_door, tutorial_mode)
    
    if swapped:
        final_door = [d for d in [1, 2, 3] if d != player_door and d != goat_door][0]
        action = 'SWAPPED'
    else:
        final_door = player_door
        action = 'STAYED'
    
    clear_screen()
    display_final_result(car_door)
    
    won = (final_door == car_door)
    
    if won:
        print(f'🎉 YOU WON! You {action.lower()} and got the car! 🚗')
    else:
        print(f'😔 You lost. You {action.lower()} and got a goat. 🐐')
    
    return action, won

def main():
    display_welcome()
    show_rules()
    
    game_mode = get_game_mode()
    
    if game_mode == 3:
        run_auto_simulation()
        input('\nPress Enter to exit...')
        return
    
    tutorial_mode = (game_mode == 1)
    
    swap_wins = swap_total = stay_wins = stay_total = 0
    
    while True:
        clear_screen()
        
        if swap_total + stay_total > 0:
            display_statistics(swap_wins, swap_total, stay_wins, stay_total, game_mode)
            print()
        
        result = play_single_game(tutorial_mode)
        
        if result[0] == 'QUIT':
            break
        elif result[0] == 'STATS':
            display_statistics(swap_wins, swap_total, stay_wins, stay_total, game_mode)
            input('\nPress Enter to continue...')
            continue
        
        action, won = result
        
        if action == 'SWAPPED':
            swap_total += 1
            if won:
                swap_wins += 1
        else:
            stay_total += 1
            if won:
                stay_wins += 1
        
        input('\n🎮 Press Enter to play again...')
    
    clear_screen()
    if swap_total + stay_total > 0:
        print('🎊 FINAL STATISTICS:')
        display_statistics(swap_wins, swap_total, stay_wins, stay_total, game_mode)
    
    print('\n🎪 Thanks for exploring the Monty Hall Problem! 🎪')
    print('Remember: In probability, counterintuitive results are often correct! 🧠')

if __name__ == '__main__':
    main()