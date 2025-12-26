import os

NUMBER_OF_DIGITS = 10

def main():
    abacus_number = 0

    # Mapping keys to (digit_index, change_amount)
    # Index 0 is the leftmost digit (billions place)
    keys = {
        'q': (0, 1), 'a': (0, -1),
        'w': (1, 1), 's': (1, -1),
        'e': (2, 1), 'd': (2, -1),
        'r': (3, 1), 'f': (3, -1),
        't': (4, 1), 'g': (4, -1),
        'y': (5, 1), 'h': (5, -1),
        'u': (6, 1), 'j': (6, -1),
        'i': (7, 1), 'k': (7, -1),
        'o': (8, 1), 'l': (8, -1),
        'p': (9, 1), ';': (9, -1)
    }

    while True:
        display_abacus(abacus_number)
        print('\n  + q  w  e  r  t  y  u  i  o  p')
        print('  - a  s  d  f  g  h  j  k  l  ;')
        print('(Enter number, keys, or "quit")')
        
        command = input('> ').lower()
        
        if command == 'quit':
            break
        elif command.isdecimal():
            abacus_number = int(command)
        else:
            for char in command:
                if char in keys:
                    idx, change = keys[char]
                    # Calculate value of this digit position
                    power = NUMBER_OF_DIGITS - 1 - idx
                    abacus_number += change * (10 ** power)

        if abacus_number < 0:
            abacus_number = 0
        if abacus_number > 9999999999:
            abacus_number = 9999999999

def display_abacus(number):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    digits = [int(d) for d in str(number).zfill(NUMBER_OF_DIGITS)]
    
    # Build rows
    heaven_rows = [[], []]
    earth_rows = [[], [], [], [], []]
    
    for d in digits:
        # Heaven
        if d < 5:
            heaven_rows[0].append('O')
            heaven_rows[1].append('│')
        else:
            heaven_rows[0].append('│')
            heaven_rows[1].append('O')
            
        # Earth
        rem = d % 5
        for i in range(5):
            if i == rem:
                earth_rows[i].append('│')
            else:
                earth_rows[i].append('O')

    # Print
    print('Soroban - Japanese Abacus')
    print('┌' + '─' * (NUMBER_OF_DIGITS * 3 + 1) + '┐')
    
    # Heaven
    for row in heaven_rows:
        print('│ ' + '  '.join(row) + ' │')
        
    print('├' + '─' * (NUMBER_OF_DIGITS * 3 + 1) + '┤')
    
    # Earth
    for row in earth_rows:
        print('│ ' + '  '.join(row) + ' │')
        
    print('└' + '─' * (NUMBER_OF_DIGITS * 3 + 1) + '┘')
    
    # Digits
    digit_str = '  '.join(str(d) for d in digits)
    print('  ' + digit_str)

if __name__ == '__main__':
    main()
