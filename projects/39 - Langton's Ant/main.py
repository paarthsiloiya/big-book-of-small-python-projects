import copy
import random
import sys
import time
import bext

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

SIMULATION_PRESETS = {
    'CLASSIC': {'ants': 1, 'speed': 0.05, 'colors': 2},
    'SWARM': {'ants': 10, 'speed': 0.02, 'colors': 2},
    'RAINBOW': {'ants': 5, 'speed': 0.03, 'colors': 4},
    'CHAOS': {'ants': 25, 'speed': 0.01, 'colors': 6},
    'SLOW_MOTION': {'ants': 3, 'speed': 0.2, 'colors': 3}
}

ANT_CHARS = {
    'north': '▲',
    'south': '▼', 
    'east': '►',
    'west': '◄'
}

COLOR_TILES = [' ', '█', '▓', '▒', '░', '●', '■']
ANT_COLORS = ['red', 'cyan', 'yellow', 'magenta', 'green', 'blue', 'white']

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

def select_preset():
    bext.clear()
    bext.fg('white')
    print("╔" + "═" * 58 + "╗")
    print("║" + " " * 18 + "LANGTON'S ANT SIMULATOR" + " " * 17 + "║")
    print("╚" + "═" * 58 + "╝")
    print("\nSelect a simulation preset:")
    
    presets = list(SIMULATION_PRESETS.keys())
    for i, preset in enumerate(presets, 1):
        settings = SIMULATION_PRESETS[preset]
        print(f"{i}. {preset:<12} - {settings['ants']:2d} ants, {settings['colors']} colors, {settings['speed']:.2f}s speed")
    
    print(f"{len(presets) + 1}. CUSTOM      - Design your own simulation")
    
    while True:
        try:
            choice = int(input(f"\nEnter choice (1-{len(presets) + 1}): "))
            if 1 <= choice <= len(presets):
                return SIMULATION_PRESETS[presets[choice - 1]]
            elif choice == len(presets) + 1:
                return create_custom_preset()
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number.")

def create_custom_preset():
    print("\n--- Custom Simulation Setup ---")
    
    while True:
        try:
            ants = int(input("Number of ants (1-50): "))
            if 1 <= ants <= 50:
                break
            print("Please enter a number between 1 and 50.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            colors = int(input("Number of colors (2-7): "))
            if 2 <= colors <= 7:
                break
            print("Please enter a number between 2 and 7.")
        except ValueError:
            print("Please enter a valid number.")
    
    while True:
        try:
            speed = float(input("Animation speed in seconds (0.001-1.0): "))
            if 0.001 <= speed <= 1.0:
                break
            print("Please enter a number between 0.001 and 1.0.")
        except ValueError:
            print("Please enter a valid number.")
    
    return {'ants': ants, 'speed': speed, 'colors': colors}

def main():
    settings = select_preset()
    
    bext.clear()
    bext.fg('white')
    print("Initializing simulation...")
    print(f"Ants: {settings['ants']}, Colors: {settings['colors']}, Speed: {settings['speed']}s")
    print("Press Ctrl+C to stop the simulation.")
    time.sleep(2)
    
    bext.fg('white')
    bext.bg('black')
    bext.clear()

    board = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = 0

    ants = []
    for i in range(settings['ants']):
        ant = {
            'x': random.randint(WIDTH//4, 3*WIDTH//4),
            'y': random.randint(HEIGHT//4, 3*HEIGHT//4),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST]),
            'id': i,
            'steps': 0,
            'color_index': i % len(ANT_COLORS)
        }
        ants.append(ant)

    step_count = 0
    start_time = time.time()
    
    try:
        while True:
            display_board(board, ants, settings, step_count, start_time)
            next_board(board, ants, settings['colors'])
            step_count += 1
            time.sleep(settings['speed'])
    except KeyboardInterrupt:
        show_statistics(ants, step_count, start_time)

def display_board(board, ants, settings, step_count, start_time):
    elapsed_time = time.time() - start_time
    
    bext.goto(0, 0)
    bext.fg('white')
    status_line = f"Step: {step_count:6d} | Time: {elapsed_time:6.1f}s | Ants: {len(ants)} | Colors: {settings['colors']} | Speed: {settings['speed']}s"
    print(status_line + " " * (WIDTH - len(status_line)))

    ant_positions = {}
    for ant in ants:
        ant_positions[(ant['x'], ant['y'])] = ant

    for y in range(1, HEIGHT):
        bext.goto(0, y)
        for x in range(WIDTH):
            if (x, y) in ant_positions:
                ant = ant_positions[(x, y)]
                bext.fg(ANT_COLORS[ant['color_index']])
                print(ANT_CHARS[ant['direction']], end='')
            else:
                color_value = board[(x, y)]
                if color_value == 0:
                    bext.fg('black')
                    print(' ', end='')
                else:
                    tile_colors = ['white', 'red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
                    bext.fg(tile_colors[min(color_value - 1, len(tile_colors) - 1)])
                    print(COLOR_TILES[min(color_value, len(COLOR_TILES) - 1)], end='')
        sys.stdout.flush()

def next_board(board, ants, num_colors):
    for ant in ants:
        current_color = board[(ant['x'], ant['y'])]
        
        if current_color % 2 == 0:
            turn_left(ant)
        else:
            turn_right(ant)
        
        board[(ant['x'], ant['y'])] = (current_color + 1) % num_colors
        
        move_ant_forward(ant)
        ant['steps'] += 1

def turn_left(ant):
    if ant['direction'] == NORTH:
        ant['direction'] = WEST
    elif ant['direction'] == WEST:
        ant['direction'] = SOUTH
    elif ant['direction'] == SOUTH:
        ant['direction'] = EAST
    elif ant['direction'] == EAST:
        ant['direction'] = NORTH

def turn_right(ant):
    if ant['direction'] == NORTH:
        ant['direction'] = EAST
    elif ant['direction'] == EAST:
        ant['direction'] = SOUTH
    elif ant['direction'] == SOUTH:
        ant['direction'] = WEST
    elif ant['direction'] == WEST:
        ant['direction'] = NORTH

def move_ant_forward(ant):
    if ant['direction'] == NORTH:
        ant['y'] -= 1
    elif ant['direction'] == SOUTH:
        ant['y'] += 1
    elif ant['direction'] == WEST:
        ant['x'] -= 1
    elif ant['direction'] == EAST:
        ant['x'] += 1

    ant['x'] = ant['x'] % WIDTH
    ant['y'] = ant['y'] % HEIGHT
    if ant['y'] == 0:
        ant['y'] = 1

def show_statistics(ants, step_count, start_time):
    bext.clear()
    bext.fg('white')
    
    total_time = time.time() - start_time
    
    print("╔" + "═" * 50 + "╗")
    print("║" + " " * 15 + "SIMULATION COMPLETE" + " " * 16 + "║")
    print("╚" + "═" * 50 + "╝")
    print(f"\nTotal simulation time: {total_time:.2f} seconds")
    print(f"Total steps completed: {step_count}")
    print(f"Steps per second: {step_count/total_time:.1f}")
    print(f"Number of ants: {len(ants)}")
    
    print("\n--- Individual Ant Statistics ---")
    for ant in ants:
        print(f"Ant #{ant['id']:2d}: {ant['steps']:6d} steps, facing {ant['direction']}")
    
    print(f"\nAverage steps per ant: {sum(ant['steps'] for ant in ants) / len(ants):.1f}")
    print("\nThank you for watching Langton's Ant simulation!")

if __name__ == '__main__':
    main()