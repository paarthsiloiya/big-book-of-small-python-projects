# Digital Stream - Matrix-Style Rain Effect

Experience the iconic **Matrix digital rain** effect right in your terminal! This mesmerizing animation recreates the famous green cascading code from the Matrix movies, filling your screen with streams of glowing characters that fall continuously down your terminal.

## What This Program Does

This stunning visual effect transforms your terminal into a Matrix-style digital world:

- **Cascading Streams**: Multiple columns of characters falling at different speeds
- **Dynamic Characters**: Mix of numbers, letters, and symbols that change randomly
- **Color Gradients**: White to light green to dark green fade effect for authentic look
- **Full Screen**: Automatically adapts to your terminal size for complete coverage
- **Smooth Animation**: Optimized 50 FPS rendering with minimal CPU usage
- **Random Variation**: Each stream has unique length, speed, and character patterns

## Visual Design

The effect creates the iconic Matrix digital rain with three distinct visual layers:

```
Character Set: "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?"

Color Scheme:
WHITE       - Leading character (brightest)
LIGHT_GREEN - First third of stream  
GREEN       - Trailing characters (darkest)
```

### Stream Properties

Each column creates an independent digital stream with:
- **Variable Length**: 5-25 characters per stream
- **Multiple Speeds**: 1x, 2x, or 3x movement rates
- **Character Mutation**: 30% chance of random character changes per frame
- **Continuous Flow**: Streams regenerate automatically when they exit the screen

## Features

### Authentic Matrix Effect
- **Gradient Colors**: White lead fades through light green to dark green
- **Random Characters**: Constantly changing alphanumeric and symbol characters
- **Variable Speeds**: Multiple streams moving at different rates for organic feel
- **Screen Wrapping**: Seamless regeneration maintains continuous flow

### Performance Optimized
- **Differential Rendering**: Only redraws changed characters for smooth performance
- **Memory Efficient**: Smart screen buffering prevents unnecessary updates
- **Cross-Platform**: Works on Windows, macOS, and Linux terminals
- **ANSI Terminal Control**: Professional cursor and screen management

### Terminal Integration
- **Auto-Sizing**: Detects and adapts to any terminal dimensions
- **Clean Exit**: Proper cursor restoration and screen clearing on exit
- **Keyboard Interrupt**: Graceful shutdown with Ctrl+C
- **Hidden Cursor**: Immersive fullscreen experience

## How It Works

The program uses an object-oriented approach to manage the digital rain:

### Stream Management
```python
class DigitalStream:
    - Multiple independent character streams
    - Each stream tracks position, speed, length, and characters
    - Automatic regeneration when streams exit screen
```

### Rendering Pipeline
1. **Update Phase**: Move streams, mutate characters, handle boundaries
2. **Color Assignment**: Apply white → light green → green gradient
3. **Differential Draw**: Only redraw changed screen positions
4. **Frame Rate Control**: 50 FPS with 0.02-second intervals

## How to Run

Launch the Matrix digital rain effect:

```bash
python main.py
```

The program will:
1. Display terminal information and startup message
2. Clear the screen and hide the cursor
3. Begin the infinite digital rain animation
4. Continue until you press `Ctrl+C` to exit


## Technical Details

### Color Codes
```python
GREEN = '\033[92m'        # ANSI bright green
LIGHT_GREEN = '\033[32m'  # ANSI standard green  
WHITE = '\033[97m'        # ANSI bright white
RESET = '\033[0m'         # Reset to default
```

### Terminal Control
```python
'\033[?25l'  # Hide cursor
'\033[?25h'  # Show cursor
'\033c'      # Clear screen
'\033[y;xH'  # Position cursor at row y, column x
```

## Customization Ideas

The code is designed for easy modification:

### Speed Control
```python
time.sleep(0.01)  # Faster animation (100 FPS)
time.sleep(0.05)  # Slower animation (20 FPS)
```

### Character Sets
```python
# Numbers only
STREAM_CHARS = "0123456789"

# Japanese katakana for authentic Matrix look
STREAM_CHARS = "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワン"

# Binary only
STREAM_CHARS = "01"
```

### Colors
```python
# Blue theme
BLUE = '\033[94m'
CYAN = '\033[96m'
WHITE = '\033[97m'

# Red theme for dangerous Matrix
RED = '\033[91m'
YELLOW = '\033[93m'
WHITE = '\033[97m'
```

### Stream Density
```python
# Fewer streams (every 2nd column)
for x in range(0, width, 2):

# More streams with offset patterns
for x in range(width):
    if x % 3 == 0:  # Every 3rd column
```