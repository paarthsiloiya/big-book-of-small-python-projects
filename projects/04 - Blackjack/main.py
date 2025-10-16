HEARTS = "♥"
DIAMONDS = "♦"
SPADES = "♠"
CLUBS = "♣"

CARD_TEMPLATE = """
┌─────────┐
│{rank:<2}       │
│         │
│    {suit}    │
│         │
│       {rank:>2}│
└─────────┘
"""

def render_card(rank, suit):
    return CARD_TEMPLATE.format(rank=rank, suit=suit)

MIN_BET, MAX_BET, INITIAL_BALANCE = 2, 1000, 400
NUMBER_OF_DECKS = 6

current_balance = INITIAL_BALANCE

def getDeck():
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = [HEARTS, DIAMONDS, SPADES, CLUBS]
    deck = []
    for _ in range(NUMBER_OF_DECKS):
        for suit in suits:
            for rank in ranks:
                deck.append((rank, suit))
    import random
    random.shuffle(deck)
    return deck


def displayHands(dealer_hand, player_hand, show_dealer_card):
    print("\nDealer's hand:")
    if show_dealer_card:
        display_cards_side_by_side([render_card(rank, suit) for rank, suit in dealer_hand])
    else:
        cards_to_show = [render_card(dealer_hand[0][0], dealer_hand[0][1]), render_card("?", "?")]
        display_cards_side_by_side(cards_to_show)
    
    print(f"Dealer's hand value: {getHandValue(dealer_hand) if show_dealer_card else '?'}")
    
    print("\nYour hand:")
    display_cards_side_by_side([render_card(rank, suit) for rank, suit in player_hand])
    print(f"Your hand value: {getHandValue(player_hand)}")

def display_cards_side_by_side(card_strings):
    if not card_strings:
        return
    
    card_lines = [card.split('\n') for card in card_strings]
    
    lines_per_card = len(card_lines[0])
    
    for line_num in range(lines_per_card):
        line_parts = []
        for card in card_lines:
            if line_num < len(card):
                line_parts.append(card[line_num])
            else:
                line_parts.append(' ' * 11)
        print(' '.join(line_parts))


def getHandValue(hand):
    value = 0
    aces = 0
    for rank, _ in hand:
        if rank in ['J', 'Q', 'K']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value



while True:
    print(f"\nCurrent balance: ${current_balance}")
    while True:
        try:
            bet = int(input(f"Enter your bet (${MIN_BET}-${MAX_BET}): "))
            if MIN_BET <= bet <= MAX_BET and bet <= current_balance:
                break
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}, and not exceed your balance.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    deck = getDeck()

    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]

    displayHands(dealer_hand, player_hand, show_dealer_card=False)

    player_value = getHandValue(player_hand)
    dealer_value = getHandValue(dealer_hand)
    
    if player_value == 21 and len(player_hand) == 2:
        if dealer_value == 21 and len(dealer_hand) == 2:
            print("Both have blackjack! It's a tie!")
            displayHands(dealer_hand, player_hand, show_dealer_card=True)
        else:
            print("Blackjack! You win!")
            displayHands(dealer_hand, player_hand, show_dealer_card=True)
            current_balance += int(bet * 1.5)  # Blackjack pays 3:2
        continue

    game_over = False
    while not game_over:
        action = input("\nDo you want to (h)it, (s)tand or (d)ouble down? ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            displayHands(dealer_hand, player_hand, show_dealer_card=False)
            if getHandValue(player_hand) > 21:
                print("You busted! Dealer wins.")
                current_balance -= bet
                game_over = True
        elif action == 's':
            while getHandValue(dealer_hand) < 17:
                dealer_hand.append(deck.pop())
            displayHands(dealer_hand, player_hand, show_dealer_card=True)
            dealer_value = getHandValue(dealer_hand)
            player_value = getHandValue(player_hand)
            if dealer_value > 21:
                print("Dealer busted! You win!")
                current_balance += bet
            elif player_value > dealer_value:
                print("You win!")
                current_balance += bet
            elif player_value < dealer_value:
                print("Dealer wins!")
                current_balance -= bet
            else:
                print("It's a tie!")
            game_over = True
        elif action == 'd':
            if current_balance >= bet * 2:
                bet *= 2
                player_hand.append(deck.pop())
                displayHands(dealer_hand, player_hand, show_dealer_card=False)
                if getHandValue(player_hand) > 21:
                    print("You busted! Dealer wins.")
                    current_balance -= bet
                else:
                    while getHandValue(dealer_hand) < 17:
                        dealer_hand.append(deck.pop())
                    displayHands(dealer_hand, player_hand, show_dealer_card=True)
                    dealer_value = getHandValue(dealer_hand)
                    player_value = getHandValue(player_hand)
                    if dealer_value > 21:
                        print("Dealer busted! You win!")
                        current_balance += bet
                    elif player_value > dealer_value:
                        print("You win!")
                        current_balance += bet
                    elif player_value < dealer_value:
                        print("Dealer wins!")
                        current_balance -= bet
                    else:
                        print("It's a tie!")
                game_over = True
            else:
                print("Insufficient balance to double down.")
        else:
            print("Invalid input. Please enter 'h', 's' or 'd'.")
    
    if current_balance < MIN_BET:
        print("You are out of money! Game over.")
        break
    
    print(f"Your current balance is: ${current_balance}")
    if input("Do you want to play another round? (y/n): ").lower() != 'y':
        print("Thanks for playing! Goodbye.")
        break
