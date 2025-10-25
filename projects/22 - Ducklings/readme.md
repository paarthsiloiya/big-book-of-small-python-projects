# Ducklings - Adorable ASCII Art Screensaver

Experience the charm of **adorable ASCII ducklings** waddling down your terminal screen! This delightful screensaver brings a parade of randomly generated cute ducklings, each with unique personalities, body types, and expressions, creating an endless stream of kawaii terminal art.

## What This Program Does

This heartwarming screensaver fills your terminal with procedurally generated ducklings:

- **Procedural Generation**: Every duckling is randomly created with unique characteristics
- **Personality Variations**: Each duckling has different eyes, mouth, body size, and wing positions
- **Continuous Parade**: Ducklings appear randomly and scroll down the screen continuously
- **Multi-Lane System**: Multiple ducklings can waddle down different columns simultaneously
- **Adaptive Display**: Automatically fits any terminal size for optimal viewing
- **Smooth Animation**: 5 FPS scrolling creates relaxing, gentle movement

## Visual Design

Each duckling is lovingly crafted from ASCII characters in a three-part structure:

```
Facing Left:           Facing Right:
>"") (head)           ( ""< (head)
( >) (body)           < ) (body)  
 ^^  (feet)            ^^  (feet)
```

### Duckling Anatomy

Every duckling is composed of three distinct parts that scroll down together:

#### Head Features
- **Direction**: Faces left `>` or right `<`
- **Mouth**: Open `><` or closed `=`
- **Eyes**: Beady `"`, wide `''`, happy `^^`, or aloof `` ` ``
- **Expression**: Combinations create unique personalities

#### Body Characteristics  
- **Size**: Chubby `( )` or very chubby `(  )`
- **Wings**: Out `><`, up `^`, or down `v`
- **Shape**: Parentheses form the duckling's round body

#### Feet Patterns
- **Chubby ducklings**: Wide-set feet ` ^^  `
- **Very chubby ducklings**: Closer feet ` ^ ^ `

## Features

### Personality System
Each duckling gets randomly assigned traits that work together:
- **Body-Eye Coordination**: Chubby ducklings always have beady eyes
- **Very chubby ducklings**: Can have any eye type for more variety
- **Independent Traits**: Wings and mouth positions are completely random
- **Unique Combinations**: Hundreds of possible duckling personalities

### Animation System
- **Lane-Based Movement**: Terminal width divided into 5-character duckling lanes
- **Random Spawning**: 10% chance per frame for new ducklings in empty lanes
- **Three-Frame Display**: Head → Body → Feet sequence creates full duckling
- **Smooth Scrolling**: Continuous downward movement with proper buffering

### Technical Excellence
- **Terminal Adaptation**: Uses `bext` library for professional terminal control
- **Screen Buffering**: Efficient line-by-line rendering system
- **Memory Management**: Smart buffer limiting prevents memory overflow
- **Clean Exit**: Proper cursor restoration and graceful shutdown

### Duckling Class
```python
class Duckling:
    - Randomly generates all physical traits
    - Stores direction, body type, mouth, wing, and eye states
    - Provides methods to render each body part
    - Tracks which part to display next in sequence
```

### Main Animation Loop
1. **Check Each Lane**: Randomly spawn new ducklings (10% chance)
2. **Render Frame**: Get next body part from each active duckling
3. **Buffer Management**: Add new line to screen buffer
4. **Display Update**: Print all buffered lines to terminal
5. **Cleanup**: Remove completed ducklings and excess buffer lines

### Spawning Algorithm
```python
if (ducklingObj == None and random.random() <= DENSITY):
    ducklingObj = Duckling()  # 10% spawn chance per lane per frame
```

## How to Run

Launch the adorable duckling parade:

```bash
python main.py
```

**Requirements**: The program uses the `bext` library for terminal control:
```bash
pip install bext
```

The program will:
1. Display terminal size information and instructions  
2. Clear the screen and hide cursor for clean viewing
3. Begin the infinite duckling parade
4. Continue until you press `Ctrl+C` to exit

## Perfect For

- **Stress Relief**: Watching cute ducklings is surprisingly therapeutic
- **Work Breaks**: Perfect screensaver for coding breaks
- **Presentations**: Charming way to fill time during setup
- **Learning Tool**: Great example of procedural generation and ASCII art
- **Gift**: Brighten someone's day with terminal ducklings
- **Background Ambiance**: Gentle animation while working