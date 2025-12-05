# Rotating Cube

A 3D wireframe cube animation rendered in the terminal using ASCII characters.

## Improvements

-   **Flicker-Free Rendering**: Uses ANSI escape codes instead of clearing the screen for smoother animation.
-   **Optimized Drawing**: Uses a character buffer and Bresenham's line algorithm for efficient rendering.
-   **Clean Code**: Simplified logic with no global state and clear separation of concerns.

## How It Works

The program calculates the 3D coordinates of a cube's vertices, applies rotation matrices, projects them onto a 2D plane, and draws lines between them.

## Usage

Run the script to see the animation:
`python main.py`

Press `Ctrl-C` to stop.
