import random
import time

HEARTS = chr(9829)
DIAMONDS = chr(9830)
SPADES = chr(9824)
CLUBS = chr(9827)

POSITIONS = ['LEFT', 'MIDDLE', 'RIGHT']

def get_random_card():
    while True:
        rank = random.choice(list('23456789JQKA') + ['10'])
        suit = random.choice([HEARTS, DIAMONDS, SPADES, CLUBS])
        if rank != 'Q' or suit != HEARTS:
            return (rank, suit)

def display_cards(cards):
    lines = ['', '', '', '', '']
    for rank, suit in cards:
        lines[0] += ' ___  '
        lines[1] += f'|{rank.ljust(2)} | '
        lines[2] += f'| {suit} | '
        lines[3] += f'|_{rank.rjust(2, "_")}| '
            
    for line in lines:
        print(line)

def main():
    print('Three-Card Monte\n')
    print('Find the red lady (the Queen of Hearts)! Keep an eye on the cards.\n')

    cards = [('Q', HEARTS), get_random_card(), get_random_card()]
    random.shuffle(cards)
    
    print('Here are the cards:')
    display_cards(cards)
    input('Press Enter when you are ready to begin...')

    for _ in range(16):
        positions = [0, 1, 2]
        idx1, idx2 = random.sample(positions, 2)
        print(f'Swapping {POSITIONS[idx1]} and {POSITIONS[idx2]}...')
        cards[idx1], cards[idx2] = cards[idx2], cards[idx1]
        time.sleep(0.8)

    print('\n' * 50)
    
    while True:
        print('Which card has the Queen of Hearts? (LEFT, MIDDLE, RIGHT)')
        guess = input('> ').upper().strip()
        if guess in POSITIONS:
            guess_index = POSITIONS.index(guess)
            break
    
    display_cards(cards)

    if cards[guess_index] == ('Q', HEARTS):
        print('You won!')
        print('Thanks for playing!')
    else:
        print('You lost!')
        print('Thanks for playing, sucker!')

if __name__ == '__main__':
    main()
