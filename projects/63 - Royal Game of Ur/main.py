import random
import sys

class RoyalGameOfUr:
    X_PLAYER = 'X'
    O_PLAYER = 'O'
    EMPTY = ' '
    X_HOME = 'x_home'
    O_HOME = 'o_home'
    X_GOAL = 'x_goal'
    O_GOAL = 'o_goal'
    
    ALL_SPACES = 'hgfetsijklmnopdcbarq'
    X_TRACK = 'HefghijklmnopstG'
    O_TRACK = 'HabcdijklmnopqrG'
    FLOWER_SPACES = ('h', 't', 'l', 'd', 'r')
    
    BOARD_TEMPLATE = """
                   {}           {}
                   Home              Goal
                     v                 ^
+-----+-----+-----+--v--+           +--^--+-----+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****h|    g|    f|    e|           |****t|    s|
+--v--+-----+-----+-----+-----+-----+-----+--^--+
|     |     |     |*****|     |     |     |     |
|  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
|    i|    j|    k|****l|    m|    n|    o|    p|
+--^--+-----+-----+-----+-----+-----+-----+--v--+
|*****|     |     |     |           |*****|     |
|* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
|****d|    c|    b|    a|           |****r|    q|
+-----+-----+-----+--^--+           +--v--+-----+
                     ^                 v
                   Home              Goal
                   {}           {}
"""

    def __init__(self):
        self.board = {s: self.EMPTY for s in self.ALL_SPACES}
        self.board[self.X_HOME] = 7
        self.board[self.X_GOAL] = 0
        self.board[self.O_HOME] = 7
        self.board[self.O_GOAL] = 0
        self.turn = self.O_PLAYER

    def display_board(self):
        print('\n' * 60)
        x_home = ('X' * self.board[self.X_HOME]).ljust(7, '.')
        x_goal = ('X' * self.board[self.X_GOAL]).ljust(7, '.')
        o_home = ('O' * self.board[self.O_HOME]).ljust(7, '.')
        o_goal = ('O' * self.board[self.O_GOAL]).ljust(7, '.')

        spaces = [x_home, x_goal]
        for label in self.ALL_SPACES:
            spaces.append(self.board[label])
        spaces.append(o_home)
        spaces.append(o_goal)

        print(self.BOARD_TEMPLATE.format(*spaces))

    def get_valid_moves(self, roll):
        if roll == 0:
            return []

        moves = []
        if self.turn == self.X_PLAYER:
            track = self.X_TRACK
            home = self.X_HOME
            opponent = self.O_PLAYER
        else:
            track = self.O_TRACK
            home = self.O_HOME
            opponent = self.X_PLAYER

        if self.board[home] > 0:
            dest_index = roll
            if self.board[track[dest_index]] == self.EMPTY:
                moves.append('home')

        for index, space in enumerate(track):
            if space == 'H' or space == 'G' or self.board[space] != self.turn:
                continue
            
            next_index = index + roll
            if next_index >= len(track):
                continue
            
            dest = track[next_index]
            if dest == 'G':
                moves.append(space)
                continue
            
            if self.board[dest] in (self.EMPTY, opponent):
                if dest == 'l' and self.board['l'] == opponent:
                    continue
                moves.append(space)
        
        return moves

    def run(self):
        print("The Royal Game of Ur")
        input('Press Enter to begin...')

        while True:
            self.display_board()
            
            if self.turn == self.X_PLAYER:
                home, goal, track = self.X_HOME, self.X_GOAL, self.X_TRACK
                opponent_home = self.O_HOME
                opponent = self.O_PLAYER
            else:
                home, goal, track = self.O_HOME, self.O_GOAL, self.O_TRACK
                opponent_home = self.X_HOME
                opponent = self.X_PLAYER

            input(f"It is {self.turn}'s turn. Press Enter to flip...")
            
            roll = sum(random.randint(0, 1) for _ in range(4))
            print(f"Flips: {roll}")
            
            if roll == 0:
                input("Zero moves. Press Enter...")
                self.turn = opponent
                continue

            valid_moves = self.get_valid_moves(roll)
            
            if not valid_moves:
                print("No possible moves.")
                input("Press Enter...")
                self.turn = opponent
                continue

            while True:
                print(f"Select move {roll} spaces: {' '.join(valid_moves)} quit")
                move = input('> ').lower()
                
                if move == 'quit':
                    sys.exit()
                if move in valid_moves:
                    break
                print("Invalid move.")

            if move == 'home':
                self.board[home] -= 1
                dest_index = roll
            else:
                self.board[move] = self.EMPTY
                dest_index = track.index(move) + roll

            if dest_index == len(track) - 1:
                self.board[goal] += 1
                if self.board[goal] == 7:
                    self.display_board()
                    print(f"{self.turn} has won!")
                    sys.exit()
                next_space = None
            else:
                next_space = track[dest_index]
                if self.board[next_space] == opponent:
                    self.board[opponent_home] += 1
                self.board[next_space] = self.turn

            if next_space in self.FLOWER_SPACES:
                print(f"{self.turn} landed on a flower and goes again.")
                input("Press Enter...")
            else:
                self.turn = opponent

if __name__ == '__main__':
    game = RoyalGameOfUr()
    game.run()
