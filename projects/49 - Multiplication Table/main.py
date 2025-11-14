import os
import sys

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_table_settings():
    while True:
        try:
            print('🔢 Table Configuration:')
            
            start_num = input('Start number (default 0): ').strip()
            start_num = int(start_num) if start_num else 0
            
            end_num = input('End number (default 12): ').strip()
            end_num = int(end_num) if end_num else 12
            
            if start_num > end_num:
                print('❌ Start number must be <= end number!')
                continue
            
            if end_num - start_num > 50:
                print('❌ Range too large! Maximum 50 numbers.')
                continue
            
            return start_num, end_num
        except ValueError:
            print('❌ Please enter valid numbers!')

def get_display_options():
    print('\n🎨 Display Options:')
    
    while True:
        highlight = input('Highlight perfect squares? (y/n, default n): ').lower().strip()
        if highlight in ['', 'n', 'no']:
            highlight = False
            break
        elif highlight in ['y', 'yes']:
            highlight = True
            break
        print('❌ Please enter y or n!')
    
    while True:
        show_colors = input('Show colored output? (y/n, default y): ').lower().strip()
        if show_colors in ['', 'y', 'yes']:
            show_colors = True
            break
        elif show_colors in ['n', 'no']:
            show_colors = False
            break
        print('❌ Please enter y or n!')
    
    while True:
        show_specific = input('Show specific multiplication (e.g., "5" for 5x table)? (Enter for full table): ').strip()
        if show_specific == '':
            show_specific = None
            break
        try:
            show_specific = int(show_specific)
            break
        except ValueError:
            print('❌ Please enter a valid number!')
    
    return highlight, show_colors, show_specific

def is_perfect_square(n):
    if n < 0:
        return False
    root = int(n ** 0.5)
    return root * root == n

def get_color_for_number(number, is_square, use_colors):
    if not use_colors:
        return ''
    
    if number == 0:
        return '\033[90m'
    elif is_square:
        return '\033[93m'
    elif number % 2 == 0:
        return '\033[94m'
    else:
        return '\033[92m'

def reset_color():
    return '\033[0m'

def format_number(num, width, is_square, use_colors):
    color = get_color_for_number(num, is_square, use_colors)
    reset = reset_color() if use_colors else ''
    
    if is_square and use_colors:
        return f'{color}{str(num).rjust(width)}²{reset}'
    else:
        return f'{color}{str(num).rjust(width)}{reset}'

def print_full_table(start, end, highlight_squares, use_colors):
    clear_screen()
    print('📊 MULTIPLICATION TABLE')
    print('=' * (6 + (end - start + 1) * 5))
    
    header = '   |'
    for col in range(start, end + 1):
        is_square = is_perfect_square(col) and highlight_squares
        formatted = format_number(col, 4, is_square, use_colors)
        header += f' {formatted}'
    print(header)
    
    separator = '---+' + '-----' * (end - start + 1)
    print(separator)
    
    for row in range(start, end + 1):
        row_is_square = is_perfect_square(row) and highlight_squares
        row_label = format_number(row, 2, row_is_square, use_colors)
        print(f'{row_label} |', end='')
        
        for col in range(start, end + 1):
            product = row * col
            product_is_square = is_perfect_square(product) and highlight_squares
            formatted = format_number(product, 4, product_is_square, use_colors)
            print(f' {formatted}', end='')
        print()

def print_specific_table(number, start, end, highlight_squares, use_colors):
    clear_screen()
    print(f'📊 MULTIPLICATION TABLE FOR {number}')
    print('=' * 40)
    
    for i in range(start, end + 1):
        product = number * i
        is_square = is_perfect_square(product) and highlight_squares
        
        if use_colors:
            color = get_color_for_number(product, is_square, True)
            reset = reset_color()
            if is_square:
                print(f'{number} × {i:2} = {color}{product:3}²{reset}')
            else:
                print(f'{number} × {i:2} = {color}{product:3}{reset}')
        else:
            if is_square and highlight_squares:
                print(f'{number} × {i:2} = {product:3}²')
            else:
                print(f'{number} × {i:2} = {product:3}')

