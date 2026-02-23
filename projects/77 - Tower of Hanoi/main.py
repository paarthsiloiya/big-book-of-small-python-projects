import sys

TOTAL_DISKS = 5

def print_towers(towers):
    for level in range(TOTAL_DISKS - 1, -1, -1):
        for name in 'ABC':
            if level < len(towers[name]):
                disk = towers[name][level]
                disk_str = f"{'=' * disk}|{'=' * disk}"
                print(disk_str.center(TOTAL_DISKS * 2 + 2), end='')
            else:
                print('|'.center(TOTAL_DISKS * 2 + 2), end='')
        print()
    
    labels = [f" {name}" for name in 'ABC']
    print("".join(label.center(TOTAL_DISKS * 2 + 2) for label in labels))
    print()

def get_move(towers):
    while True:
        move = input('\nEnter move (e.g. AB) or QUIT: ').upper().strip()
        if move == 'QUIT':
            sys.exit()
        
        if len(move) != 2 or move[0] not in 'ABC' or move[1] not in 'ABC':
            print('Invalid input. Enter two tower letters like AB.')
            continue
            
        src, dest = move[0], move[1]
        
        if not towers[src]:
            print('Source tower is empty.')
        elif towers[dest] and towers[dest][-1] < towers[src][-1]:
            print('Cannot place a larger disk on a smaller one.')
        else:
            return src, dest

def main():
    print('Tower of Hanoi')
    print('Move the stack of disks from A to C following the rules.\n')

    towers = {
        'A': list(range(TOTAL_DISKS, 0, -1)),
        'B': [],
        'C': []
    }

    while True:
        print_towers(towers)

        if len(towers['C']) == TOTAL_DISKS:
            print('Congratulations! You solved the puzzle!')
            break
            
        src, dest = get_move(towers)
        disk = towers[src].pop()
        towers[dest].append(disk)

if __name__ == '__main__':
    main()
