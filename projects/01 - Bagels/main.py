TOP_DISPLAY= """
Welcome to the Bagels game!
============================

Instructions:
1. Think of a 3-digit number with no repeated digits.
2. The computer will try to guess your number.
3. After each guess, you will provide feedback in the form of:
   - "Bagels" if the guess has no correct digits.
   - "Pico" if the guess has a correct digit in the wrong position.
   - "Fermi" if the guess has a correct digit in the right position.
4. The game continues until the computer guesses your number.

Example:
If your number is 123 and the computer guesses 321, you would respond with "Pico" for the 3, "Fermi" for the 2, and "Pico" for the 1.

Good luck!
"""

print(TOP_DISPLAY)

NUM_DIGITS = 3 
MAX_GUESSES = 10

def getSecretNumber():
    import random
    secret_number = ""
    for i in random.sample('0123456789', NUM_DIGITS):
        secret_number += i
    return int(secret_number)


def getGuess(current_guess):
    while True:
        guess = input(f"Guess Number : {current_guess} > ").strip()
        if len(guess) != NUM_DIGITS or not guess.isdecimal():
            print(f"Please enter a {NUM_DIGITS}-digit number.")
        else:
            return guess


def getClues(guess, secret_number):
    if guess == str(secret_number).zfill(NUM_DIGITS):
        return "You got it!"

    clues = [""] * NUM_DIGITS
    guess_str = guess
    secret_str = str(secret_number).zfill(NUM_DIGITS)
    
    secret_used = [False] * NUM_DIGITS
    guess_used = [False] * NUM_DIGITS

    for i in range(NUM_DIGITS):
        if guess_str[i] == secret_str[i]:
            clues[i] = "Fermi"
            secret_used[i] = True
            guess_used[i] = True

    for i in range(NUM_DIGITS):
        if not guess_used[i]:
            for j in range(NUM_DIGITS):
                if not secret_used[j] and guess_str[i] == secret_str[j]:
                    clues[i] = "Pico"
                    secret_used[j] = True
                    break

    final_clues = [clue for clue in clues if clue]
    
    if not final_clues:
        return "Bagels"
    else:
        return ' '.join(final_clues)
    

while True:
    secret_number = getSecretNumber()
    print(f"I have thought up of a {NUM_DIGITS}-digit number.")
    print(f"You have {MAX_GUESSES} guesses to get it.")

    current_guess = 1
    while current_guess <= MAX_GUESSES:
        guess = getGuess(current_guess)
        clues = getClues(guess, secret_number)
        print(clues)
        current_guess += 1

        if guess == str(secret_number).zfill(NUM_DIGITS):
            break
        
        if current_guess > MAX_GUESSES:
            print("You ran out of guesses.")
            print(f"The answer was {secret_number}.")

    print("Do you want to play again? (yes/no)")
    if not input().lower().startswith('y'):
        break
    
print("Thank You for playing Bagels!")