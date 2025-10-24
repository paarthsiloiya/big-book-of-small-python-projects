import random, sys, time, os

PAUSE = 0.1
DISPLAY_HEIGHT = 20

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
RESET = '\033[0m'

BASE_COLORS = {
    'A': RED,
    'T': GREEN,
    'C': YELLOW,
    'G': BLUE
}

DNA = [
'          #-#',
'         #{}-{}#',
'        #{}---{}#',
'       #{}-----{}#',
'      #{}-------{}#',
'      #{}-------{}#',
'       #{}-----{}#',
'        #{}---{}#',
'         #{}-{}#',
'          #-#',
'         #{}-{}#',
'        #{}---{}#',
'       #{}-----{}#',
'      #{}-------{}#',
'      #{}-------{}#',
'       #{}-----{}#',
'        #{}---{}#',
'         #{}-{}#'
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def goto(x, y):
    print(f'\033[{y};{x}H', end='', flush=True)

def hide_cursor():
    print('\033[?25l', end='', flush=True)

def show_cursor():
    print('\033[?25h', end='', flush=True)

try:
    print('Press Ctrl-C to quit...')
    time.sleep(2)
    clear_screen()
    hide_cursor()
    
    rowIndex = 0

    while True:
        for line_num in range(DISPLAY_HEIGHT):
            dna_index = (rowIndex + line_num) % len(DNA)
            goto(1, line_num + 1)
            
            if dna_index == 0 or dna_index == 9:
                print(DNA[dna_index] + ' ' * 10)
            else:
                pairing = random.choice([('A', 'T'), ('T', 'A'), ('C', 'G'), ('G', 'C')])
                base1, base2 = pairing
                color1 = BASE_COLORS[base1]
                color2 = BASE_COLORS[base2]
                colored_base1 = f"{color1}{base1}{RESET}"
                colored_base2 = f"{color2}{base2}{RESET}"
                print(DNA[dna_index].format(colored_base1, colored_base2) + ' ' * 10)
        
        rowIndex = (rowIndex + 1) % len(DNA)
        time.sleep(PAUSE)

except KeyboardInterrupt:
    clear_screen()
    show_cursor()
    sys.exit()
