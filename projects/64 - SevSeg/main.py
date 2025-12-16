DIGITS = {
    '0': (' __ ', '|  |', '|__|'),
    '1': ('    ', '   |', '   |'),
    '2': (' __ ', ' __|', '|__ '),
    '3': (' __ ', ' __|', ' __|'),
    '4': ('    ', '|__|', '   |'),
    '5': (' __ ', '|__ ', ' __|'),
    '6': (' __ ', '|__ ', '|__|'),
    '7': (' __ ', '   |', '   |'),
    '8': (' __ ', '|__|', '|__|'),
    '9': (' __ ', '|__|', ' __|'),
    'A': (' __ ', '|__|', '|  |'),
    'B': ('    ', '|__ ', '|__|'),
    'b': ('    ', '|__ ', '|__|'),
    'C': (' __ ', '|  ', '|__ '),
    'D': ('    ', ' __|', '|__|'),
    'd': ('    ', ' __|', '|__|'),
    'E': (' __ ', '|__ ', '|__ '),
    'F': (' __ ', '|__ ', '|__ '),
    '-': ('    ', ' __ ', '    '),
}

def get_sev_seg_str(number, min_width=0):
    number = str(number).zfill(min_width)
    rows = ['', '', '']
    
    for i, char in enumerate(number):
        if char == '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += '.'
            continue
            
        if char in DIGITS:
            pattern = DIGITS[char]
        elif char.upper() in DIGITS:
            pattern = DIGITS[char.upper()]
        else:
            pattern = ('    ', '  ? ', '    ')

        rows[0] += pattern[0]
        rows[1] += pattern[1]
        rows[2] += pattern[2]

        if i != len(number) - 1 and number[i + 1] != '.':
            rows[0] += ' '
            rows[1] += ' '
            rows[2] += ' '

    return '\n'.join(rows)

if __name__ == '__main__':
    print('Seven Segment Display Module')
    print('Enter a number to display (or QUIT):')
    
    while True:
        response = input('> ').upper()
        if response == 'QUIT':
            break
        try:
            print(get_sev_seg_str(response))
        except Exception as e:
            print(f"Error: {e}")
