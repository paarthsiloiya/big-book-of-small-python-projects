import random
import sys
import time
import os

GARBAGE_CHARS = '~!@#$%^&*()_+-={}[]|\\;:,.<>?/'
DIFFICULTY_LEVELS = {
    'NOVICE': {'attempts': 6, 'word_count': 15, 'hint_bonus': True},
    'ADVANCED': {'attempts': 4, 'word_count': 12, 'hint_bonus': False},
    'EXPERT': {'attempts': 3, 'word_count': 10, 'hint_bonus': False},
    'MASTER': {'attempts': 2, 'word_count': 8, 'hint_bonus': False}
}

try:
    with open('sevenletterwords.txt') as wordListFile:
        WORDS = [word.strip().upper() for word in wordListFile.readlines()]
except FileNotFoundError:
    WORDS = ['MONITOR', 'CONTROL', 'NETWORK', 'SYSTEMS', 'DEVICES', 'PROGRAM', 
             'DIGITAL', 'MACHINE', 'PROCESS', 'HANDLER', 'POINTER', 'COMMAND',
             'PACKAGE', 'SERVICE', 'FACTORY', 'MANAGER', 'ELEMENT', 'CIRCUIT']

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def typewriter_print(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def simulate_loading(text="ACCESSING MAINFRAME", duration=2):
    print(f"{text}", end="", flush=True)
    for _ in range(duration * 4):
        print(".", end="", flush=True)
        time.sleep(0.25)
    print(" COMPLETE")

def get_difficulty():
    clear_screen()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 15 + "DIFFICULTY SELECTION" + " " * 15 + "║")
    print("╠" + "═" * 50 + "╣")
    
    for i, (level, settings) in enumerate(DIFFICULTY_LEVELS.items(), 1):
        attempts = settings['attempts']
        word_count = settings['word_count']
        bonus = " + HINTS" if settings['hint_bonus'] else ""
        print(f"║ {i}. {level:<8} │ {attempts} attempts │ {word_count} words{bonus:<8} ║")
    
    print("╚" + "═" * 50 + "╝")
    
    while True:
        try:
            choice = int(input("\nSelect difficulty (1-4): "))
            if 1 <= choice <= 4:
                level_name = list(DIFFICULTY_LEVELS.keys())[choice - 1]
                return level_name, DIFFICULTY_LEVELS[level_name]
        except (ValueError, IndexError):
            pass
        print("Invalid selection. Please enter 1, 2, 3, or 4.")

def main():
    clear_screen()
    typewriter_print("╔" + "═" * 60 + "╗")
    typewriter_print("║" + " " * 20 + "ROBCO INDUSTRIES" + " " * 24 + "║")
    typewriter_print("║" + " " * 15 + "UNIFIED OPERATING SYSTEM" + " " * 21 + "║")
    typewriter_print("║" + " " * 25 + "COPYRIGHT 2075-2077" + " " * 16 + "║")
    typewriter_print("╚" + "═" * 60 + "╝", 0.01)
    
    time.sleep(1)
    simulate_loading("INITIALIZING TERMINAL")
    time.sleep(0.5)
    
    print("\n" + "█" * 62)
    typewriter_print("█ UNAUTHORIZED ACCESS DETECTED - LOCKOUT IMMINENT █", 0.02)
    print("█" * 62)
    
    print("\nFind the correct password in the computer's memory.")
    print("Each guess reveals how many letters match in the correct position.")
    
    input("\nPress ENTER to continue...")
    
    difficulty_name, difficulty_settings = get_difficulty()
    
    clear_screen()
    simulate_loading(f"LOADING {difficulty_name} DIFFICULTY")
    
    game_words = get_words(difficulty_settings['word_count'])
    computer_memory = get_computer_memory_string(game_words)
    secret_password = game_words[0]
    
    clear_screen()
    print(f"DIFFICULTY: {difficulty_name}")
    print(f"ATTEMPTS REMAINING: {difficulty_settings['attempts']}")
    print("=" * 70)
    print(computer_memory)
    print("=" * 70)
    
    attempts_used = 0
    max_attempts = difficulty_settings['attempts']
    
    for attempt in range(max_attempts):
        attempts_remaining = max_attempts - attempt
        player_guess = ask_for_player_guess(game_words, attempts_remaining, difficulty_settings)
        
        if player_guess == secret_password:
            clear_screen()
            typewriter_print(">" * 70, 0.01)
            typewriter_print("> ACCESS GRANTED", 0.05)
            typewriter_print(">" * 70, 0.01)
            typewriter_print(f"> Welcome, authorized user", 0.03)
            typewriter_print(f"> Password cracked in {attempt + 1} attempts", 0.03)
            if attempt == 0:
                typewriter_print("> EXCEPTIONAL PERFORMANCE DETECTED", 0.03)
            elif attempt == 1:
                typewriter_print("> EXCELLENT HACKING SKILLS", 0.03)
            return
        else:
            attempts_used += 1
            matches = num_matching_letters(secret_password, player_guess)
            
            print(f"\n>>> ACCESS DENIED <<<")
            print(f">>> Likeness: {matches}/7 <<<")
            
            if difficulty_settings['hint_bonus'] and matches > 0:
                matching_positions = []
                for i in range(len(secret_password)):
                    if secret_password[i] == player_guess[i]:
                        matching_positions.append(i + 1)
                if matching_positions:
                    print(f">>> Matching positions: {', '.join(map(str, matching_positions))} <<<")
            
            if attempts_remaining > 1:
                print(f"\n{attempts_remaining - 1} ATTEMPTS REMAINING")
                time.sleep(1.5)
    
    clear_screen()
    typewriter_print("!" * 70, 0.01)
    typewriter_print("! TERMINAL LOCKED - MAXIMUM ATTEMPTS EXCEEDED !", 0.05)
    typewriter_print("!" * 70, 0.01)
    typewriter_print(f"! Correct password was: {secret_password}", 0.03)
    typewriter_print("! System entering lockdown mode...", 0.03)

