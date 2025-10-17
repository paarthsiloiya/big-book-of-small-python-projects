message = input("Enter the encrypted message to crack: ")
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ.,!? #$%&'()*+-/<=>@[]^_`{|}~\"\\\'0123456789abcdefghijklmnopqrstuvwxyz"

# * Test Input : Vw>HvsFs/>?ooFHv>$wzCwMo>HvwG>Gwrs
for key in range(len(SYMBOLS)):
    translated = ""
    for symbol in message:
        if symbol in SYMBOLS:
            symbol_index = SYMBOLS.find(symbol)
            translated_index = (symbol_index - key) % len(SYMBOLS)
            translated += SYMBOLS[translated_index]
        else:
            translated += symbol
    print(f"Key {key}: {translated}")
