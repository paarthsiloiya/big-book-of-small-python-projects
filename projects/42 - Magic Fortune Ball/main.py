import random
import time
import os
import sys

FORTUNE_THEMES = {
    'CLASSIC': {
        'name': 'Classic Magic 8-Ball',
        'replies': [
            'LET ME THINK ON THIS...',
            'AN INTERESTING QUESTION...',
            'HMMM... ARE YOU SURE YOU WANT TO KNOW..?',
            'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
            'I SHALL CONSULT MY VISIONS...'
        ],
        'answers': [
            'YES, FOR SURE',
            'MY ANSWER IS NO', 
            'ASK ME LATER',
            'FOCUS AND ASK ONCE MORE',
            'DOUBTFUL, VERY DOUBTFUL',
            'AFFIRMATIVE',
            'YES, THOUGH YOU MAY NOT LIKE IT',
            'NO, BUT YOU MAY WISH IT WAS SO'
        ]
    },
    'MYSTICAL': {
        'name': 'Mystical Oracle',
        'replies': [
            'THE SPIRITS ARE GATHERING...',
            'THE CRYSTAL BALL GROWS CLOUDY...',
            'ANCIENT WISDOM STIRS WITHIN...',
            'THE UNIVERSE WHISPERS TO ME...',
            'COSMIC FORCES ALIGN FOR YOUR ANSWER...'
        ],
        'answers': [
            'THE STARS ALIGN IN YOUR FAVOR',
            'DARKNESS CLOUDS YOUR PATH',
            'THE MOON SAYS WAIT',
            'DESTINY CALLS WITH A YES',
            'THE VOID SPEAKS OF UNCERTAINTY',
            'CELESTIAL POWERS SAY NO',
            'YOUR FUTURE SHINES BRIGHT',
            'THE ORACLE REMAINS SILENT'
        ]
    },
    'HUMOROUS': {
        'name': 'Sarcastic Fortune Teller',
        'replies': [
            'OH, ANOTHER LIFE CRISIS...',
            'LET ME GUESS, ROMANCE TROUBLES..?',
            'SERIOUSLY? THIS IS YOUR BIG QUESTION..?',
            'I SUPPOSE I HAVE TO ANSWER...',
            'FINE, BUT DON\'T BLAME ME LATER...'
        ],
        'answers': [
            'OBVIOUSLY YES, DUH',
            'NO WAY, JOSE',
            'MAYBE IF YOU\'RE LUCKY',
            'ASK YOUR MOM INSTEAD',
            'FLIP A COIN, SAME ACCURACY',
            'YES, BUT I\'M PROBABLY WRONG',
            'NO, AND I\'M DEFINITELY RIGHT',
            'OUTLOOK NOT SO GOOD, BUDDY'
        ]
    },
    'TECH': {
        'name': 'AI Fortune Module',
        'replies': [
            'PROCESSING YOUR QUERY...',
            'SCANNING PROBABILITY MATRICES...',
            'RUNNING FORTUNE ALGORITHMS...',
            'ACCESSING FUTURE DATABASE...',
            'COMPUTING DESTINY VARIABLES...'
        ],
        'answers': [
            'PROBABILITY: 99.9% YES',
            'ERROR 404: FORTUNE NOT FOUND',
            'SYSTEM SAYS: NEGATIVE',
            'PROCESSING... RESULT: AFFIRMATIVE',
            'BUFFER OVERFLOW: TRY AGAIN',
            'QUANTUM ANALYSIS: UNCERTAIN',
            'BOOLEAN RESULT: TRUE',
            'COMPILATION ERROR: ASK LATER'
        ]
    }
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_space_print(text, interval=0.1):
    for character in text:
        if character == 'I':
            print('i ', end='', flush=True)
        else:
            print(character + ' ', end='', flush=True)
        time.sleep(interval)
    print()
    print()

def select_theme():
    clear_screen()
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 18 + "🔮 MAGIC FORTUNE BALL 🔮" + " " * 16 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\nSelect your fortune telling experience:")
    
    themes = list(FORTUNE_THEMES.keys())
    for i, theme_key in enumerate(themes, 1):
        theme_name = FORTUNE_THEMES[theme_key]['name']
        print(f"{i}. {theme_name}")
    
    while True:
        try:
            choice = int(input(f"\nChoose theme (1-{len(themes)}): "))
            if 1 <= choice <= len(themes):
                return themes[choice - 1]
        except ValueError:
            pass
        print("Invalid choice. Please try again.")

def display_crystal_ball_animation():
    frames = [
        "     ✨ ○ ✨        ",
        "   ✨ ◐ ○ ◑ ✨     ",
        " ✨ ◐ ● ○ ● ◑ ✨   ",
        "✨ ◐ ● ◉ ○ ◉ ● ◑ ✨",
        " ✨ ◑ ● ○ ● ◐ ✨   ",
        "   ✨ ◑ ○ ◐ ✨     ",
        "     ✨ ○ ✨        "
    ]
    
    for _ in range(3):
        for frame in frames:
            print(f"\r{frame}", end='', flush=True)
            time.sleep(0.3)
    print()

def get_question():
    questions_asked = []
    
    while True:
        clear_screen()
        print("🔮 " + "═" * 50 + " 🔮")
        print("     ASK YOUR YES/NO QUESTION ABOUT THE FUTURE")
        print("🔮 " + "═" * 50 + " 🔮")
        
        if questions_asked:
            print(f"\n📜 Previous questions asked: {len(questions_asked)}")
            if len(questions_asked) >= 3:
                print("💭 The spirits grow weary... perhaps take a break?")
        
        question = input('\n> ').strip()
        
        if not question:
            print("The fortune ball requires a question to divine your future!")
            time.sleep(2)
            continue
        
        if question.lower() in ['quit', 'exit', 'bye']:
            return None, questions_asked
        
        if question in questions_asked:
            print("🔄 You've asked this before! The answer remains the same...")
            time.sleep(2)
            continue
        
        questions_asked.append(question)
        return question, questions_asked

def fortune_session():
    theme_key = select_theme()
    theme = FORTUNE_THEMES[theme_key]
    questions_asked = []
    
    while True:
        question, questions_asked = get_question()
        
        if question is None:
            break
        
        clear_screen()
        print("🔮 " + theme['name'].upper() + " 🔮")
        print("═" * 60)
        
        slow_space_print(random.choice(theme['replies']))
        
        display_crystal_ball_animation()
        
        slow_space_print('.' * random.randint(4, 12), 0.7)
        
        slow_space_print('I HAVE AN ANSWER...', 0.2)
        time.sleep(1)
        
        answer = random.choice(theme['answers'])
        slow_space_print(answer, 0.05)
        
        confidence = random.randint(60, 99)
        print(f"✨ Mystical Confidence Level: {confidence}% ✨")
        
        print("\n" + "═" * 60)
        choice = input("Ask another question? (y/n/change theme): ").lower()
        
        if choice.startswith('n') or choice in ['quit', 'exit']:
            break
        elif choice.startswith('c'):
            theme_key = select_theme()
            theme = FORTUNE_THEMES[theme_key]

def main():
    try:
        clear_screen()
        print("🌟 Welcome to the Enhanced Magic Fortune Ball! 🌟")
        print("Ask yes/no questions and receive mystical guidance...")
        print("\nType 'quit' at any time to exit.")
        input("\nPress Enter to begin your fortune telling journey...")
        
        fortune_session()
        
        clear_screen()
        print("🔮 " + "═" * 40 + " 🔮")
        print("   Thank you for consulting the Fortune Ball!")
        print("      May your future be bright! ✨")
        print("🔮 " + "═" * 40 + " 🔮")
        
    except KeyboardInterrupt:
        clear_screen()
        print("\n🔮 The spirits have departed... Goodbye! ✨")

if __name__ == '__main__':
    main()