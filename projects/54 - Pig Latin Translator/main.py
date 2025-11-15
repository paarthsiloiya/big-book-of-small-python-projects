import os
import sys

try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')
CONSONANTS = 'bcdfghjklmnpqrstvwxz'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def english_to_pig_latin(message):
    pig_latin = ''
    for word in message.split():
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        
        if len(word) == 0:
            pig_latin += prefix_non_letters + ' '
            continue

        suffix_non_letters = ''
        while len(word) > 0 and not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]
        
        if len(word) == 0:
            pig_latin += prefix_non_letters + suffix_non_letters + ' '
            continue

        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower()

        prefix_consonants = ''
        while len(word) > 0 and word[0] not in VOWELS:
            prefix_consonants += word[0]
            word = word[1:]

        if prefix_consonants != '':
            word += prefix_consonants + 'ay'
        else:
            word += 'way'

        if was_upper:
            word = word.upper()
        elif was_title:
            word = word.title()

        pig_latin += prefix_non_letters + word + suffix_non_letters + ' '
    
    return pig_latin.strip()

def pig_latin_to_english(message):
    english = ''
    for word in message.split():
        prefix_non_letters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefix_non_letters += word[0]
            word = word[1:]
        
        if len(word) == 0:
            english += prefix_non_letters + ' '
            continue

        suffix_non_letters = ''
        while len(word) > 0 and not word[-1].isalpha():
            suffix_non_letters = word[-1] + suffix_non_letters
            word = word[:-1]
        
        if len(word) == 0:
            english += prefix_non_letters + suffix_non_letters + ' '
            continue

        was_upper = word.isupper()
        was_title = word.istitle()
        word = word.lower()

        if word.endswith('way') and len(word) > 3:
            original_word = word[:-3]
        elif word.endswith('ay') and len(word) > 2:
            ay_index = word.rfind('ay')
            if ay_index > 0:
                consonants = word[ay_index-len(word[:-2]):ay_index]
                original_word = consonants + word[:ay_index-len(consonants)]
            else:
                original_word = word
        else:
            original_word = word

        if was_upper:
            original_word = original_word.upper()
        elif was_title:
            original_word = original_word.title()

        english += prefix_non_letters + original_word + suffix_non_letters + ' '
    
    return english.strip()

def display_menu():
    print("🐷 PIG LATIN TRANSLATOR 🐷")
    print("=" * 40)
    print("1. English → Pig Latin")
    print("2. Pig Latin → English")
    print("3. Batch File Translation")
    print("4. Language Rules Help")
    print("5. Translation History")
    print("6. Clear Screen")
    print("0. Quit")
    print("-" * 40)

def show_rules():
    print("\n📖 PIG LATIN RULES:")
    print("=" * 40)
    print("🔸 Words starting with vowels: add 'way'")
    print("   Example: apple → appleway")
    print()
    print("🔸 Words starting with consonants: move consonants to end + 'ay'")
    print("   Example: hello → ellohay")
    print("   Example: string → ingstray")
    print()
    print("🔸 Capitalization and punctuation preserved")
    print("   Example: Hello! → Ellohay!")
    print("=" * 40)

def translate_file():
    filename = input("📁 Enter filename to translate: ").strip()
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found!")
        return
    
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
        
        mode = input("Translate to (1) Pig Latin or (2) English? ").strip()
        
        if mode == '1':
            translated = english_to_pig_latin(content)
            output_file = filename.rsplit('.', 1)[0] + '_piglatin.txt'
        else:
            translated = pig_latin_to_english(content)
            output_file = filename.rsplit('.', 1)[0] + '_english.txt'
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(translated)
        
        print(f"✅ Translation saved to '{output_file}'")
        
    except Exception as e:
        print(f"❌ Error processing file: {e}")

def main():
    translation_history = []
    
    while True:
        display_menu()
        choice = input("🔍 Enter choice: ").strip()
        
        if choice == '0' or choice.lower() == 'quit':
            print("🐷 Oodgay Yebay! (Good Bye!)")
            break
        
        elif choice == '1':
            print("\n📝 ENGLISH TO PIG LATIN")
            print("-" * 30)
            message = input("Enter English text: ")
            if message.strip():
                result = english_to_pig_latin(message)
                print(f"\n🐷 Pig Latin: {result}")
                
                translation_history.append({
                    'original': message,
                    'translated': result,
                    'direction': 'EN→PL'
                })
                
                if CLIPBOARD_AVAILABLE:
                    try:
                        pyperclip.copy(result)
                        print("📋 Copied to clipboard!")
                    except:
                        pass
                
                input("\n⏎ Press Enter to continue...")
        
        elif choice == '2':
            print("\n📝 PIG LATIN TO ENGLISH")
            print("-" * 30)
            message = input("Enter Pig Latin text: ")
            if message.strip():
                result = pig_latin_to_english(message)
                print(f"\n🔤 English: {result}")
                
                translation_history.append({
                    'original': message,
                    'translated': result,
                    'direction': 'PL→EN'
                })
                
                if CLIPBOARD_AVAILABLE:
                    try:
                        pyperclip.copy(result)
                        print("📋 Copied to clipboard!")
                    except:
                        pass
                
                input("\n⏎ Press Enter to continue...")
        
        elif choice == '3':
            translate_file()
            input("\n⏎ Press Enter to continue...")
        
        elif choice == '4':
            show_rules()
            input("\n⏎ Press Enter to continue...")
        
        elif choice == '5':
            print("\n📚 TRANSLATION HISTORY")
            print("=" * 50)
            if translation_history:
                for i, trans in enumerate(translation_history[-10:], 1):
                    print(f"{i}. [{trans['direction']}] {trans['original'][:30]}...")
                    print(f"   → {trans['translated'][:30]}...")
                    print()
            else:
                print("No translations yet.")
            input("\n⏎ Press Enter to continue...")
        
        elif choice == '6':
            clear_screen()
        
        else:
            print("❌ Invalid choice. Please try again.")
            input("⏎ Press Enter to continue...")

if __name__ == '__main__':
    main()