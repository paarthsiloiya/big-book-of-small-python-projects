# Simple Substitution Cipher

A simple substitution cipher replaces each letter in the plaintext with a different letter from the ciphertext alphabet.

## How to Run

Run the program using Python:
`python main.py`

## How to Use

1.  **Choose Mode**: Select whether you want to (e)ncrypt or (d)ecrypt a message.
2.  **Set Key**:
    *   For encryption, you can enter a custom 26-letter key or type `RANDOM` to generate one.
    *   For decryption, you must enter the specific key used to encrypt the message.
3.  **Enter Message**: Type the text you want to process.
4.  **Result**: The program will display the translated message and copy it to your clipboard if `pyperclip` is installed.

## Requirements

*   Python 3.x
*   `pyperclip` (optional, for clipboard support)
