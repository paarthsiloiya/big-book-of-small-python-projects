# Pig Latin Translator

An enhanced Pig Latin translator that converts between English and Pig Latin with advanced features, file processing, and bidirectional translation capabilities.

## Features

- **Bidirectional Translation**: Convert English to Pig Latin and vice versa
- **Smart Text Processing**: Preserves capitalization, punctuation, and formatting
- **Interactive Menu System**: Easy-to-use interface with multiple options
- **File Translation**: Batch process entire text files
- **Translation History**: Keep track of recent translations
- **Clipboard Integration**: Automatic copying to clipboard (if pyperclip available)
- **Language Rules Help**: Built-in reference for Pig Latin rules
- **Enhanced Algorithm**: Improved handling of edge cases and special characters

## Translation Rules

### English to Pig Latin:
- **Vowel Start**: Words beginning with vowels get "way" added
  - Example: "apple" → "appleway"
- **Consonant Start**: Move consonant cluster to end + "ay"
  - Example: "hello" → "ellohay"
  - Example: "string" → "ingstray"

### Special Handling:
- Preserves capitalization (Hello → Ellohay)
- Maintains punctuation (Hello! → Ellohay!)
- Handles numbers and symbols correctly

## Usage Options

1. **Interactive Translation**: Real-time English ↔ Pig Latin conversion
2. **File Processing**: Translate entire text files
3. **Rules Reference**: View translation rules and examples
4. **History Tracking**: Review recent translations
5. **Screen Management**: Clear screen functionality

## Requirements

- Python 3.6+
- Optional: pyperclip library for clipboard functionality
  - Install with: `pip install pyperclip`

## Enhanced Features

- Improved reverse translation algorithm
- Better handling of consonant clusters
- File batch processing
- Translation history with directional indicators
- Cross-platform screen clearing
- Error handling for file operations
- Menu-driven interface with emojis and formatting

## Example Translations

- "Hello World!" → "Ellohay Orldway!"
- "Python Programming" → "Ythonpay Ogrammingpray"  
- "appleway orldway" → "apple world"