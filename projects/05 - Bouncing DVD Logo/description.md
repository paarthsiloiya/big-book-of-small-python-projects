# Bouncing DVD Logo - A Nostalgic Screensaver

Remember staring at old DVD players, mesmerized by the bouncing logo, waiting for that magical moment when it perfectly hits the corner? This **Bouncing DVD Logo** simulation brings back that nostalgic experience with multiple colorful logos bouncing around your terminal screen.

## What This Program Does

This animated screensaver recreates the classic DVD screensaver experience with a modern twist:

- **Multiple Logos**: Watch 5 DVD logos bounce simultaneously around your screen
- **Color Changes**: Each time a logo hits a wall, it randomly changes color
- **Realistic Physics**: Logos bounce off walls at proper angles, just like the original
- **Full Screen**: Uses your entire terminal window as the bouncing area
- **Smooth Animation**: 60+ FPS animation for satisfying, smooth movement

## The Physics Behind the Magic

The logos follow simple but satisfying physics:

1. **Diagonal Movement**: Each logo moves diagonally (up-right, up-left, down-right, or down-left)
2. **Wall Bouncing**: When a logo hits a wall, it bounces off at the correct angle
3. **Color Randomization**: Every wall collision triggers a random color change
4. **Continuous Motion**: The animation runs indefinitely until you stop it

## Features

### Visual Appeal
- **7 Colors**: Red, green, yellow, blue, magenta, cyan, and white
- **Smooth Animation**: 0.1-second intervals create fluid motion
- **Clear Trails**: Old positions are erased before drawing new ones
- **Terminal Responsive**: Automatically adapts to your terminal size

### Technical Details
- **Coordinate System**: Uses precise x,y positioning for pixel-perfect movement
- **Edge Detection**: Smart boundary checking prevents logos from disappearing
- **Direction Mapping**: Four-direction system (ur, ul, dr, dl) for clean bouncing logic
- **Even Positioning**: X-coordinates are kept even for consistent spacing

## The Corner Hit Challenge

Just like the original DVD screensaver, there's something deeply satisfying about watching for that perfect corner hit. With 5 logos bouncing around, you'll have multiple chances to witness this rare and beautiful moment!

## How to Run

Simply execute the program and watch the magic happen:

```bash
python main.py
```

The animation will fill your entire terminal window. Press `Ctrl+C` to stop the simulation.

## Requirements

This program uses the `bext` module for terminal control:

```bash
pip install bext
```

The `bext` library provides:
- Terminal clearing and cursor positioning
- Color text output
- Terminal size detection
- Cross-platform compatibility

## Customization Ideas

The code is designed to be easily customizable:

### Change the Logo
```python
LOGO = 'DVD'  # Try 'RETRO', '🎬', or any text!
```

### Adjust Speed
```python
PAUSE_TIME = 0.05  # Faster animation
PAUSE_TIME = 0.2   # Slower, more relaxed
```

### More Logos
```python
NUM_LOGOS = 10  # Chaos mode!
NUM_LOGOS = 1   # Classic single logo
```

### Different Colors
```python
COLORS = ['red', 'blue']  # Limited palette
COLORS.append('black')    # Add more colors
```