# Flooder - Color Flood Strategy Game

Fill the entire board with a single color in this addictive **flood fill puzzle game**! Starting from the top-left corner, strategically choose colors to expand your territory and conquer the board within limited moves. A perfect blend of strategy and satisfying visual feedback.

## What This Program Does

This engaging puzzle game challenges your strategic thinking:

- **Flood Fill Mechanics**: Choose colors to expand your controlled area from the top-left corner
- **Strategic Gameplay**: Limited moves (20) force careful planning and efficient choices
- **Colorblind Support**: Switch between color mode and shape mode for accessibility
- **Visual Feedback**: Colorful terminal display with Unicode characters and borders
- **Win/Lose Conditions**: Complete the board or run out of moves

## How to Play

### Game Objective
Fill the entire 16×14 board with a single color starting from the top-left corner (marked with `>`).

### Game Mechanics
1. **Choose a Color**: Select from 6 colors (Red, Green, White, Yellow, Blue, Pink)
2. **Flood Adjacent**: Your chosen color spreads to all connected tiles of the same color
3. **Expand Territory**: The flooded area grows, allowing you to reach new regions
4. **Strategic Planning**: Look for colors that connect separate regions efficiently

### Controls
- **Color Mode**: R(ed), G(reen), W(hite), Y(ellow), B(lue), P(ink)
- **Shape Mode**: H(eart), T(riangle), D(iamond), B(all), C(lub), S(pade)
- **QUIT**: Exit the game at any time

## Strategy Tips

- **Connect Regions**: Choose colors that bridge gaps between your current area and isolated regions
- **Maximize Coverage**: Pick colors that appear most frequently adjacent to your territory
- **Plan Ahead**: Consider which color choices will open up the most future possibilities
- **Corner Strategy**: Focus on reaching corners and edges to maximize flooding potential

## Features

### Accessibility
- **Colorblind Mode**: Uses distinct shapes instead of colors for better accessibility
- **Clear Interface**: High-contrast borders and intuitive controls
- **Visual Indicators**: Current position marked with `>` symbol

### Game Design
- **Balanced Difficulty**: 20 moves provides challenging but achievable gameplay
- **Random Boards**: Each game features a procedurally generated unique board
- **Instant Feedback**: Immediate visual response to your color choices

## Perfect For

- **Puzzle Enthusiasts**: Strategic thinking and pattern recognition
- **Casual Gaming**: Quick, satisfying gameplay sessions
- **Accessibility**: Colorblind-friendly shape mode available
- **Programming Study**: Example of flood fill algorithms and game logic

## Sample Gameplay

```
Choose one of (R)ed (G)reen (W)hite (Y)ellow (B)lue (P)ink or QUIT:
> R
Moves left: 19

[Board updates with red flood fill from top-left corner]

Choose one of (R)ed (G)reen (W)hite (Y)ellow (B)lue (P)ink or QUIT:
> G
Moves left: 18
```

Win by filling the entire board before your 20 moves run out!