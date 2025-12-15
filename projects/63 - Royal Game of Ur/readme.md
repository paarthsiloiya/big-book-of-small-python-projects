# Royal Game of Ur

A digital recreation of the ancient Mesopotamian board game, dating back 5,000 years. Race your opponent to get all seven tokens to the goal first!

## How to Play

1. Run the game: `python main.py`
2. Players take turns flipping 4 coins to determine movement (0-4 spaces).
3. **X** and **O** compete to move tokens from Home to Goal.

## Rules

- **Movement**: Move tokens based on coin flips.
- **Capture**: Landing on an opponent's token sends it back to their Home.
- **Safety**: The center flower space (l) is safe; tokens there cannot be captured.
- **Rosettes (Flowers)**: Landing on a flower space grants an extra turn.
- **Winning**: The first player to move all 7 tokens off the board wins.

## Board Map

```
      X Home      X Goal
        v           ^
  +---+-v-+---+---+-^-+---+
  | h | g | f | e | t | s |
  +---+-v-+---+---+-^-+---+
  | i | j | k | l | m | n | o | p |
  +---+-^-+---+---+-v-+---+
  | d | c | b | a | r | q |
  +---+-^-+---+---+-v-+---+
        ^           v
      O Home      O Goal
```

## Controls

- Press **Enter** to roll.
- Type the letter of the space to move a token from (e.g., `a`, `b`, `home`).
- Type `quit` to exit.
