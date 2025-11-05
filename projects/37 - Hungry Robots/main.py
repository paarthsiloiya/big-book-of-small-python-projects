import random
import sys
import os

WIDTH = 40
HEIGHT = 20
NUM_ROBOTS = 10
NUM_TELEPORTS = 2
NUM_DEAD_ROBOTS = 2
NUM_WALLS = 100

EMPTY_SPACE = ' '
PLAYER = '♦'
ROBOT = '◊'
DEAD_ROBOT = '✗'
WALL = '█'
TELEPORT_SPOT = '⚡'


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():
    clear_screen()
    print('HUNGRY ROBOTS - Escape by making them crash into each other!')
    print('Controls: QWEASDZXC for movement, T for teleport, QUIT to exit')
    input('Press Enter to begin...')

    board = get_new_board()
    robots = add_robots(board)
    player_position = get_random_empty_space(board, robots)
    
    while True:
        clear_screen()
        display_board(board, robots, player_position)

        if len(robots) == 0:
            print('Victory! All robots have crashed!')
            sys.exit()

        player_position = ask_for_player_move(board, robots, player_position)
        robots = move_robots(board, robots, player_position)

        for x, y in robots:
            if (x, y) == player_position:
                clear_screen()
                display_board(board, robots, player_position)
                print('Game Over! You were caught by a robot!')
                sys.exit()


def get_new_board():
    board = {'teleports': NUM_TELEPORTS}

    for x in range(WIDTH):
        for y in range(HEIGHT):
            board[(x, y)] = EMPTY_SPACE

    for x in range(WIDTH):
        board[(x, 0)] = WALL
        board[(x, HEIGHT - 1)] = WALL
    for y in range(HEIGHT):
        board[(0, y)] = WALL
        board[(WIDTH - 1, y)] = WALL

    for i in range(NUM_WALLS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = WALL

    for i in range(NUM_DEAD_ROBOTS):
        x, y = get_random_empty_space(board, [])
        board[(x, y)] = DEAD_ROBOT
    return board


def get_random_empty_space(board, robots):
    while True:
        random_x = random.randint(1, WIDTH - 2)
        random_y = random.randint(1, HEIGHT - 2)
        if is_empty(random_x, random_y, board, robots):
            break
    return (random_x, random_y)


def is_empty(x, y, board, robots):
    return board[(x, y)] == EMPTY_SPACE and (x, y) not in robots


def add_robots(board):
    robots = []
    for i in range(NUM_ROBOTS):
        x, y = get_random_empty_space(board, robots)
        robots.append((x, y))
    return robots


def display_board(board, robots, player_position):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if board[(x, y)] == WALL:
                print(WALL, end='')
            elif board[(x, y)] == DEAD_ROBOT:
                print(DEAD_ROBOT, end='')
            elif (x, y) == player_position:
                print(PLAYER, end='')
            elif (x, y) in robots:
                print(ROBOT, end='')
            else:
                print(EMPTY_SPACE, end='')
        print()


def ask_for_player_move(board, robots, player_position):
    player_x, player_y = player_position

    q = 'Q' if is_empty(player_x - 1, player_y - 1, board, robots) else ' '
    w = 'W' if is_empty(player_x + 0, player_y - 1, board, robots) else ' '
    e = 'E' if is_empty(player_x + 1, player_y - 1, board, robots) else ' '
    d = 'D' if is_empty(player_x + 1, player_y + 0, board, robots) else ' '
    c = 'C' if is_empty(player_x + 1, player_y + 1, board, robots) else ' '
    x = 'X' if is_empty(player_x + 0, player_y + 1, board, robots) else ' '
    z = 'Z' if is_empty(player_x - 1, player_y + 1, board, robots) else ' '
    a = 'A' if is_empty(player_x - 1, player_y + 0, board, robots) else ' '
    all_moves = (q + w + e + d + c + x + a + z + 'S')

    while True:
        print(f'\n{TELEPORT_SPOT} Teleports remaining: {board["teleports"]}')
        print(f'                    ({q}) ({w}) ({e})')
        print(f'                    ({a}) (S) ({d})')
        print(f'Enter move or QUIT: ({z}) ({x}) ({c})')

        move = input('> ').upper()
        if move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'T' and board['teleports'] > 0:
            board['teleports'] -= 1
            return get_random_empty_space(board, robots)
        elif move != '' and move in all_moves:
            return {'Q': (player_x - 1, player_y - 1),
                    'W': (player_x + 0, player_y - 1),
                    'E': (player_x + 1, player_y - 1),
                    'D': (player_x + 1, player_y + 0),
                    'C': (player_x + 1, player_y + 1),
                    'X': (player_x + 0, player_y + 1),
                    'Z': (player_x - 1, player_y + 1),
                    'A': (player_x - 1, player_y + 0),
                    'S': (player_x, player_y)}[move]


def move_robots(board, robot_positions, player_position):
    player_x, player_y = player_position
    next_robot_positions = []

    while len(robot_positions) > 0:
        robot_x, robot_y = robot_positions[0]

        if robot_x < player_x:
            move_x = 1
        elif robot_x > player_x:
            move_x = -1
        elif robot_x == player_x:
            move_x = 0

        if robot_y < player_y:
            move_y = 1
        elif robot_y > player_y:
            move_y = -1
        elif robot_y == player_y:
            move_y = 0

        if board[(robot_x + move_x, robot_y + move_y)] == WALL:
            if board[(robot_x + move_x, robot_y)] == EMPTY_SPACE:
                move_y = 0
            elif board[(robot_x, robot_y + move_y)] == EMPTY_SPACE:
                move_x = 0
            else:
                move_x = 0
                move_y = 0
        
        new_robot_x = robot_x + move_x
        new_robot_y = robot_y + move_y

        if (board[(robot_x, robot_y)] == DEAD_ROBOT
            or board[(new_robot_x, new_robot_y)] == DEAD_ROBOT):
            del robot_positions[0]
            continue

        if (new_robot_x, new_robot_y) in next_robot_positions:
            board[(new_robot_x, new_robot_y)] = DEAD_ROBOT
            next_robot_positions.remove((new_robot_x, new_robot_y))
        else:
            next_robot_positions.append((new_robot_x, new_robot_y))

        del robot_positions[0]
    return next_robot_positions


if __name__ == '__main__':
    main()
