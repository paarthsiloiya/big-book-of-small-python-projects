import time
import random
import sys
import os

SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS', 'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE', 'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE', 'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']

DIFFICULTY_LEVELS = {
    'EASY': {'time_limit': 600, 'accusations': 5},
    'NORMAL': {'time_limit': 300, 'accusations': 3},
    'HARD': {'time_limit': 180, 'accusations': 2}
}

PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    if len(place) > LONGEST_PLACE_NAME_LENGTH:
        LONGEST_PLACE_NAME_LENGTH = len(place)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def select_difficulty():
    clear_screen()
    print("🔍 J'ACCUSE! - DETECTIVE MYSTERY GAME 🔍")
    print("=" * 50)
    print("Select Difficulty Level:")
    print("1. EASY   - 10 minutes, 5 accusations")
    print("2. NORMAL - 5 minutes, 3 accusations") 
    print("3. HARD   - 3 minutes, 2 accusations")
    
    while True:
        choice = input("\nChoose difficulty (1-3): ").strip()
        if choice == '1':
            return DIFFICULTY_LEVELS['EASY']
        elif choice == '2':
            return DIFFICULTY_LEVELS['NORMAL']
        elif choice == '3':
            return DIFFICULTY_LEVELS['HARD']
        print("Invalid choice. Please enter 1, 2, or 3.")

def setup_game():
    difficulty = select_difficulty()
    
    known_suspects_and_items = []
    visited_places = {}
    current_location = 'TAXI'
    accused_suspects = []
    liars = random.sample(SUSPECTS, random.randint(3, 4))
    accusations_left = difficulty['accusations']
    culprit = random.choice(SUSPECTS)

    random.shuffle(SUSPECTS)
    random.shuffle(ITEMS)  
    random.shuffle(PLACES)

    clues = {}
    for i, interviewee in enumerate(SUSPECTS):
        clues[interviewee] = {'debug_liar': interviewee in liars}
        
        for item in ITEMS:
            if interviewee not in liars:
                if random.randint(0, 1) == 0:
                    clues[interviewee][item] = PLACES[ITEMS.index(item)]
                else:
                    clues[interviewee][item] = SUSPECTS[ITEMS.index(item)]
            else:
                if random.randint(0, 1) == 0:
                    while True:
                        clues[interviewee][item] = random.choice(PLACES)
                        if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                            break
                else:
                    while True:
                        clues[interviewee][item] = random.choice(SUSPECTS)
                        if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                            break

        for suspect in SUSPECTS:
            if interviewee not in liars:
                if random.randint(0, 1) == 0:
                    clues[interviewee][suspect] = PLACES[SUSPECTS.index(suspect)]
                else:
                    clues[interviewee][suspect] = ITEMS[SUSPECTS.index(suspect)]
            else:
                if random.randint(0, 1) == 0:
                    while True:
                        clues[interviewee][suspect] = random.choice(PLACES)
                        if clues[interviewee][suspect] != PLACES[SUSPECTS.index(suspect)]:
                            break
                else:
                    while True:
                        clues[interviewee][suspect] = random.choice(ITEMS)
                        if clues[interviewee][suspect] != ITEMS[SUSPECTS.index(suspect)]:
                            break

    zophie_clues = {}
    for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
        kind_of_clue = random.randint(1, 3)
        if kind_of_clue == 1:
            if interviewee not in liars:
                zophie_clues[interviewee] = culprit
            else:
                while True:
                    zophie_clues[interviewee] = random.choice(SUSPECTS)
                    if zophie_clues[interviewee] != culprit:
                        break
        elif kind_of_clue == 2:
            if interviewee not in liars:
                zophie_clues[interviewee] = PLACES[SUSPECTS.index(culprit)]
            else:
                while True:
                    zophie_clues[interviewee] = random.choice(PLACES)
                    if zophie_clues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                        break
        elif kind_of_clue == 3:
            if interviewee not in liars:
                zophie_clues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
            else:
                while True:
                    zophie_clues[interviewee] = random.choice(ITEMS)
                    if zophie_clues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                        break

    return {
        'difficulty': difficulty,
        'known_suspects_and_items': known_suspects_and_items,
        'visited_places': visited_places,
        'current_location': current_location,
        'accused_suspects': accused_suspects,
        'liars': liars,
        'accusations_left': accusations_left,
        'culprit': culprit,
        'clues': clues,
        'zophie_clues': zophie_clues
    }

def display_status(game_state, start_time, end_time):
    clear_screen()
    time_left = max(0, int(end_time - time.time()))
    minutes_left = time_left // 60
    seconds_left = time_left % 60
    
    print("🔍 J'ACCUSE! - DETECTIVE MYSTERY GAME 🔍")
    print("=" * 50)
    print(f"⏰ Time: {minutes_left:02d}:{seconds_left:02d} | 🎯 Accusations: {game_state['accusations_left']}")
    print("🐱 Find ZOPHIE THE CAT before time runs out!")
    print("=" * 50)

