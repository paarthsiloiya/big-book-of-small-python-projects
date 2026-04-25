import string

try:
    import pyperclip
except ImportError:
    pyperclip = None

LETTERS = string.ascii_uppercase

def translate_message(message, key, mode):
    translated = []
    key_chars = [c for c in key.upper() if c in LETTERS]
    key_index = 0

    for symbol in message:
        num = LETTERS.find(symbol.upper())
        if num != -1:
            key_shift = LETTERS.find(key_chars[key_index])
            if mode == 'encrypt':
                num = (num + key_shift) % 26
            else:
                num = (num - key_shift) % 26

            if symbol.isupper():
                translated.append(LETTERS[num])
            else:
                translated.append(LETTERS[num].lower())

            key_index = (key_index + 1) % len(key_chars)
        else:
            translated.append(symbol)

    return ''.join(translated)

def main():
    print("Vigenère Cipher")
    while True:
        mode = input('Do you want to (e)ncrypt or (d)ecrypt?\n> ').lower()
        if mode in ('e', 'encrypt', 'd', 'decrypt'):
            mode = 'encrypt' if mode.startswith('e') else 'decrypt'
            break
        print('Please enter the letter e or d.')

    while True:
        key = input('Please specify the key to use (letters only).\n> ').upper()
        if key.isalpha():
            break

    message = input(f'Enter the message to {mode}.\n> ')
    translated = translate_message(message, key, mode)

    print(f'\n{mode.title()}ed message:\n{translated}')

    if pyperclip:
        pyperclip.copy(translated)
        print(f'Full {mode}ed text copied to clipboard.')

if __name__ == '__main__':
    main()