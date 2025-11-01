import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    print("I'm thinking of a number between 1 and 100.")
    
    number_to_guess = random.randint(1, 100)
    number_of_guesses = 0
    max_guesses = 10

    while number_of_guesses < max_guesses:
        guess = input(f"Guess #{number_of_guesses + 1}: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        number_of_guesses += 1

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {number_to_guess} in {number_of_guesses} tries!")
            break
    else:
        print(f"Sorry, you've used all your guesses. The number was {number_to_guess}.")