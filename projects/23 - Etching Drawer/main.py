import shutil, sys, os

UP_DOWN_CHAR         = chr(9474)
LEFT_RIGHT_CHAR      = chr(9472)
DOWN_RIGHT_CHAR      = chr(9484)
DOWN_LEFT_CHAR       = chr(9488)
UP_RIGHT_CHAR        = chr(9492)
UP_LEFT_CHAR         = chr(9496)
UP_DOWN_RIGHT_CHAR   = chr(9500)
UP_DOWN_LEFT_CHAR    = chr(9508)
DOWN_LEFT_RIGHT_CHAR = chr(9516)
UP_LEFT_RIGHT_CHAR   = chr(9524)
CROSS_CHAR           = chr(9532)

TERMINAL_WIDTH, TERMINAL_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH = TERMINAL_WIDTH - 2
CANVAS_HEIGHT = TERMINAL_HEIGHT - 4

canvas = {}
cursorX = 0
cursorY = 0

def getCanvasString(canvasData, cx, cy):
    canvasStr = ''
    
    canvasStr += DOWN_RIGHT_CHAR + LEFT_RIGHT_CHAR * CANVAS_WIDTH + DOWN_LEFT_CHAR + '\n'
    
    for rowNum in range(CANVAS_HEIGHT):
        canvasStr += UP_DOWN_CHAR
        for columnNum in range(CANVAS_WIDTH):
            if columnNum == cx and rowNum == cy:
                canvasStr += '#'
                continue

            cell = canvasData.get((columnNum, rowNum))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                canvasStr += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                canvasStr += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                canvasStr += DOWN_RIGHT_CHAR
            elif cell == set(['A', 'S']):
                canvasStr += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                canvasStr += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                canvasStr += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                canvasStr += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                canvasStr += UP_DOWN_LEFT_CHAR
            elif cell == set(['A', 'S', 'D']):
                canvasStr += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'D']):
                canvasStr += UP_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'A', 'S', 'D']):
                canvasStr += CROSS_CHAR
            elif cell == None:
                canvasStr += ' '
        canvasStr += UP_DOWN_CHAR + '\n'
    
    canvasStr += UP_RIGHT_CHAR + LEFT_RIGHT_CHAR * CANVAS_WIDTH + UP_LEFT_CHAR
    return canvasStr

moves = []
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(getCanvasString(canvas, cursorX, cursorY))

    response = input('WASD keys to move, H for help, C to clear, '
        + 'F to save, or Q to quit: ').upper()

    if response == 'Q':
        print('Thanks for playing!')
        sys.exit()
    elif response == 'H':
        print('Enter W, A, S, and D characters to move the cursor and')
        print('draw a line behind it as it moves. For example, ddd')
        print('draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif response == 'C':
        canvas = {}
        moves.append('C')
    elif response == 'F':
        try:
            filename = input('Enter filename to save to: ')

            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(''.join(moves) + '\n')
                file.write(getCanvasString(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in response:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)

        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(cursorX, cursorY)] = set(['A', 'D'])

        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY - 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY = cursorY + 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX - 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX = cursorX + 1
        else:
            continue

        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')
