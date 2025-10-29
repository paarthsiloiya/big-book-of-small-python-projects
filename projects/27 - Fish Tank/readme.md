# Fish Tank Aquarium Simulation 🐠

A beautiful ASCII art aquarium simulation that creates a living, breathing underwater world in your terminal!

## Features

- **Multiple Fish Types**: Small and big fish with different ASCII art sprites
- **Animated Movement**: Fish swim left and right, changing direction at terminal boundaries
- **Seaweed Animation**: Swaying seaweed with realistic movement
- **Bubble Effects**: Fish occasionally exhale bubbles that float to the surface
- **Dynamic Colors**: Colorful fish, green seaweed, and white bubbles
- **Responsive Design**: Automatically detects terminal size and adapts
- **Water Effects**: Occasional ripples for added realism

## Requirements

- Python 3.x
- `bext` library for terminal graphics

## Installation

Install the required library:
```bash
pip install bext
```

## Usage

Run the aquarium simulation:
```bash
python main.py
```

Press `Ctrl+C` to exit the aquarium.

## Features Detail

### Fish
- **Small Fish**: `<°)))><` (swimming right), `><(((°>` (swimming left)
- **Big Fish**: `<°))))))><` (swimming right), `><((((((°>` (swimming left)
- Fish change direction when they reach the terminal edges
- Each fish has a random color (yellow, cyan, magenta, red)
- Fish occasionally generate bubbles

### Seaweed
- Animated swaying motion
- Different heights for variety
- Green colored for realism
- Positioned at the bottom of the aquarium

### Bubbles
- Generated randomly by fish
- Float upward with slight horizontal drift
- Different bubble characters: `o`, `O`, `°`
- Disappear when they reach the surface

### Aquarium Border
- Blue border frames the aquarium
- Adjusts to terminal size
- Minimum size requirement: 40x15 characters

## Customization

You can easily customize the aquarium by modifying:
- Number of fish in the `Aquarium.__init__()` method
- Fish colors in the `FISH_COLORS` list
- Animation speed by changing the `time.sleep()` value
- Bubble generation frequency in the `Fish.should_bubble()` method

Enjoy your virtual aquarium! 🌊🐟🌱