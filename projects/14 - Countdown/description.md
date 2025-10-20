# Countdown Timer - Seven-Segment Display

Welcome to **Countdown Timer**, a visually stunning terminal-based countdown clock that displays time using beautiful seven-segment display digits, just like classic digital clocks and timers!

## What is This?

This program transforms your terminal into a large, easy-to-read countdown timer. Instead of plain text numbers, it uses ASCII art to render seven-segment display digits—the same style used in digital alarm clocks, microwave ovens, and electronic scoreboards. Watch as the seconds tick down in style!

## How to Use

1. **Start the Program**: Run the script and you'll be prompted to enter a countdown duration
2. **Enter Seconds**: Type in how many seconds you want to count down from (e.g., `60` for one minute, `3600` for one hour)
3. **Watch the Countdown**: The timer will display in large seven-segment digits showing hours:minutes:seconds format
4. **Stop Early**: Press `Ctrl+C` if you need to stop the countdown before it finishes

## Display Format

The timer shows time in `HH:MM:SS` format:
- **HH**: Hours (00-99)
- **MM**: Minutes (00-59)
- **SS**: Seconds (00-59)

### Example Display

When counting down from 65 seconds, you'll see:
```
┌───┐  ┌───┐       ┌───┐     ────┐       ┌───┐  ┌────  
│   │  │   │       │   │         │       │   │  │      
│   │  │   │       │   │     ┌───┘       │   │  └───┐  
│   │  │   │       │   │     │           │   │      │  
└───┘  └───┘       └───┘     └────       └───┘  ────┘  
```