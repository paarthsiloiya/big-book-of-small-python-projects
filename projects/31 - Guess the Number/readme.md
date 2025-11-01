# Guess the Number - Classic Number Guessing Game

Welcome to **Guess the Number**, the timeless game of deduction and luck! Test your intuition and logical thinking as you try to guess a secret number between 1 and 100. With only 10 attempts, every guess counts in this engaging battle of wits against the computer.

## How to Play

### Game Setup
1. **Secret Number**: The computer randomly selects a number between 1 and 100
2. **Limited Attempts**: You have exactly 10 guesses to find the correct number
3. **Smart Guessing**: Use the feedback clues to narrow down your search

### Making Your Guess
- Enter any whole number between 1 and 100
- The game will tell you if your guess is too high, too low, or exactly right
- Keep track of your previous guesses to avoid repetition
- You win if you guess correctly within 10 attempts

## Game Features

### Intelligent Feedback System
After each guess, you'll receive one of three helpful clues:
- **"Too low!"** - Your guess is smaller than the secret number
- **"Too high!"** - Your guess is larger than the secret number  
- **"Congratulations!"** - You've found the secret number

### Attempt Tracking
- Each guess is numbered (Guess #1, Guess #2, etc.)
- You can see exactly how many attempts you have remaining
- The game displays your total guesses when you win

### Input Validation
- Only accepts valid whole numbers
- Handles invalid input gracefully with helpful error messages
- Prompts you to try again if you enter non-numeric text

## Winning and Losing

### Victory Conditions
- **Find the Number**: Guess the exact secret number within 10 attempts
- **Efficiency Bonus**: The fewer guesses you use, the more impressive your victory
- **Perfect Score**: Guessing in 1 try is the ultimate achievement

### Game Over
- **Out of Guesses**: If you use all 10 attempts without success
- **Number Revealed**: The secret number is shown when the game ends
- **Encouraging Message**: You're invited to try again with a new number

## Strategy Tips

### Binary Search Method
- **Start in the Middle**: Begin with 50 to eliminate half the possibilities
- **Divide and Conquer**: Use each clue to cut the remaining range in half
- **Mathematical Approach**: This method guarantees success within 7 guesses

### Psychological Approach  
- **Trust Your Instincts**: Sometimes a gut feeling leads to quick success
- **Avoid Patterns**: Don't fall into predictable number sequences
- **Stay Flexible**: Mix logical deduction with intuitive leaps

### Advanced Techniques
- **Range Tracking**: Keep mental notes of eliminated number ranges
- **Probability Thinking**: Consider which numbers are most likely
- **Pattern Recognition**: Notice if you tend to guess high or low
