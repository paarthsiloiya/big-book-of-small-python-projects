import random
import os
import sys

GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

STAR_FACE = ["┌───────────┐",
             "│     .     │",
             "│    ,O,    │",
             "│ 'ooOOOoo' │",
             "│   `OOO`   │",
             "│   O' 'O   │",
             "└───────────┘"]

SKULL_FACE = ["┌───────────┐",
              "│  ╔═════╗  │",
              "│  ║() ()║  │",
              "│  ║  ∧  ║  │",
              "│  ║ VVV ║  │",
              "│   \___/   │",
              "└───────────┘"]

QUESTION_FACE = ["┌───────────┐",
                 "│           │",
                 "│     ?     │",
                 "│     ?     │",
                 "│     ?     │",
                 "│           │",
                 "└───────────┘"]

DICE_COLORS = {
    GOLD: '\033[93m',
    SILVER: '\033[37m', 
    BRONZE: '\033[33m'
}

RESET_COLOR = '\033[0m'
FACE_WIDTH = 13
FACE_HEIGHT = 7

DIFFICULTY_SETTINGS = {
    'EASY': {'target_score': 10, 'skull_limit': 4},
    'NORMAL': {'target_score': 13, 'skull_limit': 3},
    'HARD': {'target_score': 16, 'skull_limit': 2}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_title():
    clear_screen()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 20 + "🌟 LUCKY STARS 🌟" + " " * 21 + "║")
    print("║" + " " * 15 + "Press Your Luck Dice Game" + " " * 18 + "║")
    print("╚" + "═" * 58 + "╝")

def get_difficulty():
    print("\nSelect difficulty level:")
    difficulties = list(DIFFICULTY_SETTINGS.keys())
    for i, diff in enumerate(difficulties, 1):
        settings = DIFFICULTY_SETTINGS[diff]
        print(f"{i}. {diff} - Target: {settings['target_score']} points, Skull limit: {settings['skull_limit']}")
    
    while True:
        try:
            choice = int(input("\nChoose difficulty (1-3): "))
            if 1 <= choice <= 3:
                return difficulties[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_players():
    while True:
        try:
            num_players = int(input("\nHow many players (2-6): "))
            if 2 <= num_players <= 6:
                break
            print("Please enter a number between 2 and 6.")
        except ValueError:
            print("Please enter a valid number.")
    
    player_names = []
    for i in range(num_players):
        while True:
            name = input(f"Enter name for player #{i + 1}: ").strip()
            if name and name not in player_names:
                player_names.append(name)
                break
            print("Please enter a unique, non-empty name.")
    
    return player_names

def create_dice_cup():
    return ([GOLD] * 6) + ([SILVER] * 4) + ([BRONZE] * 3)

def roll_die(dice_type):
    roll = random.randint(1, 6)
    if dice_type == GOLD:
        if 1 <= roll <= 3:
            return 'STAR'
        elif 4 <= roll <= 5:
            return 'QUESTION'
        else:
            return 'SKULL'
    elif dice_type == SILVER:
        if 1 <= roll <= 2:
            return 'STAR'
        elif 3 <= roll <= 4:
            return 'QUESTION'
        else:
            return 'SKULL'
    else:
        if roll == 1:
            return 'STAR'
        elif 2 <= roll <= 3:
            return 'QUESTION'
        else:
            return 'SKULL'

def display_dice_roll(hand, roll_results):
    print("\n" + "═" * 45)
    
    for line_num in range(FACE_HEIGHT):
        for dice_num in range(len(roll_results)):
            dice_type = hand[dice_num]
            color = DICE_COLORS.get(dice_type, '')
            
            if roll_results[dice_num] == 'STAR':
                face = STAR_FACE
            elif roll_results[dice_num] == 'SKULL':
                face = SKULL_FACE
            else:
                face = QUESTION_FACE
            
            print(color + face[line_num] + RESET_COLOR + " ", end="")
        print()
    
    for dice_type in hand:
        color = DICE_COLORS.get(dice_type, '')
        print(color + dice_type.center(FACE_WIDTH) + RESET_COLOR + " ", end="")
    print("\n" + "═" * 45)

def display_scores(player_names, player_scores):
    print("\n🏆 CURRENT SCORES:")
    sorted_players = sorted(player_names, key=lambda x: player_scores[x], reverse=True)
    for i, name in enumerate(sorted_players):
        score = player_scores[name]
        medal = "🥇" if i == 0 else "🥈" if i == 1 else "🥉" if i == 2 else "  "
        print(f"{medal} {name}: {score} points")

def player_turn(player_name, cup, settings):
    stars = 0
    skulls = 0
    hand = []
    
    print(f"\n🎲 {player_name}'s turn!")
    
    while True:
        if (3 - len(hand)) > len(cup):
            print(f"⚠️ Not enough dice in cup for {player_name}'s turn!")
            break
        
        random.shuffle(cup)
        while len(hand) < 3:
            hand.append(cup.pop())
        
        roll_results = []
        for dice in hand:
            result = roll_die(dice)
            roll_results.append(result)
            
            if result == 'STAR':
                stars += 1
            elif result == 'SKULL':
                skulls += 1
        
        display_dice_roll(hand, roll_results)
        print(f"⭐ Stars: {stars}  💀 Skulls: {skulls}")
        
        if skulls >= settings['skull_limit']:
            print(f"\n💀 {settings['skull_limit']} or more skulls! You lose all stars!")
            input("Press Enter to continue...")
            return 0
        
        choice = input(f"\n{player_name}, roll again? (y/n): ").lower()
        if choice.startswith('n'):
            print(f"\n🌟 {player_name} collected {stars} stars!")
            input("Press Enter to continue...")
            return stars
        
        next_hand = []
        for i in range(3):
            if roll_results[i] == 'QUESTION':
                next_hand.append(hand[i])
        hand = next_hand

def main():
    display_title()
    
    print("\n🎮 Welcome to Lucky Stars!")
    print("Roll dice to collect stars, but beware of skulls!")
    
    difficulty = get_difficulty()
    settings = DIFFICULTY_SETTINGS[difficulty]
    player_names = get_players()
    
    player_scores = {name: 0 for name in player_names}
    
    print(f"\n🎯 Game Settings:")
    print(f"Difficulty: {difficulty}")
    print(f"Target Score: {settings['target_score']} points")
    print(f"Skull Limit: {settings['skull_limit']} skulls")
    input("\nPress Enter to start the game...")
    
    turn = 0
    end_game_with = None
    
    while True:
        clear_screen()
        display_scores(player_names, player_scores)
        
        current_player = player_names[turn]
        cup = create_dice_cup()
        
        stars_earned = player_turn(current_player, cup, settings)
        player_scores[current_player] += stars_earned
        
        if end_game_with is None and player_scores[current_player] >= settings['target_score']:
            print(f"\n🎊 {current_player} reached {settings['target_score']} points!")
            print("Everyone else gets one final turn!")
            end_game_with = current_player
            input("Press Enter to continue...")
        
        turn = (turn + 1) % len(player_names)
        
        if end_game_with == player_names[turn]:
            break
    
    clear_screen()
    print("🏁 GAME OVER!")
    display_scores(player_names, player_scores)
    
    highest_score = max(player_scores.values())
    winners = [name for name, score in player_scores.items() if score == highest_score]
    
    if len(winners) == 1:
        print(f"\n🏆 The winner is {winners[0]}!")
    else:
        print(f"\n🏆 It's a tie! Winners: {', '.join(winners)}")
    
    print("\nThanks for playing Lucky Stars! 🌟")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print("\nGame interrupted. Thanks for playing! 🌟")
        sys.exit()