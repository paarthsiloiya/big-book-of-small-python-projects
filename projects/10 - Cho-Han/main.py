import random, sys

JAP_NUM_MAP = {1:'ICHI', 2:'NI', 3:'SAN', 4:'SHI', 5:'GO', 6:'ROKU'}

purse = 5000

while True:
    print(f"\nYou have ¥{purse}.")
    while True:
        bet = input("Enter your bet amount (or 'q' to quit): ")
        if bet.lower() == 'q':
            print("Thanks for playing!")
            sys.exit()

        try:
            bet = int(bet)
            if 1 <= bet <= purse:
                break
            else:
                print(f"Bet must be between 1 and ¥{purse}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    d1, d2 = random.randint(1, 6), random.randint(1, 6)
    total = d1 + d2

    while True:
        player_guess = input("Enter your guess (cho[even]/han[odd]): ")
        if player_guess.lower() in ['cho', 'han']:
            break
        else:
            print("Invalid guess. Please enter 'cho' or 'han'.")

    print(f"\nThe dealer rolls the dice...")
    print(f"The dealer rolled {JAP_NUM_MAP[d1]}({d1}) and {JAP_NUM_MAP[d2]}({d2}).")
    print(f"The total is {total}.")

    if (total % 2 == 0 and player_guess.lower() == 'cho') or (total % 2 == 1 and player_guess.lower() == 'han'):
        print(f"You guessed {player_guess}, and the total is {total}. You win ¥{bet}!")
        purse += bet
        print("A house fee of 10% is deducted")
        purse -= bet // 10
        print(f"Your new balance is ¥{purse}.")
    else:
        print(f"You guessed {player_guess}, and the total is {total}. You lose ¥{bet}.")
        purse -= bet

    if purse <= 0:
        print("You're out of money! Game over.")
        sys.exit()