import random, sys, time
WIDTH = 80
PAUSE_TIME = 0.05
WALL = '⣿'
LEFT_WIDTH = 20
gap_width = 20

while True:
    left_width = random.randint(LEFT_WIDTH - 1, LEFT_WIDTH + 1)
    right_width = WIDTH - left_width - gap_width

    print(WALL * left_width + ' ' * gap_width + WALL * right_width)

    if random.randint(1, 6) == 1 and gap_width > 2:
        gap_width -= 1
    elif random.randint(1, 6) == 2 and gap_width < WIDTH - 2:
        gap_width += 1
    
    time.sleep(PAUSE_TIME)
