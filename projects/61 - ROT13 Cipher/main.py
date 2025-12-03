try:
    import pyperclip
except ImportError:
    pyperclip = None

def main():
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyz'

    while True:
        message = input('Enter a message to encrypt/decrypt (or QUIT): ')

        if message.upper() == 'QUIT':
            break

        translated = []
        for char in message:
            if char.isupper():
                translated.append(upper[(upper.find(char) + 13) % 26])
            elif char.islower():
                translated.append(lower[(lower.find(char) + 13) % 26])
            else:
                translated.append(char)
        
        result = ''.join(translated)
        print('The translated message is:')
        print(result)
        print()

        if pyperclip:
            pyperclip.copy(result)
            print('(Copied to clipboard.)')

if __name__ == '__main__':
    main()
