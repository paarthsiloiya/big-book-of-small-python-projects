# Conway's Game of Life - A Cellular Automaton Simulation

Welcome to **Conway's Game of Life**, a mesmerizing zero-player game that simulates the evolution of life through simple mathematical rules. Created by mathematician John Conway in 1970, this cellular automaton demonstrates how complex, life-like patterns can emerge from remarkably simple rules.

## What is the Game of Life?

Despite its name, this isn't really a "game" in the traditional sense—it's a simulation. You set up an initial configuration of living cells, and then watch as they evolve according to fixed rules, creating fascinating patterns that can grow, shrink, move, or even create new structures entirely on their own.

## How to Play

### Setting Up the Initial State

When you start the program, you'll enter the **Interactive Drawing Mode** where you can create your initial pattern:

1. **Manual Cell Placement**: Enter coordinates as `x,y` to toggle individual cells on/off (e.g., `30,10`)
2. **Random Generation**: Type `random` to fill the grid with a random pattern (20% alive cells by default)
3. **Clear the Board**: Type `clear` to remove all cells and start fresh
4. **Start Simulation**: Type `done` when you're ready to watch your creation come to life

The grid is displayed inside a bordered box with coordinates ranging from `x(0-59)` and `y(0-19)`.

### Watching the Simulation

Once you've set up your initial pattern and typed `done`, the simulation begins:

- The screen updates every 0.2 seconds showing each new generation
- Living cells are shown as solid blocks: `██`
- Dead cells are shown as empty spaces
- The generation number and living cell count are displayed at the top
- Press `Ctrl+C` at any time to stop the simulation

## The Rules of Life

The game follows four elegant rules that determine whether each cell lives, dies, or is born:

1. **Underpopulation**: A living cell with fewer than 2 living neighbors dies (as if by loneliness)
2. **Survival**: A living cell with 2 or 3 living neighbors survives to the next generation
3. **Overpopulation**: A living cell with more than 3 living neighbors dies (as if by overcrowding)
4. **Reproduction**: A dead cell with exactly 3 living neighbors becomes alive (as if by reproduction)

Each cell has 8 neighbors (horizontally, vertically, and diagonally adjacent cells). The grid wraps around at the edges, so cells on the left edge neighbor cells on the right edge, and top neighbors bottom.

## Famous Patterns to Try

### Still Lifes (Stable Patterns)
These patterns don't change from generation to generation.

**Block** - The simplest still life:
```
Coordinates: (10,10), (11,10), (10,11), (11,11)
██ ██
██ ██
```

**Beehive** - A hexagonal shape:
```
Coordinates: (10,10), (11,10), (9,11), (12,11), (10,12), (11,12)
   ██ ██
██       ██
   ██ ██
```

### Oscillators (Repeating Patterns)

**Blinker** - Period 2 (switches between horizontal and vertical):
```
Coordinates: (10,10), (10,11), (10,12)
Generation 1:    Generation 2:
██               
██               ██ ██ ██
██               
```

**Toad** - Period 2:
```
Coordinates: (10,10), (11,10), (12,10), (9,11), (10,11), (11,11)
   ██ ██ ██
██ ██ ██
```

### Spaceships (Moving Patterns)

**Glider** - The smallest spaceship, moves diagonally:
```
Coordinates: (10,10), (11,11), (9,12), (10,12), (11,12)
   ██
      ██
██ ██ ██
```

**Lightweight Spaceship (LWSS)** - Travels horizontally:
```
Coordinates: (10,10), (13,10), (9,11), (9,12), (13,12), (9,13), (10,13), (11,13), (12,13)
   ██       ██
██
██          ██
██ ██ ██ ██
```

## Customization

You can modify these constants at the top of the code to customize your experience:

- **WIDTH**: Width of the grid (default: 60)
- **HEIGHT**: Height of the grid (default: 20)
- **ALIVE**: Character used for living cells (default: `'██'`)
- **DEAD**: Character used for dead cells (default: `'  '`)
- **ALIVE_RATIO**: Probability of cells being alive during random generation (default: 0.2 or 20%)
