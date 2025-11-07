import random
import sys
import os

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

CHAR_MAPPINGS = {
    'a': ['4', '@', '/-\\', '^', 'λ'],
    'b': ['8', '|3', 'ß', '6'],
    'c': ['(', '<', '©', '¢'],
    'd': ['|)', 'cl', '|]'],
    'e': ['3', '€', '[-'],
    'f': ['ph', '|=', 'ƒ'],
    'g': ['9', '6', '&'],
    'h': [']-[', '|-|', '#', '|-'],
    'i': ['1', '!', '|', ']['],
    'j': ['_|', ']'],
    'k': [']<', '|<', '/<'],
    'l': ['1', '|_', '|', '7'],
    'm': ['|v|', 'M', '/\\/\\'],
    'n': ['|\\|', '/\\/', 'И'],
    'o': ['0', '()', '[]', '°'],
    'p': ['|*', '|D', '|>'],
    'q': ['(_,)', '9'],
    'r': ['12', '|2', 'R'],
    's': ['$', '5', 'z', '§'],
    't': ['7', '+', '†', '1'],
    'u': ['|_|', 'µ', 'v'],
    'v': ['\\/', 'V'],
    'w': ['\\/\\/', 'vv', 'W'],
    'x': ['><', '%', 'X'],
    'y': ['`/', 'Y', '¥'],
    'z': ['2', '7_', '%', 'Z']
}

LEET_LEVELS = {
    'mild': 0.3,
    'medium': 0.5,
    'heavy': 0.7,
    'extreme': 0.9
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    clear_screen()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 15 + "L33T 5P34K 60N\/3RT3R" + " " * 14 + "║")
    print("╚" + "═" * 50 + "╝")
    print("\nOptions:")
    print("1. Convert text to leetspeak")
    print("2. Batch convert from file")
    print("3. Interactive mode")
    print("4. Reverse leetspeak (decode)")
    print("5. Exit")

def get_leet_level():
    print("\nSelect leetspeak intensity:")
    for i, (level, percentage) in enumerate(LEET_LEVELS.items(), 1):
        print(f"{i}. {level.upper()} - {int(percentage*100)}% conversion rate")
    
    while True:
        try:
            choice = int(input("\nEnter choice (1-4): "))
            if 1 <= choice <= 4:
                level_name = list(LEET_LEVELS.keys())[choice - 1]
                return LEET_LEVELS[level_name]
            print("Invalid choice. Please enter 1-4.")
        except ValueError:
            print("Please enter a valid number.")

def english_to_leetspeak(message, conversion_rate=0.7, preserve_case=True):
    result = ''
    for char in message:
        lower_char = char.lower()
        if lower_char in CHAR_MAPPINGS and random.random() <= conversion_rate:
            replacements = CHAR_MAPPINGS[lower_char]
            replacement = random.choice(replacements)
            
            if preserve_case and char.isupper():
                replacement = replacement.upper() if replacement.isalpha() else replacement
            
            result += replacement
        else:
            result += char
    return result

def leetspeak_to_english(leet_message):
    reverse_mapping = {}
    for char, leet_chars in CHAR_MAPPINGS.items():
        for leet_char in leet_chars:
            reverse_mapping[leet_char.lower()] = char
    
    result = ''
    i = 0
    while i < len(leet_message):
        found = False
        for length in range(4, 0, -1):
            if i + length <= len(leet_message):
                substring = leet_message[i:i + length].lower()
                if substring in reverse_mapping:
                    result += reverse_mapping[substring]
                    i += length
                    found = True
                    break
        if not found:
            result += leet_message[i]
            i += 1
    
    return result

def convert_single_text():
    message = input("\nEnter your message: ")
    if not message.strip():
        print("No message entered.")
        return
    
    conversion_rate = get_leet_level()
    
    preserve = input("\nPreserve original case? (y/n): ").lower() == 'y'
    
    leetspeak = english_to_leetspeak(message, conversion_rate, preserve)
    
    print(f"\nOriginal: {message}")
    print(f"L33tsp34k: {leetspeak}")
    
    if CLIPBOARD_AVAILABLE:
        try:
            pyperclip.copy(leetspeak)
            print("✓ Copied to clipboard!")
        except:
            print("✗ Could not copy to clipboard")
    
    save = input("\nSave to file? (y/n): ").lower() == 'y'
    if save:
        filename = input("Enter filename (or press Enter for 'output.txt'): ").strip()
        if not filename:
            filename = 'output.txt'
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"Original: {message}\n")
                f.write(f"L33tsp34k: {leetspeak}\n")
            print(f"✓ Saved to {filename}")
        except Exception as e:
            print(f"✗ Error saving file: {e}")

def batch_convert_file():
    filename = input("\nEnter input filename: ").strip()
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("File not found!")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    conversion_rate = get_leet_level()
    
    output_filename = input("Enter output filename (or press Enter for 'leetspeak_output.txt'): ").strip()
    if not output_filename:
        output_filename = 'leetspeak_output.txt'
    
    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            for i, line in enumerate(lines):
                original = line.strip()
                if original:
                    converted = english_to_leetspeak(original, conversion_rate)
                    f.write(f"Line {i+1}:\n")
                    f.write(f"Original: {original}\n")
                    f.write(f"L33tsp34k: {converted}\n\n")
        
        print(f"✓ Batch conversion complete! Output saved to {output_filename}")
    except Exception as e:
        print(f"✗ Error writing output file: {e}")

def interactive_mode():
    clear_screen()
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 12 + "1NT3R4CT1V3 L33T M0D3" + " " * 17 + "║")
    print("╚" + "═" * 50 + "╝")
    print("\nType messages to convert (type 'quit' to exit):")
    
    conversion_rate = get_leet_level()
    
    while True:
        message = input("\n> ")
        if message.lower() in ['quit', 'exit', 'q']:
            break
        
        if message.strip():
            leetspeak = english_to_leetspeak(message, conversion_rate)
            print(f"L33t: {leetspeak}")

def reverse_leetspeak():
    leet_message = input("\nEnter leetspeak to decode: ")
    if not leet_message.strip():
        print("No message entered.")
        return
    
    decoded = leetspeak_to_english(leet_message)
    
    print(f"\nL33tsp34k: {leet_message}")
    print(f"Decoded: {decoded}")
    
    if CLIPBOARD_AVAILABLE:
        try:
            pyperclip.copy(decoded)
            print("✓ Decoded text copied to clipboard!")
        except:
            print("✗ Could not copy to clipboard")

def main():
    while True:
        display_menu()
        
        try:
            choice = int(input("\nEnter your choice (1-5): "))
            
            if choice == 1:
                convert_single_text()
            elif choice == 2:
                batch_convert_file()
            elif choice == 3:
                interactive_mode()
            elif choice == 4:
                reverse_leetspeak()
            elif choice == 5:
                clear_screen()
                print("7h4nk y0u f0r u51n9 L33T 5P34K!")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1-5.")
            
            input("\nPress Enter to continue...")
            
        except ValueError:
            print("Please enter a valid number.")
            input("\nPress Enter to continue...")
        except KeyboardInterrupt:
            clear_screen()
            print("\nGoodbye!")
            sys.exit()

if __name__ == '__main__':
    main()
