import random, os, sys

try:
    import pyperclip
except ImportError:
    pyperclip = None

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('sPoNgEcAsE tExT gEnErAtOr')
    print('EnTeR tExT tO cOnVeRt (Or "QUIT" tO eXiT).')

    while True:
        text = input('\n> ')
        if text.upper() == 'QUIT':
            sys.exit()

        converted = to_spongecase(text)
        print(f'\n{converted}')

        if pyperclip:
            pyperclip.copy(converted)
            print('(CoPiEd To ClIpBoArD)')

def to_spongecase(text):
    result = []
    upper = False
    
    for char in text:
        if not char.isalpha():
            result.append(char)
            continue
            
        if upper:
            result.append(char.upper())
        else:
            result.append(char.lower())
            
        if random.random() < 0.9:
            upper = not upper
            
    return ''.join(result)

if __name__ == '__main__':
    main()
