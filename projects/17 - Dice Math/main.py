import random, time, bext, sys, threading

die_template = """┌───────┐
│ {0} {1} {2} │
│ {3} {4} {5} │
│ {6} {7} {8} │
└───────┘"""

PIP = "●"
BLANK = " "

DIE_FACES = {
    1: [BLANK, BLANK, BLANK,
        BLANK, PIP, BLANK,
        BLANK, BLANK, BLANK],
    2: [PIP, BLANK, BLANK,
        BLANK, BLANK, BLANK,
        BLANK, BLANK, PIP],
    3: [PIP, BLANK, BLANK,
        BLANK, PIP, BLANK,
        BLANK, BLANK, PIP],
    4: [PIP, BLANK, PIP,
        BLANK, BLANK, BLANK,
        PIP, BLANK, PIP],
    5: [PIP, BLANK, PIP,
        BLANK, PIP, BLANK,
        PIP, BLANK, PIP],
    6: [PIP, BLANK, PIP,
        PIP, BLANK, PIP,
        PIP, BLANK, PIP]
}

OPPOSITE_FACES = {1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

MIN_DICE = 2
MAX_DICE = 6
QUIZ_DURATION = 30
ROLLING_DURATION = 5  # 5 seconds of rolling before quiz starts
PAUSE_TIME = 0.15     # Pause between movements

CANVAS_WIDTH = 80
CANVAS_HEIGHT = 15
DIE_WIDTH = 9
DIE_HEIGHT = 5

DIRECTIONS = ['ur', 'ul', 'dr', 'dl']

def get_valid_face_change(current_face):
    valid_faces = [face for face in range(1, 7) if face != OPPOSITE_FACES[current_face]]
    return random.choice(valid_faces)

def clear_die_area(x, y):
    for row in range(DIE_HEIGHT):
        if y + row < CANVAS_HEIGHT - 1:
            bext.goto(x, y + row)
            print(' ' * DIE_WIDTH, end='', flush=True)

def draw_die(x, y, face_value):
    die_lines = die_template.format(*DIE_FACES[face_value]).split('\n')
    for i, line in enumerate(die_lines):
        if y + i < CANVAS_HEIGHT - 1:
            bext.goto(x, y + i)
            print(line, end='')

def draw_canvas():
    bext.clear()
    print('┌' + '─' * (CANVAS_WIDTH - 2) + '┐')
    for i in range(CANVAS_HEIGHT - 2):
        print('│' + ' ' * (CANVAS_WIDTH - 2) + '│')
    print('└' + '─' * (CANVAS_WIDTH - 2) + '┘')

def check_collision(die1, die2):
    die1_right = die1['x'] + DIE_WIDTH
    die1_bottom = die1['y'] + DIE_HEIGHT
    die2_right = die2['x'] + DIE_WIDTH
    die2_bottom = die2['y'] + DIE_HEIGHT
    
    return not (die1_right <= die2['x'] or die2_right <= die1['x'] or 
                die1_bottom <= die2['y'] or die2_bottom <= die1['y'])

def is_position_valid(x, y, dice, exclude_index=-1):
    test_die = {'x': x, 'y': y}
    for i, die in enumerate(dice):
        if i != exclude_index and check_collision(test_die, die):
            return False
    return True

def get_valid_position(dice):
    max_attempts = 100
    for _ in range(max_attempts):
        x = random.randint(2, CANVAS_WIDTH - DIE_WIDTH - 2)
        y = random.randint(2, CANVAS_HEIGHT - DIE_HEIGHT - 2)
        if is_position_valid(x, y, dice):
            return x, y
    return random.randint(2, CANVAS_WIDTH - DIE_WIDTH - 2), random.randint(2, CANVAS_HEIGHT - DIE_HEIGHT - 2)

def handle_dice_collisions(dice):
    for i in range(len(dice)):
        for j in range(i + 1, len(dice)):
            if check_collision(dice[i], dice[j]):
                direction_opposites = {
                    'ur': 'dl', 'ul': 'dr', 'dr': 'ul', 'dl': 'ur'
                }
                
                dice[i]['direction'] = direction_opposites[dice[i]['direction']]
                dice[j]['direction'] = direction_opposites[dice[j]['direction']]
                
                dice[i]['face'] = get_valid_face_change(dice[i]['face'])
                dice[j]['face'] = get_valid_face_change(dice[j]['face'])
                
                if dice[i]['x'] < dice[j]['x']:
                    dice[i]['x'] = max(2, dice[i]['x'] - 2)
                    dice[j]['x'] = min(CANVAS_WIDTH - DIE_WIDTH - 2, dice[j]['x'] + 2)
                else:
                    dice[i]['x'] = min(CANVAS_WIDTH - DIE_WIDTH - 2, dice[i]['x'] + 2)
                    dice[j]['x'] = max(2, dice[j]['x'] - 2)
                
                if dice[i]['y'] < dice[j]['y']:
                    dice[i]['y'] = max(2, dice[i]['y'] - 1)
                    dice[j]['y'] = min(CANVAS_HEIGHT - DIE_HEIGHT - 2, dice[j]['y'] + 1)
                else:
                    dice[i]['y'] = min(CANVAS_HEIGHT - DIE_HEIGHT - 2, dice[i]['y'] + 1)
                    dice[j]['y'] = max(2, dice[j]['y'] - 1)

def get_user_input_with_timeout(timeout):
    result = [None]
    
    def input_thread():
        try:
            result[0] = input()
        except:
            pass
    
    thread = threading.Thread(target=input_thread)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    
    return result[0]

def main():
    bext.clear()
    
    print("BOUNCING DICE ADDITION QUIZ")
    print("=" * 50)
    print("Watch the dice bounce around for 5 seconds,")
    print("then add up all the visible faces when they stop!")
    print("Press Enter to start...")
    input()
    
    num_dice = random.randint(MIN_DICE, MAX_DICE)
    dice = []
    
    for _ in range(num_dice):
        x, y = get_valid_position(dice)
        
        dice.append({
            'x': x,
            'y': y,
            'face': random.randint(1, 6),
            'direction': random.choice(DIRECTIONS)
        })
    
    draw_canvas()
    
    start_time = time.time()
    bext.goto(1, CANVAS_HEIGHT)
    print("Dice are rolling... ", end='')
    sys.stdout.flush()
    
    while time.time() - start_time < ROLLING_DURATION:
        for die in dice:
            clear_die_area(die['x'], die['y'])
            
            # Move die
            if die['direction'] == 'ur':
                die['x'] += 2
                die['y'] -= 1
            elif die['direction'] == 'ul':
                die['x'] -= 2
                die['y'] -= 1
            elif die['direction'] == 'dr':
                die['x'] += 2
                die['y'] += 1
            elif die['direction'] == 'dl':
                die['x'] -= 2
                die['y'] += 1
            
            if die['x'] <= 1:
                if die['direction'] == 'ul':
                    die['direction'] = 'ur'
                elif die['direction'] == 'dl':
                    die['direction'] = 'dr'
                die['x'] = 2
                die['face'] = get_valid_face_change(die['face'])
            elif die['x'] >= CANVAS_WIDTH - DIE_WIDTH - 1:
                if die['direction'] == 'ur':
                    die['direction'] = 'ul'
                elif die['direction'] == 'dr':
                    die['direction'] = 'dl'
                die['x'] = CANVAS_WIDTH - DIE_WIDTH - 2
                die['face'] = get_valid_face_change(die['face'])
            
            if die['y'] <= 1:
                if die['direction'] == 'ul':
                    die['direction'] = 'dl'
                elif die['direction'] == 'ur':
                    die['direction'] = 'dr'
                die['y'] = 2
                die['face'] = get_valid_face_change(die['face'])
            elif die['y'] >= CANVAS_HEIGHT - DIE_HEIGHT - 1:
                if die['direction'] == 'dl':
                    die['direction'] = 'ul'
                elif die['direction'] == 'dr':
                    die['direction'] = 'ur'
                die['y'] = CANVAS_HEIGHT - DIE_HEIGHT - 2
                die['face'] = get_valid_face_change(die['face'])
        
        handle_dice_collisions(dice)
        
        for die in dice:
            draw_die(die['x'], die['y'], die['face'])
        
        sys.stdout.flush()
        time.sleep(PAUSE_TIME)
    
    bext.goto(1, CANVAS_HEIGHT)
    print("DICE STOPPED! Add up all the visible faces: ", end='')
    sys.stdout.flush()
    
    correct_answer = sum(die['face'] for die in dice)
    
    user_answer = get_user_input_with_timeout(QUIZ_DURATION)
    
    bext.goto(1, CANVAS_HEIGHT + 1)
    if user_answer is None:
        print(f"Time's up! The correct answer was {correct_answer}")
    else:
        try:
            user_answer = int(user_answer)
            if user_answer == correct_answer:
                print(f"Correct! The answer was {correct_answer}")
            else:
                print(f"Wrong! You said {user_answer}, but the correct answer was {correct_answer}")
        except ValueError:
            print(f"Invalid input! The correct answer was {correct_answer}")
    
    bext.goto(1, CANVAS_HEIGHT + 2)
    print("Die values were: " + " + ".join(str(die['face']) for die in dice) + f" = {correct_answer}")
    
    bext.goto(1, CANVAS_HEIGHT + 3)
    print("Press Enter to play again or Ctrl+C to quit...")
    try:
        input()
        main()
    except KeyboardInterrupt:
        print("\nThanks for playing!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nThanks for playing!")