# Water Bucket Puzzle

A logic puzzle game where you pour water between buckets to reach the target amount!

## How to Play

1.  **Buckets**: You have three buckets with capacities of 8L, 5L, and 3L.
2.  **Actions**:
    *   **F**: Fill a bucket to the top.
    *   **E**: Empty a bucket completely.
    *   **P**: Pour water from one bucket to another until the source is empty or the destination is full.
3.  **Goal**: Get exactly **4L** into any of the buckets.
4.  **Game Over**: The game ends when you successfully measure out 4L.

## Running the Game

Run the script using Python:
```bash
python main.py
```

## Improvements
- Cleaned up repetitive array generation and index mapping for visuals
- Consolidated the action rendering and input validations loops
- Grouped hardcoded capacities into lookup dictionaries
- Stripped out all comments and docstrings for a cleaner, minimalist codebase

Good luck!