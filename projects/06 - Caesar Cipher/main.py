SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!? #$%&'()*+-/<=>@[]^_`{|}~\"\\\'0123456789abcdefghijklmnopqrstuvwxyz"

while True:
    option = input("Would you like to (e)ncrypt or (d)ecrypt? ").lower()
    if option in ('e', 'd'):
        break
    
    print("Invalid input. Please enter 'e' or 'd'.")

while True:
    key = input("Please enter the key (1-{}): ".format(len(SYMBOLS) - 1))
    if key.isdecimal() and 1 <= int(key) < len(SYMBOLS):
        key = int(key)
        break

    print("Invalid input. Please enter a number between 1 and {}.".format(len(SYMBOLS) - 1))

message = input("Enter your message: ")
translated = ""

for symbol in message:
    if symbol in SYMBOLS:
        symbol_index = SYMBOLS.find(symbol)
        if option == 'e':
            translated_index = (symbol_index + key) % len(SYMBOLS)
        elif option == 'd':
            translated_index = (symbol_index - key) % len(SYMBOLS)
        translated += SYMBOLS[translated_index]
    else:
        translated += symbol

print("Here's the translated message:")
print(translated)