def show_table_analysis(start, end):
    total_products = (end - start + 1) ** 2
    perfect_squares = sum(1 for i in range(start, end + 1) for j in range(start, end + 1) 
                         if is_perfect_square(i * j))
    
    print(f'\n📈 TABLE ANALYSIS:')
    print(f'Range: {start} to {end}')
    print(f'Total calculations: {total_products}')
    print(f'Perfect squares: {perfect_squares}')
    print(f'Perfect square ratio: {perfect_squares/total_products*100:.1f}%')

def show_legend(use_colors):
    if use_colors:
        print('\n🎨 COLOR LEGEND:')
        print(f'{get_color_for_number(0, False, True)}Gray{reset_color()}: Zero')
        print(f'{get_color_for_number(4, True, True)}Yellow{reset_color()}: Perfect squares')
        print(f'{get_color_for_number(2, False, True)}Blue{reset_color()}: Even numbers')
        print(f'{get_color_for_number(3, False, True)}Green{reset_color()}: Odd numbers')

def save_table_to_file(start, end, highlight_squares, specific_number=None):
    try:
        if specific_number:
            filename = f'multiplication_table_{specific_number}x.txt'
        else:
            filename = f'multiplication_table_{start}-{end}.txt'
        
        with open(filename, 'w') as f:
            f.write(f'MULTIPLICATION TABLE\n')
            f.write(f'Range: {start} to {end}\n')
            if specific_number:
                f.write(f'Specific table: {specific_number}\n')
            f.write('=' * 50 + '\n\n')
            
            if specific_number:
                for i in range(start, end + 1):
                    product = specific_number * i
                    if is_perfect_square(product) and highlight_squares:
                        f.write(f'{specific_number} × {i:2} = {product:3}²\n')
                    else:
                        f.write(f'{specific_number} × {i:2} = {product:3}\n')
            else:
                header = '   |'
                for col in range(start, end + 1):
                    header += f'{col:4} '
                f.write(header + '\n')
                
                separator = '---+' + '-----' * (end - start + 1)
                f.write(separator + '\n')
                
                for row in range(start, end + 1):
                    f.write(f'{row:2} |')
                    for col in range(start, end + 1):
                        product = row * col
                        if is_perfect_square(product) and highlight_squares:
                            f.write(f'{product:4}²')
                        else:
                            f.write(f'{product:4} ')
                    f.write('\n')
        
        print(f'💾 Table saved as: {filename}')
        
    except Exception as e:
        print(f'❌ Error saving file: {e}')

def main():
    start_num, end_num = get_table_settings()
    highlight_squares, use_colors, specific_number = get_display_options()
    
    while True:
        if specific_number is not None:
            print_specific_table(specific_number, start_num, end_num, highlight_squares, use_colors)
        else:
            print_full_table(start_num, end_num, highlight_squares, use_colors)
        
        show_table_analysis(start_num, end_num)
        show_legend(use_colors)
        
        print('\n🎯 Options:')
        print('[N] New table  [S] Save to file  [C] Change colors  [Q] Quit')
        
        choice = input('\nEnter choice: ').upper().strip()
        
        if choice == 'Q':
            break
        elif choice == 'N':
            start_num, end_num = get_table_settings()
            highlight_squares, use_colors, specific_number = get_display_options()
        elif choice == 'S':
            save_table_to_file(start_num, end_num, highlight_squares, specific_number)
            input('Press Enter to continue...')
        elif choice == 'C':
            use_colors = not use_colors
            print(f'🎨 Colors {"enabled" if use_colors else "disabled"}!')
            input('Press Enter to continue...')
    
    clear_screen()
    print('\n📊 Thanks for using the Multiplication Table Generator! 📊')

if __name__ == '__main__':
    main()