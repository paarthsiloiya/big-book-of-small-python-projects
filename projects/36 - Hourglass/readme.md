# Hourglass - Animated Sand Physics Simulation

Welcome to **Hourglass**, a mesmerizing sand physics simulation that brings the classic hourglass to life in your terminal! Watch thousands of sand particles cascade through an hourglass shape, following realistic physics as they fall, pile up, and create natural formations in this captivating ASCII animation.

## How It Works

### The Physics Engine
Each grain of sand follows realistic physics rules:
- **Gravity**: Sand falls straight down when possible
- **Lateral Movement**: When blocked, sand slides left or right diagonally
- **Pile Formation**: Sand naturally accumulates into realistic mounds
- **Wide Falls**: Occasionally sand can jump two spaces for natural spreading

### Visual Experience
- **Smooth Animation**: Continuous 60fps-style movement with configurable speed
- **ASCII Graphics**: Uses block characters to create detailed hourglass walls and sand
- **Color Coding**: Yellow sand particles contrast against dark hourglass walls
- **Cross-Platform**: Works on Windows, macOS, and Linux terminals

## Interactive Features

### Real-Time Simulation
- **Dynamic Physics**: Every sand grain is individually simulated each frame
- **Random Behavior**: Sand movement includes realistic randomization
- **Collision Detection**: Particles interact with walls and each other
- **Continuous Loop**: When sand stops flowing, the hourglass automatically resets

### Customizable Parameters
You can modify constants at the top of the code to customize the experience:
- **PAUSE_LENGTH**: Control animation speed (0.0 for fastest, 1.0 for slow motion)
- **WIDE_FALL_CHANCE**: Adjust how often sand spreads wider (0-100%)
- **Screen Dimensions**: Adapt to different terminal sizes

## Technical Implementation

### Advanced Algorithms
- **Particle System**: Manages thousands of individual sand grains efficiently  
- **Collision Detection**: Fast algorithms check walls and particle interactions
- **Randomized Processing**: Sand grains are shuffled each frame for natural behavior
- **Memory Optimization**: Uses sets for O(1) collision detection performance

### Terminal Graphics
- **ANSI Escape Sequences**: Direct cursor control for smooth animation
- **Buffer Management**: Efficient screen updates without flicker
- **Cross-Platform Compatibility**: Handles different terminal capabilities gracefully

## Controls

- **Start**: Run the program to begin the mesmerizing sand animation
- **Watch**: Enjoy the hypnotic falling sand and natural physics
- **Exit**: Press `Ctrl+C` to stop the simulation and exit cleanly

Perfect for relaxation, studying physics concepts, or simply enjoying beautiful terminal art. The realistic sand behavior and continuous animation create an almost meditative experience!