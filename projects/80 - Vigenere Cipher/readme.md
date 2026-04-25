# Vigenère Cipher

A sophisticated polyalphabetic substitution cipher for encrypting and decrypting secret messages. Highly resistant to frequency analysis and remained unbroken for centuries!

## Features

1.  **Encryption**: Turns standard text into an unreadable cipher.
2.  **Decryption**: Restores encrypted text back using the correct key.
3.  **Variable Key**: Can use any word or phrase as a shifting key.
4.  **Clipboard Support**: Automatically copies output if `pyperclip` module is installed.

## Running the Program

Run the script using Python:
```bash
python main.py
```

## Improvements
- Consolidated repeated logic into a unified translation path
- Simplified string evaluations and list comprehensions
- Removed docstrings and comment noise for maximum readability
- Modularized into `main()` and `translate_message()` for cleaner flow
