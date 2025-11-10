# Mancala - The Ancient Seed Game 🏺

An enhanced implementation of the classic two-player board game Mancala with improved visuals, multiple difficulty levels, and engaging gameplay features.

## What is Mancala?

Mancala is an ancient African board game involving strategy and counting. Players take turns picking up seeds from pits on their side and distributing them counterclockwise around the board.

## How to Play

### Basic Rules
- Choose a pit on your side (A-F for Player 1, G-L for Player 2)
- Pick up all seeds from that pit and distribute one seed per pit going counterclockwise
- Skip your opponent's store (the large pit on their side)
- If your last seed lands in your store, you get another turn! 🎯
- If your last seed lands in an empty pit on your side, capture all seeds from the opposite pit! ⚡

### Winning
- Game ends when one player's side is completely empty
- The other player gets all remaining seeds on their side
- Player with the most seeds in their store wins! 🏆

## Enhanced Features

### 🌟 Visual Improvements
- Beautiful Unicode box-drawing board display
- Colorful emojis and symbols for better visual appeal
- Clear screen clearing for smooth gameplay
- Player indicators with fire (🔥) and ice (❄️) themes

### 🎯 Difficulty Levels
- **Easy**: 3 seeds per pit - Perfect for beginners
- **Normal**: 4 seeds per pit - Classic Mancala experience
- **Hard**: 6 seeds per pit - More strategic depth
- **Extreme**: 8 seeds per pit - Maximum complexity and longer games

### 🚀 Gameplay Enhancements
- Move counter to track game progress
- Real-time feedback for captures and free turns
- Help system (type 'HELP' during play)
- Play again option for continuous gaming
- Immediate capture notifications with visual effects

### 🎮 User Experience
- Cross-platform screen clearing (Windows/Unix)
- Input validation with helpful error messages
- Graceful quit option (type 'QUIT' anytime)
- Visual confirmation for all game actions

## Technical Features

- Clean, comment-free code for easy reading
- Efficient board representation using dictionaries
- Modular function design for maintainability
- Cross-platform compatibility
- No external dependencies required

## Running the Game

```bash
python main.py
```

The game will guide you through difficulty selection and provide all necessary instructions during play. Perfect for players of all skill levels!