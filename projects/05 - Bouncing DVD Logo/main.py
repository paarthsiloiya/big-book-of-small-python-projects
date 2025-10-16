import bext, sys, random, time

WIDTH, HEIGHT = bext.size()
NUM_LOGOS = 5
LOGO = 'DVD'
PAUSE_TIME = 0.1
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

DIRECTIONS = ['ur', 'ul', 'dr', 'dl']

bext.clear()

logos = []
for _ in range(NUM_LOGOS):
    logos.append({
        'x': random.randint(1, WIDTH - len(LOGO) - 1),
        'y': random.randint(1, HEIGHT - 2),
        'color': random.choice(COLORS),
        'direction': random.choice(DIRECTIONS)
    })

    if logos[-1]['x'] % 2 == 1:
        logos[-1]['x'] += 1

while True:
    for logo in logos:
        bext.goto(logo['x'], logo['y'])
        print(' ' * len(LOGO), end='')

        if logo['direction'] == 'ur':
            logo['x'] += 2
            logo['y'] -= 1
        elif logo['direction'] == 'ul':
            logo['x'] -= 2
            logo['y'] -= 1
        elif logo['direction'] == 'dr':
            logo['x'] += 2
            logo['y'] += 1
        elif logo['direction'] == 'dl':
            logo['x'] -= 2
            logo['y'] += 1

        if logo['x'] <= 0:
            if logo['direction'] == 'ul':
                logo['direction'] = 'ur'
            elif logo['direction'] == 'dl':
                logo['direction'] = 'dr'
            logo['x'] = 1
            logo['color'] = random.choice(COLORS)
        elif logo['x'] >= WIDTH - len(LOGO):
            if logo['direction'] == 'ur':
                logo['direction'] = 'ul'
            elif logo['direction'] == 'dr':
                logo['direction'] = 'dl'
            logo['x'] = WIDTH - len(LOGO) - 1
            if logo['x'] % 2 == 1:
                logo['x'] -= 1
            logo['color'] = random.choice(COLORS)

        if logo['y'] <= 0:
            if logo['direction'] == 'ul':
                logo['direction'] = 'dl'
            elif logo['direction'] == 'ur':
                logo['direction'] = 'dr'
            logo['y'] = 1
            logo['color'] = random.choice(COLORS)
        elif logo['y'] >= HEIGHT - 1:
            if logo['direction'] == 'dl':
                logo['direction'] = 'ul'
            elif logo['direction'] == 'dr':
                logo['direction'] = 'ur'
            logo['y'] = HEIGHT - 2
            logo['color'] = random.choice(COLORS)

        bext.goto(logo['x'], logo['y'])
        bext.fg(logo['color'])
        print(LOGO, end='')
        bext.fg('white')
    sys.stdout.flush()
    time.sleep(PAUSE_TIME)
    

