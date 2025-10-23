# Digital Clock - A Seven-Segment Display Terminal Clock

Experience the nostalgia of classic digital displays with this **Digital Clock** that renders the current time using beautiful seven-segment ASCII art. Watch as the time updates every second with crisp, retro-style digits that look just like old calculator and clock displays.

## What This Program Does

This animated clock brings the classic seven-segment display aesthetic to your terminal:

- **Real-Time Display**: Shows current hours, minutes, and seconds (HH:MM:SS format)
- **Seven-Segment Rendering**: Each digit is drawn using Unicode box-drawing characters
- **Auto-Refresh**: Updates every second with smooth screen clearing
- **24-Hour Format**: Displays time in 24-hour format with leading zeros
- **Terminal Clock**: Perfect as a large, easy-to-read terminal clock

## Visual Design

The clock uses elegant Unicode box-drawing characters to create authentic seven-segment displays:

```
┌───┐  ┌───┐       ┌───┐  ──┐       ┌───┐  ┌───┐
│   │  │   │   ░   │   │    │   ░   │   │  │   │
│   │  └───┤       │   │    │       │   │  ├───┤
│   │      │   ░   │   │    │   ░   │   │  │   │
└───┘  ────┘       └───┘  ──┴──     └───┘  └───┘
```

### Character Mapping

Each digit (0-9) is represented by a unique five-line pattern:
- **Horizontal segments**: `─` (top/middle/bottom)
- **Vertical segments**: `│` (left/right sides)
- **Corners**: `┌┐└┘` (rounded corners)
- **Junctions**: `├┤┬┴` (where segments meet)
- **Colon separator**: `░` (block character for time separators)
