# Periodic Table of Elements

An interactive periodic table explorer that displays atomic information for all chemical elements with enhanced search capabilities and visual improvements.

## Features

- **Interactive Periodic Table Display**: Visual representation of the complete periodic table
- **Element Information**: Detailed atomic properties including:
  - Atomic number, symbol, and name
  - Origin of name and etymology
  - Group and period classification
  - Atomic weight and density
  - Melting and boiling points
  - Specific heat capacity and electronegativity
  - Abundance in Earth's crust
- **Multiple Search Methods**:
  - Search by element name, symbol, or atomic number
  - Advanced property-based searches
  - Atomic number range filtering
  - Group and period searches
  - State of matter at room temperature
- **Smart Suggestions**: Provides element suggestions for partial or incorrect inputs
- **Random Element**: Discover random elements for learning
- **Enhanced Display**: Color-coded interface with emojis and formatted output
- **Data Cleaning**: Removes Wikipedia formatting artifacts automatically

## Usage

Run the program and use these commands:
- Enter any element name, symbol, or atomic number (e.g., "H", "1", "Hydrogen")
- Type "search" for advanced property-based searching
- Type "random" to explore a random element
- Type "quit" to exit

## Examples

- Direct lookup: "Au", "79", "Gold"
- Property search: Filter by atomic number range, group, period, or physical state
- Partial matching: "carb" finds "Carbon"

## Requirements

- Python 3.6+
- CSV data file (periodictable.csv) in workspace root
- Standard libraries: csv, sys, re, os, random

## Enhanced Features

- Cross-platform screen clearing
- Robust error handling
- Smart search suggestions
- Property-based filtering
- Visual improvements with icons and formatting
- Data validation and cleanup