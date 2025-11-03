# Hex Grid - Terminal Hexagonal Pattern Generator

Welcome to **Hex Grid**, a mesmerizing ASCII art generator that creates beautiful hexagonal patterns in your terminal! This program automatically detects your terminal size and offers multiple stunning hexagon tessellation patterns that adapt perfectly to your screen dimensions.

## How to Use

### Getting Started
1. Run the program and it automatically detects your terminal size
2. Choose from the menu of available hex patterns
3. Watch as beautiful geometric patterns fill your entire screen
4. Return to menu to try different patterns or exit when done

### Available Patterns

**Pattern 1 - Classic Tessellation**
The traditional interlocking hexagon pattern using simple ASCII characters:
```
/ \_/ \_/ \_/ \_
\_/ \_/ \_/ \_/
/ \_/ \_/ \_/ \_
```

## Special Features

### Adaptive Sizing
- **Terminal Detection**: Automatically measures your terminal dimensions
- **Smart Scaling**: Calculates optimal pattern repetition for your screen
- **No Overflow**: Patterns are sized to fit perfectly without text wrapping

### Interactive Menu
- **Clean Interface**: Bordered menu with clear options
- **Multiple Views**: Option to see all patterns at once for comparison
- **Easy Navigation**: Simple number selection with error handling

### Bonus Animation
- **Animated Pattern**: Watch hexagons come alive with rotating symbols
- **Dynamic Effects**: 20-frame animation cycle with different pattern fills
- **Visual Appeal**: Combines movement with geometric beauty

## Technical Details

The program uses intelligent algorithms to:
- Calculate hexagon dimensions based on ASCII character spacing
- Determine maximum repetitions that fit in terminal bounds
- Handle edge cases for very small or unusually sized terminals
- Provide fallback dimensions if terminal size detection fails

Perfect for terminal art enthusiasts, geometry lovers, and anyone who appreciates the mathematical beauty of hexagonal tessellations!