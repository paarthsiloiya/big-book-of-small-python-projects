import copy, random, sys, os

PUZZLES = [
    '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..',
    '2...8.3...6..7..84.3.5..2.9...1.54.8.........4.27.6...3.1..7.4.72..4..6...4.1...3',
    '......9.7...42.18....7.5.261..9.4....5.....4....5.7..992.1.8....34.59...5.7......',
    '.3..5..4...8.1.5..46.....12.7.5.2.8....6.3....4.1.9.3.25.....98..1.2.6...8..6..2.'
]

class SudokuGrid:
    def __init__(self, setup):
        self.original = setup
        self.grid = {}
        self.moves = []
        self.reset()

    def reset(self):
        self.grid = {}
        for i in range(81):
            self.grid[(i % 9, i // 9)] = self.original[i]
        self.moves = []

    def make_move(self, col, row, num):
        x, y = 'ABCDEFGHI'.index(col), int(row) - 1
        if self.original[y * 9 + x] != '.':
            return False
        self.moves.append(copy.copy(self.grid))
        self.grid[(x, y)] = num
        return True

    def undo(self):
        if self.moves:
            self.grid = self.moves.pop()

    def is_solved(self):
        for i in range(9):
            row = [self.grid[(x, i)] for x in range(9)]
            col = [self.grid[(i, y)] for y in range(9)]
            if sorted(row) != list('123456789') or sorted(col) != list('123456789'):
                return False
        for bx in (0, 3, 6):
            for by in (0, 3, 6):
                box = [self.grid[(bx+x, by+y)] for x in range(3) for y in range(3)]
                if sorted(box) != list('123456789'):
                    return False
        return True

    def display(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print('    A B C   D E F   G H I')
        print('  ┌───────┬───────┬───────┐')
        for y in range(9):
            print(f'{y+1} │', end=' ')
            for x in range(9):
                val = self.grid[(x, y)]
                print(val if val != '.' else ' ', end=' ')
                if x in (2, 5): print('│', end=' ')
            print('│')
            if y in (2, 5):
                print('  ├───────┼───────┼───────┤')
        print('  └───────┴───────┴───────┘')

def main():
    game = SudokuGrid(random.choice(PUZZLES))
    
    while True:
        game.display()
        if game.is_solved():
            print('Solved!')
            sys.exit()

        print('Enter move (e.g. "A1 5") or NEW, RESET, UNDO, QUIT')
        action = input('> ').upper().strip()

        if action == 'QUIT': sys.exit()
        elif action == 'NEW': game = SudokuGrid(random.choice(PUZZLES))
        elif action == 'RESET': game.reset()
        elif action == 'UNDO': game.undo()
        elif len(action.split()) == 2:
            pos, num = action.split()
            if len(pos) == 2 and pos[0] in 'ABCDEFGHI' and pos[1] in '123456789' and num in '123456789':
                if not game.make_move(pos[0], pos[1], num):
                    print('Cannot overwrite fixed number.')
                    input('Press Enter...')

if __name__ == '__main__':
    main()
