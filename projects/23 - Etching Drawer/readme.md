# Etching Drawer - Terminal-Based Line Art Creator

Create beautiful **ASCII line art** directly in your terminal with this interactive drawing program! Inspired by classic Etch A Sketch toys, this digital version uses Unicode box-drawing characters to let you create stunning geometric patterns, designs, and artwork using simple WASD keyboard controls.

## What This Program Does

This creative drawing tool transforms your terminal into an artistic canvas:

- **Interactive Drawing**: Use WASD keys to move a cursor and draw connected lines
- **Unicode Box Characters**: Creates smooth, professional-looking line art with proper connections
- **Smart Line Connections**: Automatically chooses the correct Unicode character for each intersection
- **Full Terminal Canvas**: Uses your entire terminal window as drawing space
- **Save Functionality**: Export your artwork to text files for sharing or archiving
- **Command History**: Records all your moves for replay and saving

### Unicode Line Characters

The program intelligently selects the appropriate character for each position:

- **Straight Lines**: `│` (vertical) and `─` (horizontal)
- **Corners**: `┌` `┐` `└` `┘` for 90-degree turns
- **T-Junctions**: `├` `┤` `┬` `┴` for three-way intersections  
- **Cross**: `┼` for four-way intersections
- **Current Position**: `#` marks where your cursor is located


## Features

### Intelligent Drawing System
- **Direction Tracking**: Each cell remembers which directions have lines through it
- **Automatic Connections**: Lines automatically connect when paths cross
- **Boundary Protection**: Prevents drawing outside the canvas area
- **Cursor Visibility**: Always shows your current position with `#`

### Professional Output
- **Unicode Rendering**: Smooth, publication-quality line art
- **Proper Intersections**: All line connections are geometrically correct
- **Clean Borders**: Professional-looking canvas frame
- **Terminal Adaptation**: Automatically sizes to fit your terminal

### Creative Tools
- **Freeform Drawing**: Move in any direction to create organic shapes
- **Geometric Patterns**: Perfect for creating boxes, mazes, and abstract designs
- **Continuous Lines**: Lines connect seamlessly as you draw
- **Pattern Building**: Create complex designs by layering simple shapes

## Controls

The program uses intuitive WASD controls for movement:

### Movement Keys
- **W**: Move cursor up and draw a vertical line
- **A**: Move cursor left and draw a horizontal line  
- **S**: Move cursor down and draw a vertical line
- **D**: Move cursor right and draw a horizontal line

### Command Keys
- **H**: Display help information with detailed instructions
- **C**: Clear the entire canvas and start fresh
- **F**: Save your artwork to a text file
- **Q**: Quit the program