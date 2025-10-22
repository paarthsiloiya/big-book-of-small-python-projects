# Dice Math - Bouncing Dice Addition Quiz

Welcome to **Dice Math**, a fast-paced addition quiz with a twist! Watch as beautifully rendered ASCII dice bounce around the screen, colliding with walls and each other. When they stop, your challenge is to add up all the visible faces before time runs out.

## How to Play

1.  **Start the Game**: Press Enter to begin.
2.  **Watch the Dice Roll**: For 5 seconds, between 2 and 6 dice will bounce around the screen. Their faces change with every collision.
3.  **Add Them Up**: Once the dice stop, you have 30 seconds to add up the values of all the visible faces.
4.  **Enter Your Answer**: Type your answer and press Enter.
5.  **Check Your Score**: The game will tell you if you were correct and show the right answer.

## Visuals

The game takes place inside a bordered canvas where dice, rendered with detailed ASCII art, move around.

### Example of a Die (Face 5)
```
┌───────┐
│ ●   ● │
│   ●   │
│ ●   ● │
└───────┘
```

## Features

### Dynamic Bouncing Animation
Dice move diagonally across the screen, creating a lively and engaging visual before the quiz begins.

### Collision Detection
Dice realistically bounce off the walls and, more importantly, off each other, making the rolling phase unpredictable.

### Random Face Changes
When a die collides with a wall or another die, its face randomly changes, so you can't just track one die.

### Timed Quiz
You have 30 seconds to answer, adding a fun layer of pressure to the challenge.

### Randomized Rounds
The number of dice changes each round (from 2 to 6), so you never know how difficult the next quiz will be.

## Game Rules

-   When a die hits a wall, it reverses its direction and its face changes.
-   When two dice collide, they both reverse direction and their faces change.
-   A die's face will never change to its opposite side (e.g., a 1 won't become a 6, a 2 won't become a 5), adding a subtle touch of realism.

## Customization

You can modify these constants at the top of the code to change the game's difficulty and feel:

-   **MIN_DICE / MAX_DICE**: The range for the number of dice in each round (default: 2-6).
-   **QUIZ_DURATION**: How many seconds you have to answer (default: 30).
-   **ROLLING_DURATION**: How long the dice bounce before stopping (default: 5 seconds).
-   **PAUSE_TIME**: The pause between each frame of the animation. A smaller number makes the dice move faster.

## Technical Details

-   The `bext` library is used to position the cursor and draw the dice anywhere in the terminal, allowing for the animation.
-   The game uses `threading` to run a timer for user input, so the quiz doesn't wait forever for an answer.

This game is a great test of your attention and quick mental math skills, wrapped in a fun, animated package!