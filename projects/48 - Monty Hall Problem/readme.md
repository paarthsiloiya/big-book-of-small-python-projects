# The Monty Hall Problem - Probability Game 🎪

An enhanced interactive simulation of the famous Monty Hall probability paradox with multiple game modes and comprehensive statistical analysis.

## What is the Monty Hall Problem?

A classic probability puzzle: You're on a game show with 3 doors. One has a car 🚗, two have goats 🐐. After you pick a door, the host opens a different door with a goat. Should you **stay** with your choice or **swap** to the remaining door?

**Surprising Answer**: Swapping gives you a 67% win rate vs 33% for staying!

## Enhanced Features

### 🎮 **Multiple Game Modes**
- **Tutorial Mode**: Step-by-step explanations of probability theory
- **Quick Play**: Fast-paced gameplay for experienced players  
- **Auto-Simulation**: Run 1000 games instantly to verify the math

### 📊 **Advanced Statistics**
- **Real-time win percentages** with expected vs actual comparisons
- **Swap advantage calculation** showing percentage difference
- **Theory accuracy measurement** for large sample sizes
- **Convergence analysis** demonstrating law of large numbers

### 🎯 **Interactive Learning**
- **Probability explanations** available during gameplay (press E)
- **Visual door animations** for dramatic effect
- **Enhanced ASCII art** with Unicode characters and emojis
- **Mathematical theory validation** through statistical analysis

### 🚀 **User Experience Improvements**
- **Beautiful welcome screen** with game rules explanation
- **Cross-platform screen clearing** for smooth transitions
- **Multiple input options**: quit, stats, explain commands
- **Progress tracking** for auto-simulations
- **Final statistics summary** upon exit

## How to Play

1. **Run**: `python main.py`
2. **Choose Mode**: Tutorial (1), Quick Play (2), or Auto-Sim (3)
3. **Pick Door**: Choose door 1, 2, or 3
4. **Make Decision**: Stay or swap after host reveals goat
5. **Learn**: Watch your win rates approach the theoretical 33%/67% split

### Commands During Play
- **Numbers 1-3**: Choose a door
- **Y/N**: Yes/No for swapping decision
- **E**: Explain the probability theory
- **"quit"**: Exit the game
- **"stats"**: View current statistics

## Mathematical Foundation

- **Initial Probability**: Each door has 1/3 chance (33.33%)
- **After Reveal**: Your door stays 1/3, remaining door gets 2/3 (66.67%)
- **Swap Strategy**: Doubles your chances of winning
- **Law of Large Numbers**: Results converge to theory with more games
