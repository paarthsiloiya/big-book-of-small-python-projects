# Factor Finder - Fast Mathematical Factor Calculator

Discover all the **mathematical factors** of any positive integer with this efficient command-line calculator! Whether you're working on math homework, exploring number theory, or just curious about the divisors of a number, this tool provides instant, accurate results using optimized algorithms.

## What This Program Does

This powerful mathematical utility helps you explore the factor structure of numbers:

- **Complete Factor Lists**: Finds ALL factors of any positive integer instantly
- **Optimized Algorithm**: Uses square root optimization for lightning-fast calculations  
- **Dual Input Methods**: Interactive prompts or command-line arguments for flexibility
- **Input Validation**: Robust error checking ensures only valid positive integers are processed
- **Clean Output**: Displays factors in an easy-to-read, sorted format
- **No Dependencies**: Uses only Python's standard library for maximum compatibility

## Features

### Smart Input Handling
- **Interactive Mode**: Prompts for input when run without arguments
- **Command Line Mode**: Accepts number as argument for scripting
- **Input Validation**: Rejects negative numbers, zero, and non-integers
- **Error Recovery**: Allows re-entry of invalid inputs in interactive mode

### Efficient Computation
- **Square Root Optimization**: Only checks divisors up to √n
- **Pair Detection**: Automatically finds factor pairs (i, n/i)
- **Set Storage**: Uses sets to avoid duplicate factors automatically
- **Integer Square Root**: Uses `math.isqrt()` for perfect precision

### User-Friendly Output
- **Sorted Results**: Factors displayed in ascending numerical order
- **Clear Formatting**: Comma-separated list for easy reading
- **Informative Messages**: Clear prompts and error messages
- **Instant Results**: No loading delays, even for large numbers
