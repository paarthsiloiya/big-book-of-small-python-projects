import math, shutil, sys, time

WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -= 1

COLORS = [
    '\033[31m', '\033[33m', '\033[32m', '\033[36m', '\033[34m', '\033[35m'
]
RESET = '\033[0m'

print('Sine Message')
print('(Press Ctrl-C to quit.)')

while True:
    print(f'Enter message (1-{WIDTH // 2} chars):')
    message = input('> ')
    if 1 <= len(message) <= (WIDTH // 2):
        break

step = 0.0
multiplier = (WIDTH - len(message)) / 2
color_index = 0

try:
    while True:
        sin_val = math.sin(step)
        padding = ' ' * int((sin_val + 1) * multiplier)
        print(COLORS[color_index] + padding + message + RESET)
        time.sleep(0.1)
        step += 0.2
        color_index = (color_index + 1) % len(COLORS)
except KeyboardInterrupt:
    sys.exit()
