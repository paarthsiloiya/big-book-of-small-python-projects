import random, time, sys, os

MAX_SNAILS = 8
FINISH_LINE = 60

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Snail Race')
    
    while True:
        print(f'How many snails? (2-{MAX_SNAILS})')
        val = input('> ')
        if val.isdecimal() and 1 < int(val) <= MAX_SNAILS:
            num_snails = int(val)
            break
            
    names = []
    for i in range(num_snails):
        while True:
            print(f'Snail #{i+1} name:')
            name = input('> ').strip()
            if name and name not in names:
                names.append(name)
                break
    
    progress = {n: 0 for n in names}
    
    time.sleep(1)
    
    while True:
        for _ in range(random.randint(1, num_snails // 2)):
            mover = random.choice(names)
            progress[mover] += 1
            if progress[mover] >= FINISH_LINE:
                draw_track(names, progress)
                print(f'\n{mover} wins!')
                sys.exit()
                
        draw_track(names, progress)
        time.sleep(0.2)

def draw_track(names, progress):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('START' + ' ' * (FINISH_LINE - 5) + 'FINISH')
    print('│' + ' ' * (FINISH_LINE - 1) + '│')
    
    for name in names:
        pos = progress[name]
        print(' ' * pos + name)
        print('.' * pos + '@v')

if __name__ == '__main__':
    main()
