import sys
import random
import os
import time

try:
    import bext
    HAS_BEXT = True
except ImportError:
    HAS_BEXT = False

MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6

WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'

ANSI_COLORS = {
    'white': '\033[47m',
    'black': '\033[40m',
    'red': '\033[41m',
    'yellow': '\033[43m',
    'blue': '\033[44m',
    'reset': '\033[0m'
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_terminal_size():
    if HAS_BEXT:
        width, height = bext.size()
        return width - 1, height - 3
    else:
        try:
            size = os.get_terminal_size()
            return size.columns - 1, size.lines - 3
        except:
            return 80, 20

def display_welcome():
    clear_screen()
    print('🎨 ' + '=' * 70 + ' 🎨')
    print('|' + ' ' * 74 + '|')
    print('|' + '        🌈 MONDRIAN ART GENERATOR - Digital Canvas 🌈     '.center(72) + '|')
    print('|' + ' ' * 74 + '|')
    print('|' + '  Generate infinite abstract art in Piet Mondrian style  '.center(74) + '|')
    print('|' + '  with customizable colors and dynamic compositions!     '.center(74) + '|')
    print('|' + ' ' * 74 + '|')
    print('🎨 ' + '=' * 70 + ' 🎨')
    print()

def get_art_settings():
    print('🎨 Art Generation Settings:')
    
    while True:
        try:
            complexity = input('Complexity (1-Simple, 2-Medium, 3-Complex, Enter for Medium): ').strip()
            if complexity == '':
                complexity = 2
            else:
                complexity = int(complexity)
            if complexity not in [1, 2, 3]:
                print('❌ Please enter 1, 2, or 3!')
                continue
            break
        except ValueError:
            print('❌ Please enter a valid number!')
    
    while True:
        color_mode = input('Color palette (1-Classic, 2-Extended, 3-Monochrome, Enter for Classic): ').strip()
        if color_mode == '':
            color_mode = 1
        elif color_mode in ['1', '2', '3']:
            color_mode = int(color_mode)
        else:
            print('❌ Please enter 1, 2, or 3!')
            continue
        break
    
    while True:
        auto_mode = input('Auto-generate art continuously? (y/n, Enter for manual): ').lower().strip()
        if auto_mode in ['', 'n', 'no']:
            auto_mode = False
            break
        elif auto_mode in ['y', 'yes']:
            auto_mode = True
            break
        else:
            print('❌ Please enter y or n!')
    
    return complexity, color_mode, auto_mode

def get_color_palette(color_mode):
    if color_mode == 1:
        return [RED, YELLOW, BLUE, BLACK]
    elif color_mode == 2:
        return [RED, YELLOW, BLUE, BLACK, 'green', 'magenta', 'cyan']
    else:
        return [BLACK, WHITE]

def adjust_complexity_settings(complexity):
    if complexity == 1:
        return 8, 20, 4, 8
    elif complexity == 2:
        return MIN_X_INCREASE, MAX_X_INCREASE, MIN_Y_INCREASE, MAX_Y_INCREASE
    else:
        return 4, 12, 2, 4

def set_color(color):
    if HAS_BEXT:
        bext.bg(color)
    else:
        ansi_color = ANSI_COLORS.get(color, ANSI_COLORS['white'])
        print(ansi_color, end='')

def reset_color():
    if not HAS_BEXT:
        print(ANSI_COLORS['reset'], end='')

def create_canvas(width, height):
    canvas = {}
    for x in range(width):
        for y in range(height):
            canvas[(x, y)] = WHITE
    return canvas

def generate_vertical_lines(canvas, width, height, min_x_inc, max_x_inc):
    segments_created = 0
    x = random.randint(min_x_inc, max_x_inc)
    while x < width - min_x_inc:
        segments_created += 1
        for y in range(height):
            canvas[(x, y)] = BLACK
        x += random.randint(min_x_inc, max_x_inc)
    return segments_created

def generate_horizontal_lines(canvas, width, height, min_y_inc, max_y_inc):
    segments_created = 0
    y = random.randint(min_y_inc, max_y_inc)
    while y < height - min_y_inc:
        segments_created += 1
        for x in range(width):
            canvas[(x, y)] = BLACK
        y += random.randint(min_y_inc, max_y_inc)
    return segments_created

def can_delete_segment(canvas, startx, starty, width, height, orientation):
    points_to_delete = [(startx, starty)]
    
    if orientation == 'vertical':
        for changey in (-1, 1):
            y = starty
            while 0 < y < height - 1:
                y += changey
                if (canvas[(startx - 1, y)] == BLACK and canvas[(startx + 1, y)] == BLACK):
                    break
                elif ((canvas[(startx - 1, y)] == WHITE and canvas[(startx + 1, y)] == BLACK) or
                      (canvas[(startx - 1, y)] == BLACK and canvas[(startx + 1, y)] == WHITE)):
                    return False, []
                else:
                    points_to_delete.append((startx, y))
    
    elif orientation == 'horizontal':
        for changex in (-1, 1):
            x = startx
            while 0 < x < width - 1:
                x += changex
                if (canvas[(x, starty - 1)] == BLACK and canvas[(x, starty + 1)] == BLACK):
                    break
                elif ((canvas[(x, starty - 1)] == WHITE and canvas[(x, starty + 1)] == BLACK) or
                      (canvas[(x, starty - 1)] == BLACK and canvas[(x, starty + 1)] == WHITE)):
                    return False, []
                else:
                    points_to_delete.append((x, starty))
    
    return True, points_to_delete

def remove_segments(canvas, width, height, num_segments_to_delete):
    for i in range(num_segments_to_delete):
        attempts = 0
        while attempts < 100:
            attempts += 1
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            
            if canvas[(startx, starty)] == WHITE:
                continue
            
            if (canvas[(startx - 1, starty)] == WHITE and canvas[(startx + 1, starty)] == WHITE):
                orientation = 'vertical'
            elif (canvas[(startx, starty - 1)] == WHITE and canvas[(startx, starty + 1)] == WHITE):
                orientation = 'horizontal'
            else:
                continue
            
            can_delete, points_to_delete = can_delete_segment(canvas, startx, starty, width, height, orientation)
            
            if can_delete:
                for x, y in points_to_delete:
                    canvas[(x, y)] = WHITE
                break

def add_borders(canvas, width, height):
    for x in range(width):
        canvas[(x, 0)] = BLACK
        canvas[(x, height - 1)] = BLACK
    for y in range(height):
        canvas[(0, y)] = BLACK
        canvas[(width - 1, y)] = BLACK

def flood_fill(canvas, startx, starty, color):
    points_to_paint = set([(startx, starty)])
    while len(points_to_paint) > 0:
        x, y = points_to_paint.pop()
        canvas[(x, y)] = color
        if canvas.get((x - 1, y)) == WHITE:
            points_to_paint.add((x - 1, y))
        if canvas.get((x + 1, y)) == WHITE:
            points_to_paint.add((x + 1, y))
        if canvas.get((x, y - 1)) == WHITE:
            points_to_paint.add((x, y - 1))
        if canvas.get((x, y + 1)) == WHITE:
            points_to_paint.add((x, y + 1))

def paint_rectangles(canvas, width, height, num_rectangles, color_palette):
    for i in range(num_rectangles):
        attempts = 0
        while attempts < 50:
            attempts += 1
            startx = random.randint(1, width - 2)
            starty = random.randint(1, height - 2)
            
            if canvas[(startx, starty)] != WHITE:
                continue
            
            color_to_paint = random.choice(color_palette)
            flood_fill(canvas, startx, starty, color_to_paint)
            break

def display_canvas(canvas, width, height):
    for y in range(height):
        for x in range(width):
            set_color(canvas[(x, y)])
            print(' ', end='')
        reset_color()
        print()

def display_art_info(art_count, complexity, color_mode):
    complexity_names = {1: 'Simple', 2: 'Medium', 3: 'Complex'}
    color_names = {1: 'Classic', 2: 'Extended', 3: 'Monochrome'}
    
    print(f'\n🎨 Artwork #{art_count} | Complexity: {complexity_names[complexity]} | Palette: {color_names[color_mode]}')

def save_art_data(canvas, width, height, art_count):
    try:
        filename = f'mondrian_art_{art_count:03d}.txt'
        with open(filename, 'w') as f:
            f.write(f'Mondrian Art #{art_count}\n')
            f.write(f'Dimensions: {width}x{height}\n')
            f.write('=' * width + '\n')
            
            for y in range(height):
                for x in range(width):
                    color = canvas[(x, y)]
                    if color == WHITE:
                        f.write(' ')
                    elif color == BLACK:
                        f.write('#')
                    elif color == RED:
                        f.write('R')
                    elif color == YELLOW:
                        f.write('Y')
                    elif color == BLUE:
                        f.write('B')
                    else:
                        f.write('*')
                f.write('\n')
        
        print(f'💾 Art saved as: {filename}')
    except Exception as e:
        print(f'❌ Could not save art: {e}')

def generate_mondrian_art(complexity, color_palette, width, height):
    min_x_inc, max_x_inc, min_y_inc, max_y_inc = adjust_complexity_settings(complexity)
    
    canvas = create_canvas(width, height)
    
    v_segments = generate_vertical_lines(canvas, width, height, min_x_inc, max_x_inc)
    h_segments = generate_horizontal_lines(canvas, width, height, min_y_inc, max_y_inc)
    
    total_segments = v_segments + h_segments
    num_rectangles = max(1, total_segments - 3)
    num_segments_to_delete = int(total_segments * 1.5)
    
    remove_segments(canvas, width, height, num_segments_to_delete)
    add_borders(canvas, width, height)
    paint_rectangles(canvas, width, height, num_rectangles, color_palette)
    
    return canvas

def main():
    display_welcome()
    
    width, height = get_terminal_size()
    complexity, color_mode, auto_mode = get_art_settings()
    color_palette = get_color_palette(color_mode)
    
    art_count = 0
    
    try:
        while True:
            art_count += 1
            clear_screen()
            
            canvas = generate_mondrian_art(complexity, color_palette, width, height)
            display_canvas(canvas, width, height)
            display_art_info(art_count, complexity, color_mode)
            
            if auto_mode:
                print('⏱️  Auto-generating... (Ctrl+C to stop)')
                time.sleep(2)
            else:
                print('\n🎨 Commands: [Enter] New art, [S] Save, [A] Auto mode, [Q] Quit')
                choice = input('> ').lower().strip()
                
                if choice == 'q':
                    break
                elif choice == 's':
                    save_art_data(canvas, width, height, art_count)
                    input('Press Enter to continue...')
                elif choice == 'a':
                    auto_mode = True
                    print('🔄 Switched to auto mode!')
                    time.sleep(1)
    
    except KeyboardInterrupt:
        pass
    
    reset_color()
    clear_screen()
    print('\n🎨 Thank you for exploring Mondrian art! Goodbye! 🎨')

if __name__ == '__main__':
    main()