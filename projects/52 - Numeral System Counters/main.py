import sys
import time

def to_roman(num):
    if num <= 0 or num >= 4000:
        return "N/A"
    
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    
    result = ""
    for i in range(len(values)):
        count = num // values[i]
        result += symbols[i] * count
        num -= values[i] * count
    return result

def to_base(num, base):
    if num == 0:
        return "0"
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    
    while num > 0:
        result = digits[num % base] + result
        num //= base
    
    return result

def format_with_separators(num_str, separator=' '):
    return separator.join(num_str[i:i+4] for i in range(0, len(num_str), 4))

def get_input():
    while True:
        try:
            start_input = input('Enter starting number (default 0): ').strip()
            start = int(start_input) if start_input else 0
            
            if start < 0:
                print('Please enter a non-negative number.')
                continue
            
            count_input = input('Enter count (default 1000): ').strip()
            count = int(count_input) if count_input else 1000
            
            if count <= 0:
                print('Please enter a positive count.')
                continue
            
            bases_input = input('Enter number bases (2-36, comma-separated, default 2,8,16): ').strip()
            if bases_input:
                bases = [int(b.strip()) for b in bases_input.split(',')]
                for base in bases:
                    if base < 2 or base > 36:
                        print('Bases must be between 2 and 36.')
                        raise ValueError
            else:
                bases = [2, 8, 16]
            
            options = {}
            options['roman'] = input('Show Roman numerals? (y/n, default n): ').lower().startswith('y')
            options['separators'] = input('Use digit separators? (y/n, default y): ').lower() != 'n'
            options['delay'] = input('Add delay between numbers? (y/n, default n): ').lower().startswith('y')
            
            if options['delay']:
                delay_input = input('Delay in seconds (default 0.1): ').strip()
                options['delay_time'] = float(delay_input) if delay_input else 0.1
            else:
                options['delay_time'] = 0
            
            return start, count, bases, options
            
        except ValueError:
            print('Please enter valid numbers.')
        except KeyboardInterrupt:
            sys.exit()

def display_number(num, bases, options):
    line = f"DEC: {num:>8}"
    
    for base in bases:
        base_str = to_base(num, base)
        if options['separators'] and len(base_str) > 4:
            base_str = format_with_separators(base_str)
        
        if base == 2:
            line += f"   BIN: {base_str:>15}"
        elif base == 8:
            line += f"   OCT: {base_str:>8}"
        elif base == 16:
            line += f"   HEX: {base_str:>8}"
        else:
            line += f"   B{base}: {base_str:>8}"
    
    if options['roman']:
        roman = to_roman(num)
        line += f"   ROM: {roman:>8}"
    
    print(line)

def save_to_file(start, count, bases, options):
    try:
        filename = f"numeral_systems_{start}_{start+count-1}.txt"
        with open(filename, 'w') as f:
            f.write(f"Numeral Systems Output\n")
            f.write(f"Range: {start} to {start+count-1}\n")
            f.write(f"Bases: {', '.join(map(str, bases))}\n")
            if options['roman']:
                f.write("Including Roman numerals\n")
            f.write("=" * 60 + "\n\n")
            
            for num in range(start, start + count):
                line = f"DEC: {num:>8}"
                
                for base in bases:
                    base_str = to_base(num, base)
                    if options['separators'] and len(base_str) > 4:
                        base_str = format_with_separators(base_str)
                    
                    if base == 2:
                        line += f"   BIN: {base_str:>15}"
                    elif base == 8:
                        line += f"   OCT: {base_str:>8}"
                    elif base == 16:
                        line += f"   HEX: {base_str:>8}"
                    else:
                        line += f"   B{base}: {base_str:>8}"
                
                if options['roman']:
                    roman = to_roman(num)
                    line += f"   ROM: {roman:>8}"
                
                f.write(line + '\n')
        
        print(f'\nSaved to {filename}')
        
    except Exception as e:
        print(f'Error saving file: {e}')

def main():
    print('Numeral System Counters')
    print('Shows numbers in different bases with optional features.')
    print('(Ctrl-C to quit)\n')
    
    start, count, bases, options = get_input()
    
    print(f'\nDisplaying {count} numbers starting from {start}')
    if bases != [2, 8, 16]:
        print(f'Using bases: {", ".join(map(str, bases))}')
    
    try:
        for i, num in enumerate(range(start, start + count)):
            display_number(num, bases, options)
            
            if options['delay_time'] > 0:
                time.sleep(options['delay_time'])
            
            if (i + 1) % 50 == 0:
                choice = input(f'\nDisplayed {i + 1} numbers. Continue? (y/n/s to save): ').lower()
                if choice == 'n':
                    break
                elif choice == 's':
                    save_to_file(start, i + 1, bases, options)
                    break
    
    except KeyboardInterrupt:
        print(f'\n\nStopped at number {num}')
        choice = input('Save current progress? (y/n): ').lower()
        if choice == 'y':
            displayed_count = num - start + 1
            save_to_file(start, displayed_count, bases, options)

if __name__ == '__main__':
    main()