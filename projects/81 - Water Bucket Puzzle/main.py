import sys

GOAL = 4
CAPACITIES = {'8': 8, '5': 5, '3': 3}
buckets = {'8': 0, '5': 0, '3': 0}
steps = 0

def display_buckets():
    display = []
    for b in ['8', '5', '3']:
        for i in range(1, CAPACITIES[b] + 1):
            display.append('WWWWWW' if buckets[b] >= i else '      ')
    
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*display))

def main():
    global steps
    print('Water Bucket Puzzle')
    
    while True:
        display_buckets()
        
        if any(amount == GOAL for amount in buckets.values()):
            print(f'Good job! You solved it in {steps} steps!')
            sys.exit()
            
        print(f'Try to get {GOAL}L of water into one of these buckets:')
        print('You can:\n  (F)ill the bucket\n  (E)mpty the bucket\n  (P)our one bucket into another\n  (Q)uit')
        
        while True:
            move = input('> ').upper()
            if move in ('Q', 'QUIT'):
                sys.exit()
            if move in ('F', 'E', 'P'):
                break
        
        while True:
            src = input('Select a bucket 8, 5, 3:\n> ').upper()
            if src in CAPACITIES:
                break

        if move == 'F':
            buckets[src] = CAPACITIES[src]
            steps += 1
        elif move == 'E':
            buckets[src] = 0
            steps += 1
        elif move == 'P':
            while True:
                dst = input('Select a bucket to pour into: 8, 5, or 3\n> ').upper()
                if dst in CAPACITIES and src != dst:
                    break
            
            amount = min(CAPACITIES[dst] - buckets[dst], buckets[src])
            buckets[src] -= amount
            buckets[dst] += amount
            steps += 1

if __name__ == '__main__':
    main()