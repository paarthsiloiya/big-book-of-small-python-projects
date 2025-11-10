# Maze Runner 2D

A simple console-based maze navigation game where players find their way from start to exit.

## How to Play

1. Run the program: `python main.py`
2. Enter a maze filename when prompted (or type LIST to see available mazes)
3. Use WASD keys to navigate:
   - **W** - Move up
   - **A** - Move left  
   - **S** - Move down
   - **D** - Move right
4. Find the exit marked with 'X' to win!

## Game Mechanics

- **@** represents your player
- **░** represents walls (you cannot pass through)
- **X** marks the exit location
- Empty spaces are paths you can walk on

### Smart Movement System
The game features intelligent movement - when you choose a direction, you'll automatically continue moving until you reach a branch point or dead end. This makes navigation faster and more fluid.

## Maze Files

The game loads mazes from text files with this format:
- **#** = Wall
- **(space)** = Empty walkable path  
- **S** = Starting position
- **E** = Exit position

### Creating Custom Mazes
You can create your own maze files using any text editor:
1. Use # for walls and spaces for paths
2. Place one 'S' for start and one 'E' for exit
3. Save as .txt file starting with "maze" (e.g., maze1.txt)

## Features

- File browser to list available maze files
- Input validation for moves and files
- Automatic pathfinding until branch points
- Clean console display that updates with each move
- Exit detection and victory message

## Technical Details

- Pure Python implementation using only standard library
- Text-based graphics using Unicode block characters
- Coordinate-based maze representation
- No external dependencies required

Perfect for puzzle enthusiasts who enjoy navigation challenges!
