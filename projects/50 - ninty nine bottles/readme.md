# 99 Bottles of Milk 🍼

A simple animated implementation of the classic "99 Bottles" counting song with timing delays for a rhythmic experience.

## What It Does

This program displays the traditional counting song that counts down from 99 bottles to zero, with each verse following the pattern:

```
99 bottles of milk on the wall,
99 bottles of milk,
Take one down, pass it around,
98 bottles of milk on the wall!
```

## Features

- **Animated Display**: Each line appears with a 2-second delay for a song-like rhythm
- **Complete Countdown**: Counts from 99 bottles all the way down to zero
- **Special Final Verse**: Handles the last bottle with appropriate singular/plural grammar
- **Graceful Exit**: Can be stopped anytime with Ctrl+C

## How to Run

```bash
python main.py
```

The program will start automatically and display each verse with timed pauses. The complete song takes about 13 minutes to finish (99 verses × 4 lines × 2 seconds per line).

## Controls

- **Ctrl+C**: Stop the song at any time and exit gracefully

## Implementation Details

- Uses `time.sleep(2)` for 2-second pauses between lines
- Handles the transition from plural "bottles" to singular "bottle" at the end
- Includes proper exception handling for keyboard interrupts