def main():
    game_state = setup_game()
    
    clear_screen()
    print("🔍 J'ACCUSE! - DETECTIVE MYSTERY GAME 🔍")
    print("\nYou are detective Mathilde Camus.")
    print("ZOPHIE THE CAT has gone missing!")
    print("\nSome suspects always lie, others always tell the truth.")
    print("Use clues to determine who is trustworthy, then find Zophie!")
    input("\nPress Enter to begin your investigation...")

    start_time = time.time()
    end_time = start_time + game_state['difficulty']['time_limit']

    while True:
        if time.time() > end_time or game_state['accusations_left'] == 0:
            clear_screen()
            print("🚨 CASE CLOSED 🚨")
            if time.time() > end_time:
                print("⏰ Time's up, Detective!")
            else:
                print("❌ Too many wrong accusations!")
            
            culprit_index = SUSPECTS.index(game_state['culprit'])
            print(f"\n🐱 ZOPHIE was with {game_state['culprit']}")
            print(f"📍 Location: {PLACES[culprit_index]}")
            print(f"🔍 Evidence: {ITEMS[culprit_index]}")
            print("\nBetter luck next time, Detective!")
            sys.exit()

        display_status(game_state, start_time, end_time)

        if game_state['current_location'] == 'TAXI':
            print("\n🚖 You are in your TAXI. Where do you want to go?")
            print("-" * 50)
            for place in sorted(PLACES):
                place_info = ''
                if place in game_state['visited_places']:
                    place_info = game_state['visited_places'][place]
                name_label = '(' + place[0] + ')' + place[1:]
                spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
                print(f'{name_label} {spacing}{place_info}')
            print('(Q)UIT GAME')
            
            while True:
                response = input('\n> ').upper()
                if response == 'Q':
                    print('Thanks for playing!')
                    sys.exit()
                if response in PLACE_FIRST_LETTERS.keys():
                    break
                print("Invalid location. Use the first letter of a place or Q to quit.")
            game_state['current_location'] = PLACE_FIRST_LETTERS[response]
            continue

        current_location_index = PLACES.index(game_state['current_location'])
        the_person_here = SUSPECTS[current_location_index]
        the_item_here = ITEMS[current_location_index]
        
        print(f"\n📍 You are at the {game_state['current_location']}.")
        print(f"👤 {the_person_here} with the {the_item_here} is here.")

        if the_person_here not in game_state['known_suspects_and_items']:
            game_state['known_suspects_and_items'].append(the_person_here)
        if the_item_here not in game_state['known_suspects_and_items']:
            game_state['known_suspects_and_items'].append(the_item_here)
        if game_state['current_location'] not in game_state['visited_places'].keys():
            game_state['visited_places'][game_state['current_location']] = f'({the_person_here.lower()}, {the_item_here.lower()})'

        if the_person_here in game_state['accused_suspects']:
            print('\n😠 They are offended by your false accusation!')
            print('They refuse to help with your investigation.')
            input('\nPress Enter to return to your taxi...')
            game_state['current_location'] = 'TAXI'
            continue

        print(f"\n🔍 INVESTIGATION OPTIONS:")
        print(f"(J) 🎯 J'ACCUSE! ({game_state['accusations_left']} accusations left)")
        print("(Z) 🐱 Ask about ZOPHIE THE CAT")
        print("(T) 🚖 Return to TAXI")
        
        for i, suspect_or_item in enumerate(game_state['known_suspects_and_items']):
            print(f'({i + 1}) ❓ Ask about {suspect_or_item}')

        while True:
            response = input('\n> ').upper()
            if response in 'JZT' or (response.isdecimal() and 0 < int(response) <= len(game_state['known_suspects_and_items'])):
                break
            print("Invalid choice. Use J, Z, T, or a number from the list.")

        if response == 'J':
            game_state['accusations_left'] -= 1
            if the_person_here == game_state['culprit']:
                clear_screen()
                print("🎉 CASE SOLVED! 🎉")
                print(f"You've caught {game_state['culprit']}!")
                print("🐱 ZOPHIE THE CAT has been rescued!")
                
                minutes_taken = int(time.time() - start_time) // 60
                seconds_taken = int(time.time() - start_time) % 60
                print(f"⏱️ Solved in {minutes_taken}:{seconds_taken:02d}")
                print("🏆 Excellent detective work!")
                sys.exit()
            else:
                game_state['accused_suspects'].append(the_person_here)
                print(f"\n❌ Wrong accusation! {the_person_here} is innocent.")
                print("They will no longer help you.")
                game_state['current_location'] = 'TAXI'

        elif response == 'Z':
            if the_person_here not in game_state['zophie_clues']:
                print('\n🤷 "I don\'t know anything about ZOPHIE THE CAT."')
            else:
                clue = game_state['zophie_clues'][the_person_here]
                print(f'\n💬 "About Zophie: {clue}"')
                if clue not in game_state['known_suspects_and_items'] and clue not in PLACES:
                    game_state['known_suspects_and_items'].append(clue)

        elif response == 'T':
            game_state['current_location'] = 'TAXI'
            continue

        else:
            thing_being_asked_about = game_state['known_suspects_and_items'][int(response) - 1]
            if thing_being_asked_about in (the_person_here, the_item_here):
                print('\n🤐 "No comment."')
            else:
                clue = game_state['clues'][the_person_here][thing_being_asked_about]
                print(f'\n💬 "About {thing_being_asked_about}: {clue}"')
                if clue not in game_state['known_suspects_and_items'] and clue not in PLACES:
                    game_state['known_suspects_and_items'].append(clue)

        input('\nPress Enter to continue...')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print('\nThanks for playing J\'ACCUSE!')
        sys.exit()
