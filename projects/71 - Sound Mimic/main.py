import random, sys, time, os

try:
    import winsound
except ImportError:
    winsound = None

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Sound Mimic')
    print('Memorize the pattern of A S D F.')
    input('Press Enter to begin...')

    pattern = ''
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        pattern += random.choice('ASDF')
        
        print('Pattern:', end=' ', flush=True)
        for char in pattern:
            print(char, end=' ', flush=True)
            play_sound(char)
            time.sleep(0.2)
        
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        
        print('Enter the pattern:')
        response = input('> ').upper().strip()
        
        if response != pattern:
            print('Game Over!')
            print(f'The pattern was: {pattern}')
            print(f'Score: {len(pattern)-1}')
            break
        
        print('Correct!')
        time.sleep(1)

def play_sound(char):
    freqs = {'A': 440, 'S': 494, 'D': 554, 'F': 587}
    if winsound:
        winsound.Beep(freqs.get(char, 440), 400)
    else:
        time.sleep(0.4)

if __name__ == '__main__':
    main()
