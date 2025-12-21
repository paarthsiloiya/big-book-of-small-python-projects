import random
import string
import sys

try:
    import pyperclip
except ImportError:
    pyperclip = None

LETTERS = string.ascii_uppercase

def main():
    print('Simple Substitution Cipher')

    while True:
        print('Do you want to (e)ncrypt or (d)ecrypt?')
        mode = input('> ').lower()
        if mode.startswith('e'):
            mode = 'encrypt'
            break
        elif mode.startswith('d'):
            mode = 'decrypt'
            break

    while True:
        print('Please specify the key to use.')
        if mode == 'encrypt':
            print('Or enter RANDOM to have one generated for you.')
        key = input('> ').upper()
        if key == 'RANDOM':
            key_list = list(LETTERS)
            random.shuffle(key_list)
            key = ''.join(key_list)
            print(f'The key is {key}. KEEP THIS SECRET!')
            break
        elif validate_key(key):
            break

    print(f'Enter the message to {mode}.')
    message = input('> ')

    if mode == 'encrypt':
        translated = translate(message, LETTERS, key)
    else:
        translated = translate(message, key, LETTERS)

    print(f'The {mode}ed message is:')
    print(translated)

    if pyperclip:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard.')

def validate_key(key):
    if len(key) != len(LETTERS):
        print('Key must be 26 characters long.')
        return False
    if sorted(key) != sorted(LETTERS):
        print('Key must contain every letter of the alphabet exactly once.')
        return False
    return True

def translate(message, chars_a, chars_b):
    mapping = {a: b for a, b in zip(chars_a, chars_b)}
    translated = []
    for char in message:
        upper_char = char.upper()
        if upper_char in mapping:
            new_char = mapping[upper_char]
            if char.islower():
                new_char = new_char.lower()
            translated.append(new_char)
        else:
            translated.append(char)
    return ''.join(translated)

if __name__ == '__main__':
    main()
