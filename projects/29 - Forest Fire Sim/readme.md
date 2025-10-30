# Forest Fire Simulation 🔥🌲

A dynamic cellular automaton that simulates the natural cycle of forest growth and wildfire spread in your terminal. Watch as trees grow, lightning strikes, and fires cascade through the forest ecosystem!

## Features

- **Natural Growth**: Empty spaces have a 1% chance per generation to grow new trees
- **Lightning Strikes**: Trees have a 1% chance per generation to be struck by lightning
- **Fire Spreading**: Fires naturally spread to all adjacent trees (including diagonally)
- **Ecosystem Cycles**: Fires burn out after one generation, creating space for new growth
- **Optimized Display**: Only updates changed cells for smooth, flicker-free animation
- **Terminal Adaptive**: Automatically detects and uses full terminal dimensions
- **Emoji Graphics**: Beautiful 🌲 trees and 🔥 fire emojis for visual appeal

## How It Works

The simulation follows simple but powerful rules that create complex, realistic fire behavior:

### Growth Rules
- **Tree Growth**: Each empty space has a 1% chance to sprout a new tree each generation
- **Lightning Strike**: Each tree has a 1% chance to be struck by lightning and catch fire

### Fire Rules
- **Fire Spread**: Any tree adjacent to a fire (horizontally, vertically, or diagonally) will catch fire
- **Burnout**: Fires automatically burn out after one generation, leaving empty space
- **Dense vs Sparse**: Dense forests experience larger fires, while sparse forests have smaller, isolated burns

## Requirements

- Python 3.x
- `bext` library for terminal graphics (automatically installed if missing)

## Display

- **🌲 Green Trees**: Healthy, living trees
- **🔥 Red Fires**: Active fires spreading through the forest
- **Empty Spaces**: Cleared areas where new trees can grow
- **Generation Counter**: Shows current simulation step and controls

## Simulation Behavior

### Typical Patterns
- **Sparse Growth**: In empty areas, trees slowly populate the landscape
- **Fire Outbreaks**: Lightning strikes create fire seeds that spread locally
- **Burn Cycles**: Dense forest areas experience periodic large fires
- **Recovery**: Burned areas gradually regrow, creating natural cycles

### Interesting Dynamics
- **Edge Effects**: Fires at forest edges burn out faster than interior fires
- **Fragmentation**: Large fires create fragmented forest patches
- **Equilibrium**: The simulation reaches a dynamic balance between growth and destruction
- **Density Dependent**: Fire size correlates with local tree density

## Technical Features

- **Efficient Rendering**: Only redraws cells that changed between generations
- **No Flickering**: Uses cursor positioning instead of screen clearing
- **Responsive Size**: Adapts to any terminal dimensions
- **Hidden Cursor**: Smooth animation without cursor interference
