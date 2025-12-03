# ROT13 Cipher

A simple implementation of the ROT13 substitution cipher.

## How It Works

ROT13 ("rotate by 13 places") replaces a letter with the 13th letter after it in the alphabet. Because the alphabet has 26 letters, applying ROT13 twice returns the original text.

## Features

-   **Bidirectional**: The same algorithm encrypts and decrypts.
-   **Clipboard Support**: Automatically copies the result if `pyperclip` is installed.
-   **Preserves Formatting**: Non-alphabetic characters remain unchanged.

## Usage

Run the script and enter your text:
`python main.py`

To install the optional clipboard module:
`pip install pyperclip`
