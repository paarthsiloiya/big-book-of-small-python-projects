# Langton's Ant - Advanced Cellular Automaton Simulation

Welcome to **Langton's Ant**, a mesmerizing cellular automaton that demonstrates how simple rules can create incredibly complex and beautiful patterns! Watch as virtual ants follow basic movement rules to generate emergent behaviors, highways, and chaotic formations in this enhanced terminal simulation.

## How It Works

### The Simple Rules
Each ant follows two basic rules that create infinite complexity:
- **On light tile**: Turn right, flip tile to dark, move forward
- **On dark tile**: Turn left, flip tile to light, move forward

### Extended Multi-Color Rules
Our enhanced version supports 2-7 colors with generalized behavior:
- **Even-numbered colors**: Turn left, advance color cycle
- **Odd-numbered colors**: Turn right, advance color cycle

## Simulation Presets

Choose from carefully crafted experiences:
- **CLASSIC**: Single ant traditional experience - watch highway formation
- **SWARM**: 10 ants creating complex interactions and interference patterns  
- **RAINBOW**: Multi-colored tiles producing stunning visual effects
- **CHAOS**: 25 high-speed ants generating maximum complexity
- **SLOW_MOTION**: Detailed observation of individual ant decision-making
- **CUSTOM**: Design your own parameters (1-50 ants, 2-7 colors, custom speed)

## Advanced Features

### Visual Excellence
- **Flicker-free animation** using optimized bext library rendering
- **Color-coded ants** with unique directional sprites (▲▼►◄)
- **Multi-color tiles** with distinct patterns and shading
- **Real-time statistics** showing steps, time, and performance metrics
- **Fixed status display** that updates in place without scrolling

### Emergent Behaviors
- **Highway Formation**: Single ants eventually create repeating diagonal paths
- **Collision Effects**: Multiple ants create interference and new pattern types
- **Symmetric Structures**: Complex geometric forms emerge from chaos
- **Periodic Cycles**: Watch patterns stabilize into repeating sequences

### Technical Implementation
- **Efficient Rendering**: Only updates changed screen positions for smooth performance
- **Wrap-around Grid**: Ants continue seamlessly when reaching screen edges
- **Individual Tracking**: Each ant maintains step counts and directional state
- **Performance Monitoring**: Real-time FPS and computation statistics

## Controls & Usage

- **Run the program** and select from preset simulations or create custom settings
- **Watch the magic** as simple rules create complex, beautiful patterns
- **Press Ctrl+C** to stop and view detailed statistics about the simulation
- **Experiment** with different ant counts and color schemes for varied results

Perfect for mathematics enthusiasts, complexity theory students, and anyone fascinated by emergent behavior and computational beauty!