def get_words(word_count):
    if len(WORDS) < word_count:
        return random.sample(WORDS * 3, word_count)
    
    secret_password = random.choice(WORDS)
    words = [secret_password]
    
    zero_match_target = min(2, word_count // 6)
    while len(words) < 1 + zero_match_target:
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) == 0:
            words.append(random_word)
    
    partial_match_target = min(3, word_count // 4)
    for _ in range(500):
        if len(words) >= 1 + zero_match_target + partial_match_target:
            break
        random_word = get_one_word_except(words)
        matches = num_matching_letters(secret_password, random_word)
        if 2 <= matches <= 4:
            words.append(random_word)
    
    some_match_target = word_count - 2
    for _ in range(500):
        if len(words) >= some_match_target:
            break
        random_word = get_one_word_except(words)
        if num_matching_letters(secret_password, random_word) > 0:
            words.append(random_word)
    
    while len(words) < word_count:
        random_word = get_one_word_except(words)
        words.append(random_word)
    
    random.shuffle(words)
    words[0] = secret_password
    return words

def get_one_word_except(blocklist=None):
    if blocklist is None:
        blocklist = []
    
    while True:
        random_word = random.choice(WORDS)
        if random_word not in blocklist:
            return random_word

def num_matching_letters(word1, word2):
    return sum(c1 == c2 for c1, c2 in zip(word1, word2))

def get_computer_memory_string(words):
    lines_with_words = random.sample(range(32), len(words))
    memory_address = 16 * random.randint(0, 4000)
    
    computer_memory = []
    next_word = 0
    
    for line_num in range(16):
        left_half = ''.join(random.choice(GARBAGE_CHARS) for _ in range(16))
        right_half = ''.join(random.choice(GARBAGE_CHARS) for _ in range(16))
        
        if line_num in lines_with_words:
            insertion_index = random.randint(0, 9)
            left_half = (left_half[:insertion_index] + words[next_word] + 
                        left_half[insertion_index + 7:])
            next_word += 1
        
        if line_num + 16 in lines_with_words:
            insertion_index = random.randint(0, 9)
            right_half = (right_half[:insertion_index] + words[next_word] + 
                         right_half[insertion_index + 7:])
            next_word += 1
        
        left_addr = f"0x{memory_address:04X}"
        right_addr = f"0x{memory_address + 256:04X}"
        
        computer_memory.append(f"{left_addr}  {left_half}    {right_addr}  {right_half}")
        memory_address += 16
    
    return '\n'.join(computer_memory)

def ask_for_player_guess(words, tries_remaining, difficulty_settings):
    while True:
        print(f"\nEnter password ({tries_remaining} attempts remaining)")
        
        if difficulty_settings['hint_bonus']:
            print("Available passwords:")
            for i, word in enumerate(words):
                if i % 4 == 0:
                    print()
                print(f"{word:<10}", end="")
            print("\n")
        
        guess = input("> ").upper().strip()
        
        if guess in words:
            return guess
        elif len(guess) == 7 and guess.isalpha():
            print("That password is not in the system memory.")
        else:
            print("Invalid input. Enter a 7-letter word from the list above.")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSystem interrupt detected. Exiting...")
        sys.exit()
