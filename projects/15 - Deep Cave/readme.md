# Deep Cave - Endless Tunnel Animation

Welcome to **Deep Cave**, a mesmerizing endless tunnel animation that creates the illusion of descending deeper and deeper into a mysterious cave. Watch as the walls shift and narrow, creating a hypnotic scrolling effect in your terminal!

## How It Works

When you run the program, you'll see walls made of dense Unicode characters scrolling down your screen, creating the appearance of traveling through a tunnel. The gap between the walls randomly widens and narrows as you "descend," making each journey unique and unpredictable.

## Features

### Endless Animation
The cave goes on forever! The program runs continuously until you stop it with `Ctrl+C`, creating an infinite descent into the depths.

### Dynamic Tunnel Width
The gap between the walls randomly changes:
- Has a 1 in 6 chance to narrow (minimum width: 2 characters)
- Has a 1 in 6 chance to widen (maximum width: WIDTH - 2 characters)
- Otherwise maintains its current width

This randomness ensures the tunnel feels organic and unpredictable.

### Smooth Scrolling
The animation runs at a carefully tuned speed (0.05 seconds per line) to create smooth, comfortable scrolling that's easy on the eyes.

### Dense Wall Rendering
Uses the Unicode character `⣿` (Braille Pattern Full Block) to create solid, dense-looking cave walls that clearly define the tunnel boundaries.

## Tips for Best Experience

1. **Full Screen**: Maximize your terminal window for the full effect
2. **Dark Theme**: The dense wall characters look best on a dark background
3. **Sit Back**: This is a passive animation—just watch and relax
4. **Background Display**: Perfect for ambient display on a spare monitor
5. **Adjust Speed**: Modify `PAUSE_TIME` to find your preferred pace

## The Illusion of Motion

What makes this animation compelling is its simplicity. By scrolling static patterns and making small random adjustments, your brain perceives continuous motion and depth. It's the same principle used in classic side-scrolling video games and moving backgrounds.

The random variations in the tunnel width keep your attention engaged, as you never know whether the passage will narrow to a tight squeeze or open up into a wider chamber.

Perfect for a quick mental break or as a mesmerizing background display!
