# Four in a Row (Connect 4) - Classic Connection Strategy Game

Welcome to **Four in a Row**, also known as Connect 4! This is the timeless two-player strategy game where you compete to be the first to connect four of your pieces in a row. With beautiful box-drawing character graphics and colored pieces, this terminal version brings the classic game to life right in your console.

## How to Play

### Game Setup
1. **Enter Player Names**: Both players will be prompted to enter their names
2. **Take Turns**: Players alternate dropping colored discs into the grid
3. **Win Condition**: Be the first to connect four of your pieces in a row

### Making Your Move
- Choose a column (1-7) where you want to drop your piece
- Your piece will fall to the lowest available position in that column
- Type `quit` or `q` at any time to exit the game

## Game Features

### Color-Coded Players
- **Player 1**: Red pieces (●)
- **Player 2**: Blue pieces (●)
- **Empty Spaces**: White circles (○)

### Clear Screen Updates
The board is refreshed with each move, keeping the display clean and focused on the current game state.

## Winning Conditions

You can win by connecting four pieces in any of these ways:

### Horizontal Connection
Four pieces in a row horizontally across any row.

### Vertical Connection  
Four pieces stacked vertically in any column.

### Diagonal Connections
Four pieces connected diagonally in either direction:
- Top-left to bottom-right (\\)
- Top-right to bottom-left (/)

## Game Rules

### Valid Moves
- You can only drop pieces into columns that aren't full
- Pieces always fall to the lowest available position
- The game prevents invalid moves and prompts you to try again

### Game End Conditions
- **Victory**: First player to connect four pieces wins immediately
- **Draw**: If the board fills up with no winner, the game ends in a tie
- **Quit**: Players can exit anytime by typing 'quit' or 'q'

### Turn System
- Player 1 always goes first
- Players strictly alternate turns
- The current player's name and piece color are displayed before each turn.