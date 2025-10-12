# Bagels - A Deductive Logic Game

Welcome to **Bagels**, a fun and challenging code-breaking game! Your goal is to guess a secret three-digit number. The catch? The number has no repeated digits.

## How to Play

1.  The computer will generate a secret 3-digit number.
2.  You have **10 attempts** to guess the number.
3.  After each guess, the computer will provide clues to help you deduce the secret number.

## Understanding the Clues

-   **Pico**: One of your guessed digits is correct, but it's in the **wrong position**.
-   **Fermi**: One of your guessed digits is correct, and it's in the **correct position**.
-   **Bagels**: None of your guessed digits are in the secret number.

The clues are given for each digit. For example, if you get "Pico Fermi", it means one digit is correct but in the wrong spot, and another is in the right spot.

### Example

Let's say the secret number is `789`.

-   If you guess `123`, the clue will be: **Bagels** (No correct digits).
-   If you guess `867`, the clues will be: **Pico Pico** (8 and 7 are in the secret number, but both are in the wrong position).
-   If you guess `798`, the clues will be: **Fermi Pico Pico** (7 is in the correct position, while 8 and 9 are correct but in the wrong positions).

Can you crack the code before you run out of guesses? Good luck!