import random
import sys
import time
import os

try:
    import bext
except ImportError:
    print("Installing bext module...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "bext"])
    import bext

# Constants
EMPTY = ' '
TREE = '🌲'
FIRE = '🔥'

TREE_GROW_CHANCE = 0.01  # 1% chance
LIGHTNING_CHANCE = 0.01  # 1% chance


def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines - 2
    except OSError:
        return 80, 20


def create_forest(width, height):
    forest = []
    for y in range(height):
        row = []
        for x in range(width):
            if random.random() < 0.2:
                row.append(TREE)
            else:
                row.append(EMPTY)
        forest.append(row)
    return forest


def display_forest_initial(forest, generation):
    bext.hide_cursor()
    bext.clear()
    
    height = len(forest)
    width = len(forest[0])
    
    for y in range(height):
        bext.goto(0, y)
        for x in range(width):
            cell = forest[y][x]
            if cell == TREE:
                bext.fg('green')
            elif cell == FIRE:
                bext.fg('red')
            else:
                bext.fg('white')
            print(cell, end='')
    
    bext.goto(0, height)
    bext.fg('white')
    print(f'Generation: {generation} | Press Ctrl+C to quit', end='')


def update_forest_changes(old_forest, new_forest, generation):
    height = len(new_forest)
    width = len(new_forest[0])
    changes_made = False

    for y in range(height):
        for x in range(width):
            if old_forest[y][x] != new_forest[y][x]:
                changes_made = True
                bext.goto(x, y)
                
                cell = new_forest[y][x]
                if cell == TREE:
                    bext.fg('green')
                elif cell == FIRE:
                    bext.fg('red')
                else:
                    bext.fg('white')
                print(cell, end='', flush=True)
    
    bext.goto(0, height)
    bext.fg('white')
    print(f'Generation: {generation} | Press Ctrl+C to quit', end='', flush=True)
    
    return changes_made


def get_neighbors(forest, x, y):
    width = len(forest[0])
    height = len(forest)
    neighbors = []
    
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbors.append((nx, ny))
    
    return neighbors


def simulate_step(forest):
    width = len(forest[0])
    height = len(forest)
    new_forest = [[EMPTY for _ in range(width)] for _ in range(height)]
    
    for y in range(height):
        for x in range(width):
            if forest[y][x] == FIRE:
                new_forest[y][x] = EMPTY
            elif forest[y][x] == TREE:
                new_forest[y][x] = TREE
            else:
                new_forest[y][x] = EMPTY
    
    for y in range(height):
        for x in range(width):
            if forest[y][x] == EMPTY:
                if random.random() < TREE_GROW_CHANCE:
                    new_forest[y][x] = TREE
            
            elif forest[y][x] == TREE:
                neighbors = get_neighbors(forest, x, y)
                fire_nearby = any(forest[ny][nx] == FIRE for nx, ny in neighbors)
                
                if fire_nearby:
                    new_forest[y][x] = FIRE
                elif random.random() < LIGHTNING_CHANCE:
                    new_forest[y][x] = FIRE
    
    return new_forest


def main():
    width, height = get_terminal_size()
    
    width = width // 2
    
    print("Forest Fire Simulation")
    print(f"Terminal size: {width}x{height}")
    print("Starting simulation in 3 seconds...")
    time.sleep(3)
    
    forest = create_forest(width, height)
    generation = 0
    
    try:
        display_forest_initial(forest, generation)
        
        while True:
            time.sleep(0.1)
            
            old_forest = [row[:] for row in forest]
            
            forest = simulate_step(forest)
            generation += 1
            
            update_forest_changes(old_forest, forest, generation)
            
    except KeyboardInterrupt:
        bext.show_cursor()
        bext.clear()
        bext.fg('white')
        print("\nSimulation ended.")
        print(f"Final generation: {generation}")


if __name__ == '__main__':
    main()