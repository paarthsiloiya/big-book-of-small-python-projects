# Dice Roller - A Tabletop RPG Companion

Welcome to **Dice Roller**, a command-line tool that simulates rolling dice for tabletop role-playing games (RPGs) like Dungeons & Dragons. It understands standard dice notation, allowing you to roll any number of dice with any number of sides, and even add modifiers.

## How to Use

When you run the program, you'll see a `>` prompt. Enter your desired dice roll in the format `XdY[+Z]` or `XdY[-Z]`.

-   `X` is the number of dice to roll.
-   `Y` is the number of sides on each die.
-   `Z` is an optional modifier to add or subtract from the total.

To quit the program, simply type `q`.

### Command Format

-   **Roll dice**: `2d6` (Rolls two 6-sided dice)
-   **Roll with a positive modifier**: `1d20+5` (Rolls one 20-sided die and adds 5)
-   **Roll with a negative modifier**: `3d8-2` (Rolls three 8-sided dice and subtracts 2)

The program ignores spaces, so `2d6 + 3` is the same as `2d6+3`.

## Example Session

```
> 2d6
Rolling 2d6+0:
4, 1
 = 5
> 1d20+4
Rolling 1d20+4:
18
18 + 4 = 22
> 3d8-1
Rolling 3d8-1:
7, 3, 5
15 - 1 = 14
> q
Exiting Dice Roller. Goodbye!
```

## Features

### Standard Dice Notation
The roller understands the universal `XdY` format used in most tabletop RPGs.

### Positive and Negative Modifiers
Easily add bonuses or penalties to your rolls with `+` or `-`.

### Detailed Breakdown
The output shows you the result of each individual die roll before giving you the final total, ensuring transparency in your results.

### Simple and Fast
No complex menus or commands. Just type your roll and get an instant result.

### Robust Error Handling
If you enter an invalid command, the program will tell you what went wrong without crashing. For example: `Invalid input! Number of sides is missing`.

## Common RPG Rolls

This tool is perfect for any situation in a tabletop game:

-   **Attack Roll**: `1d20+7` (Roll a d20 and add your attack bonus)
-   **Damage Roll**: `2d8+3` (Roll two d8s for weapon damage and add your strength modifier)
-   **Ability Check**: `1d20-1` (Roll a d20 for a skill check with a penalty)
-   **Fireball Spell**: `8d6` (Roll eight d6s for a massive burst of fire damage)

## How It Works

1.  **Input Parsing**: The program reads your input string and splits it to identify the number of dice, the number of sides, and any modifier.
2.  **Random Rolling**: It uses Python's `random.randint(1, num_sides)` in a loop to simulate each individual die roll.
3.  **Calculation**: The results of the rolls are summed up, and the modifier is applied.
4.  **Formatted Output**: The program prints a clear, easy-to-read summary of the rolls and the final result.

This simple yet powerful tool is a must-have for any digital RPG session, providing quick and fair dice rolls on demand.