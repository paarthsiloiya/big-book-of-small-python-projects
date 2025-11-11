import copy
import sys
import os
import random

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wall_str_to_wall_dict(wall_str):
    wall_dict = {}
    height = 0
    width = 0
    for y, line in enumerate(wall_str.splitlines()):
        if y > height:
            height = y
        for x, character in enumerate(line):
            if x > width:
                width = x
            wall_dict[(x, y)] = character
    wall_dict['height'] = height + 1
    wall_dict['width'] = width + 1
    return wall_dict

EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}

ALL_OPEN = wall_str_to_wall_dict(r'''
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())

CLOSED = {}
CLOSED['A'] = wall_str_to_wall_dict(r'''
_____
.....
.....
.....
_____'''.strip())

CLOSED['B'] = wall_str_to_wall_dict(r'''
.\.
..\
...
...
...
../
./.'''.strip())

CLOSED['C'] = wall_str_to_wall_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())

CLOSED['D'] = wall_str_to_wall_dict(r'''
./.
/..
...
...
...
\..
.\.'''.strip())

CLOSED['E'] = wall_str_to_wall_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())

CLOSED['F'] = wall_str_to_wall_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())

def display_wall_dict(wall_dict):
    print('█' * (wall_dict['width'] + 2))
    for y in range(wall_dict['height']):
        print('█', end='')
        for x in range(wall_dict['width']):
            wall = wall_dict[(x, y)]
            if wall == '.':
                wall = ' '
            print(wall, end='')
        print('█')
    print('█' * (wall_dict['width'] + 2))

def paste_wall_dict(src_wall_dict, dst_wall_dict, left, top):
    dst_wall_dict = copy.copy(dst_wall_dict)
    for x in range(src_wall_dict['width']):
        for y in range(src_wall_dict['height']):
            dst_wall_dict[(x + left, y + top)] = src_wall_dict[(x, y)]
    return dst_wall_dict

def make_wall_dict(maze, playerx, playery, player_direction, exitx, exity):
    if player_direction == NORTH:
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    elif player_direction == SOUTH:
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    elif player_direction == EAST:
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    elif player_direction == WEST:
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, x_off, y_off in offsets:
        section[sec] = maze.get((playerx + x_off, playery + y_off), WALL)
        if (playerx + x_off, playery + y_off) == (exitx, exity):
            section[sec] = EXIT

    wall_dict = copy.copy(ALL_OPEN)
    paste_closed_to = {'A': (6, 4), 'B': (4, 3), 'C': (3, 1),
                       'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wall_dict = paste_wall_dict(CLOSED[sec], wall_dict,
                paste_closed_to[sec][0], paste_closed_to[sec][1])

    if section['C'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 7, 9)
    if section['E'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 0, 11)
    if section['F'] == EXIT:
        wall_dict = paste_wall_dict(EXIT_DICT, wall_dict, 13, 11)

    return wall_dict

def display_welcome():
    clear_screen()
    print('🏛️ ' + '=' * 60 + ' 🏛️')
    print('|' + ' ' * 60 + '|')
    print('|' + '        🌟 MAZE RUNNER 3D - First Person View 🌟       '.center(60) + '|')
    print('|' + ' ' * 60 + '|')
    print('|' + '     Navigate through ancient corridors to escape!     '.center(60) + '|')
    print('|' + '     Use WASD or FLRD commands to move and turn!       '.center(60) + '|')
    print('|' + ' ' * 60 + '|')
    print('🏛️ ' + '=' * 60 + ' 🏛️')
    print()

def get_difficulty():
    while True:
        print('Choose maze type:')
        print('1. 📁 Load existing maze file')
        print('2. 🎲 Generate random simple maze')
        
        choice = input('\nEnter choice (1-2): ').strip()
        if choice in ['1', '2']:
            return choice
        print('Invalid choice! Please enter 1 or 2.')

def generate_simple_maze():
    width, height = 15, 15
    maze = {}
    
    for y in range(height):
        for x in range(width):
            if x == 0 or x == width-1 or y == 0 or y == height-1:
                maze[(x, y)] = WALL
            elif x % 2 == 0 and y % 2 == 0:
                maze[(x, y)] = WALL
            else:
                maze[(x, y)] = EMPTY
    
    start_x, start_y = 1, 1
    exit_x, exit_y = width-2, height-2
    
    return maze, start_x, start_y, exit_x, exit_y, width, height

def load_maze_file():
    while True:
        print('Enter the filename of the maze (or LIST or QUIT):')
        filename = input('> ')

        if filename.upper() == 'LIST':
            print('Maze files found in', os.getcwd())
            for file_in_current_folder in os.listdir():
                if (file_in_current_folder.startswith('maze')
                and file_in_current_folder.endswith('.txt')):
                    print('  ', file_in_current_folder)
            continue

        if filename.upper() == 'QUIT':
            sys.exit()

        if os.path.exists(filename):
            break
        print('There is no file named', filename)

    maze_file = open(filename)
    maze = {}
    lines = maze_file.readlines()
    px = None
    py = None
    exitx = None
    exity = None
    y = 0
    
    for line in lines:
        width = len(line.rstrip())
        for x, character in enumerate(line.rstrip()):
            assert character in (WALL, EMPTY, START, EXIT), f'Invalid character at column {x + 1}, line {y + 1}'
            if character in (WALL, EMPTY):
                maze[(x, y)] = character
            elif character == START:
                px, py = x, y
                maze[(x, y)] = EMPTY
            elif character == EXIT:
                exitx, exity = x, y
                maze[(x, y)] = EMPTY
        y += 1
    
    height = y
    maze_file.close()
    
    assert px is not None and py is not None, 'No start point in file.'
    assert exitx is not None and exity is not None, 'No exit point in file.'
    
    return maze, px, py, exitx, exity, width, height

def display_status(px, py, p_dir, steps, maze_type):
    print('🧭 Position: ({}, {})  Direction: {}  Steps: {}  Type: {}'.format(
        px, py, p_dir, steps, maze_type))

def display_controls():
    print('🎮 Controls: [F/W]orward [L/A]eft [R/D]ight [H]elp [Q]uit')

def show_help():
    print('\n📖 HELP:')
    print('F or W - Move forward in your current direction')
    print('L or A - Turn left (counterclockwise)')  
    print('R or D - Turn right (clockwise)')
    print('H - Show this help')
    print('Q - Quit game')
    print('T x,y - Teleport to coordinates (cheat)')
    print('\n3D View: You see walls and passages from first-person perspective!')
    print('Find the EXIT sign to escape the maze! 🚪')
    input('\nPress Enter to continue...')

def main():
    display_welcome()
    difficulty = get_difficulty()
    
    if difficulty == '1':
        maze, px, py, exitx, exity, width, height = load_maze_file()
        maze_type = "📁 File"
    else:
        maze, px, py, exitx, exity, width, height = generate_simple_maze()
        maze_type = "🎲 Random"
    
    p_dir = NORTH
    steps = 0
    
    while True:
        clear_screen()
        display_wall_dict(make_wall_dict(maze, px, py, p_dir, exitx, exity))
        display_status(px, py, p_dir, steps, maze_type)
        display_controls()
        
        while True:
            move = input('> ').upper().strip()

            if move in ['QUIT', 'Q']:
                print('\n👋 Thanks for playing Maze Runner 3D! 👋')
                sys.exit()

            if move in ['HELP', 'H']:
                show_help()
                break

            if move not in ['F', 'L', 'R', 'W', 'A', 'D'] and not move.startswith('T'):
                print('❌ Invalid command! Type H for help.')
                continue

            if move in ['F', 'W']:
                new_x, new_y = px, py
                if p_dir == NORTH:
                    new_y -= 1
                elif p_dir == SOUTH:
                    new_y += 1
                elif p_dir == EAST:
                    new_x += 1
                elif p_dir == WEST:
                    new_x -= 1
                
                if maze.get((new_x, new_y)) == EMPTY:
                    px, py = new_x, new_y
                    steps += 1
                    break
                else:
                    print('🚫 Cannot move forward - wall blocks your path!')
                    
            elif move in ['L', 'A']:
                p_dir = {NORTH: WEST, WEST: SOUTH, SOUTH: EAST, EAST: NORTH}[p_dir]
                steps += 1
                break
                
            elif move in ['R', 'D']:
                p_dir = {NORTH: EAST, EAST: SOUTH, SOUTH: WEST, WEST: NORTH}[p_dir]
                steps += 1
                break
                
            elif move.startswith('T'):
                try:
                    coords = move.split()[1].split(',')
                    new_x, new_y = int(coords[0]), int(coords[1])
                    if maze.get((new_x, new_y)) == EMPTY:
                        px, py = new_x, new_y
                        print('🔮 Teleported successfully!')
                    else:
                        print('❌ Cannot teleport to wall!')
                except:
                    print('❌ Invalid teleport format! Use: T x,y')
                break

        if (px, py) == (exitx, exity):
            clear_screen()
            print('🎉 ' + '=' * 50 + ' 🎉')
            print()
            print('🏆 CONGRATULATIONS! YOU ESCAPED! 🏆')
            print(f'✨ Completed in {steps} steps! ✨')
            print('🌟 You have mastered the 3D maze! 🌟')
            print()
            print('🎉 ' + '=' * 50 + ' 🎉')
            print('\n👋 Thanks for playing! 👋')
            sys.exit()

if __name__ == '__main__':
    main()