# Sudoku

The classic 9x9 number placement puzzle.

## How to Play

1.  The goal is to fill the 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contain all of the digits from 1 to 9.
2.  Some numbers are already filled in and cannot be changed.
3.  Enter your move by specifying the column (A-I), row (1-9), and the number (1-9).

## Controls

-   **Move**: Enter coordinate and number, e.g., `A1 5` puts 5 in top-left corner.
-   `NEW`: Start a new random puzzle.
-   `RESET`: Restart the current puzzle.
-   `UNDO`: Undo the last move.
-   `QUIT`: Exit the game.

## Example

```
    A B C   D E F   G H I
  ┌───────┬───────┬───────┐
1 │ 5 3   │   7   │       │
2 │ 6     │ 1 9 5 │       │
3 │   9 8 │       │   6   │
  ├───────┼───────┼───────┤
4 │ 8     │   6   │     3 │
...
```
