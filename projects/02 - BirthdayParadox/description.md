# The Birthday Paradox - A Surprising Probability Puzzle

The **Birthday Paradox** is a classic probability problem that reveals a counterintuitive truth: you don't need a large group of people to have a high chance of two individuals sharing the same birthday.

## The Core Question

What is the probability that, in a randomly chosen group of `n` people, at least two of them share a birthday?

## The "Paradox"

The surprising part isn't a logical contradiction, but rather that the probability is much higher than most people would expect.

-   In a group of just **23 people**, the probability of a shared birthday is over **50%**.
-   In a group of **70 people**, the probability skyrockets to **99.9%**!

This program simulates this phenomenon. It generates random birthdays for a specified number of people and checks for matches. By running thousands of simulations, it demonstrates how the probability of a shared birthday changes with the size of the group.

### How the Simulation Works

1.  You specify the number of people in the group.
2.  The program generates that many random birthdays (ignoring leap years for simplicity).
3.  It checks if any birthdays in the generated set are the same.
4.  To prove the paradox, it runs this process 100,000 times and calculates the percentage of those simulations where a shared birthday was found.

Prepare to be surprised by the results! 