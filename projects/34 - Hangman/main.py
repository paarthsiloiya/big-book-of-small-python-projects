hangman_stages = ['''
  +---+
  |   |
  |   O
  |  /|\\
  |  / \\
  |
=========
''',
'''
  +---+
  |   |
  |   O
  |  /|\\
  |  /
  |
=========
''',
'''
  +---+
  |   |
  |   O
  |  /|
  |  /
  |
=========
''',
'''
  +---+
  |   |
  |   O
  |   |
  |  /
  |
=========
''',
'''
  +---+
  |   |
  |   O
  |   |
  |
  |
=========
''',
'''
  +---+
  |   |
  |   O
  |
  |
  |
=========
''',
'''
  +---+
  |   |
  |
  |
  |
  |
=========
'''][::-1]
def display_hangman(tries):
    return hangman_stages[tries]


def draw_hangman(missed_letters, correct_letters, secret_word):
    print(display_hangman(len(missed_letters)))
    print()

    print("Missed letters:", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=" ")
    print()
    print()

def getPlayerGuess(already_guessed):
    while True:
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1:
            print("Please enter a single letter.")
        elif guess in already_guessed:
            print("You have already guessed that letter. Choose again.")
        elif not guess.isalpha():
            print("Please enter a LETTER.")
        else:
            return guess

import os
import random

difficulty_levels = {
    'easy': 4,
    'medium': 5,
    'hard': 6
}

get_player_difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
player_difficulty = difficulty_levels.get(get_player_difficulty, 5)
word_list = open(os.path.join(os.path.dirname(__file__), f"wordlist-{player_difficulty}.txt")).read().splitlines()

missed_letters = []
correct_letters = []
secret_word = random.choice(word_list)

while True:
    draw_hangman(missed_letters, correct_letters, secret_word)

    guess = getPlayerGuess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters.append(guess)

        found_all_letters = True
        for letter in secret_word:
            if letter not in correct_letters:
                found_all_letters = False
                break
        if found_all_letters:
            print(f"Yes! The secret word is '{secret_word}'! You have won!")
            break
    else:
        missed_letters.append(guess)

        if len(missed_letters) == len(hangman_stages) - 1:
            draw_hangman(missed_letters, correct_letters, secret_word)
            print(f"You have run out of guesses!\nAfter {str(len(missed_letters))} missed guesses and {str(len(correct_letters))} correct guesses, the word was '{secret_word}'")
            break
