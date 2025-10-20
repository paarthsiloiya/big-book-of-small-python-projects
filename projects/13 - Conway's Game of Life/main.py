import copy, sys, time, random, os

WIDTH = 60
HEIGHT = 20
ALIVE = '██'
DEAD = '  '
ALIVE_RATIO = 0.2

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_box_with_cells(cells):
    print('┌' + '─' * (WIDTH * 2) + '┐')
    
    for y in range(HEIGHT):
        print('│', end='')
        for x in range(WIDTH):
            if (x, y) in cells:
                print(ALIVE, end='')
            else:
                print(DEAD, end='')
        print('│')
    
    print('└' + '─' * (WIDTH * 2) + '┘')

def get_initial_state():
    cells = {}
    
    print("Conway's Game of Life - Initial State Drawing")
    print("=" * 60)
    print("Instructions:")
    print("  - Enter coordinates as 'x,y' to toggle a cell (e.g., '40,10')")
    print("  - Enter 'clear' to clear all cells")
    print("  - Enter 'random' to generate random pattern")
    print("  - Enter 'done' when finished")
    print(f"  - Valid coordinates: x(0-{WIDTH-1}), y(0-{HEIGHT-1})")
    print("=" * 60)
    
    while True:
        draw_box_with_cells(cells)
        print(f"\nLiving cells: {len(cells)}")
        command = input("Enter command: ").strip().lower()
        
        if command == 'done':
            if len(cells) > 0:
                break
            else:
                print("Please add at least one living cell before starting!")
                continue
        
        elif command == 'clear':
            cells = {}
            print("All cells cleared!")
            
        elif command == 'random':
            cells = {}
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if random.random() < ALIVE_RATIO:
                        cells[(x, y)] = True
            print(f"Random pattern generated! ({len(cells)} cells alive, {ALIVE_RATIO*100:.1f}% density)")
            
        else:
            try:
                parts = command.split(',')
                if len(parts) == 2:
                    x = int(parts[0].strip())
                    y = int(parts[1].strip())
                    
                    if 0 <= x < WIDTH and 0 <= y < HEIGHT:
                        if (x, y) in cells:
                            del cells[(x, y)]
                            print(f"Cell at ({x}, {y}) removed")
                        else:
                            cells[(x, y)] = True
                            print(f"Cell at ({x}, {y}) added")
                    else:
                        print(f"Coordinates out of bounds! Use x(0-{WIDTH-1}), y(0-{HEIGHT-1})")
                else:
                    print("Invalid format! Use 'x,y' format (e.g., '40,10')")
            except ValueError:
                print("Invalid input! Use 'x,y' format with numbers, 'clear', 'random', or 'done'")
        
        clear_screen()
    
    return cells

def get_neighbors(x, y):
    neighbors = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx = (x + dx) % WIDTH
            ny = (y + dy) % HEIGHT
            if (nx, ny) in cells:
                neighbors += 1
    return neighbors

def get_next_generation(cells):
    next_cells = {}
    
    cells_to_check = set()
    for (x, y) in cells:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx = (x + dx) % WIDTH
                ny = (y + dy) % HEIGHT
                cells_to_check.add((nx, ny))
    
    for (x, y) in cells_to_check:
        neighbors = get_neighbors(x, y)
        
        if (x, y) in cells:
            if neighbors in [2, 3]:
                next_cells[(x, y)] = True
        else:
            if neighbors == 3:
                next_cells[(x, y)] = True
    
    return next_cells

cells = get_initial_state()

print("\nStarting simulation... Press Ctrl+C to stop.")
time.sleep(2)

generation = 0
try:
    while True:
        clear_screen()
        print(f"Generation: {generation} | Living cells: {len(cells)}")
        draw_box_with_cells(cells)
        
        cells = get_next_generation(cells)
        generation += 1
        time.sleep(0.2)
        
except KeyboardInterrupt:
    print("\n\nSimulation stopped.")
    sys.exit()
