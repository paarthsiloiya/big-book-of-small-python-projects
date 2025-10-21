def displayOutlineDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/', end='')
        print(' ' * (i * 2), end='')
        print('\\')

    for i in range(size):
        print(' ' * i, end='')
        print('\\', end='')
        print(' ' * ((size - i - 1) * 2), end='')
        print('/')


def displayFilledDiamond(size):
    for i in range(size):
        print(' ' * (size - i - 1), end='')
        print('/' * (i + 1), end='')
        print('\\' * (i + 1))

    for i in range(size):
        print(' ' * i, end='')
        print('\\' * (size - i), end='')
        print('/' * (size - i))


while True:
    print("Commands: 'outline <size>', 'filled <size>', 'quit'")
    command = input("Enter command: ").strip().lower()
    if command == 'quit':
        break
    parts = command.split()
    if len(parts) == 2:
        shape = parts[0]
        try:
            size = int(parts[1])
            if size < 0:
                print("Size must be a non-negative integer.")
                continue
            if shape == 'outline':
                displayOutlineDiamond(size)
            elif shape == 'filled':
                displayFilledDiamond(size)
            else:
                print("Unknown shape. Use 'outline' or 'filled'.")
        except ValueError:
            print("Invalid size. Please enter a non-negative integer.")
            