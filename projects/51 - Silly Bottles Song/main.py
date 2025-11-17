import random
import sys
import time
import os

SPEED = 0.01
LINE_PAUSE = 1.5

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_settings():
    while True:
        try:
            start_bottles = input('Starting number of bottles (default 99): ').strip()
            start_bottles = int(start_bottles) if start_bottles else 99
            if start_bottles < 1:
                print('❌ Must start with at least 1 bottle!')
                continue
            
            speed_mode = input('Speed mode (1-Slow, 2-Medium, 3-Fast, default 2): ').strip()
            if speed_mode == '1':
                speed, pause = 0.05, 2.0
            elif speed_mode == '3':
                speed, pause = 0.001, 0.5
            else:
                speed, pause = 0.01, 1.5
            
            chaos_level = input('Chaos level (1-Mild, 2-Medium, 3-Wild, default 2): ').strip()
            chaos_level = int(chaos_level) if chaos_level in ['1', '2', '3'] else 2
            
            return start_bottles, speed, pause, chaos_level
            
        except ValueError:
            print('❌ Please enter valid numbers!')

def slow_print(text, pause_amount=0.1):
    for character in text:
        print(character, flush=True, end='')
        time.sleep(pause_amount)
    print()

def colorize_text(text, verse_num):
    colors = ['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m']
    reset = '\033[0m'
    
    if verse_num % 10 == 0:
        return f'{colors[verse_num % len(colors)]}{text}{reset}'
    return text

def apply_chaos_effect(line, chaos_level):
    if len(line) < 2:
        return line
    
    line_list = list(line)
    num_effects = min(chaos_level, len(line) // 3)
    
    for _ in range(num_effects):
        effect = random.randint(0, 5)
        
        if effect == 0 and len(line_list) > 0:
            char_index = random.randint(0, len(line_list) - 1)
            line_list[char_index] = ' '
        elif effect == 1 and len(line_list) > 0:
            char_index = random.randint(0, len(line_list) - 1)
            if line_list[char_index].isupper():
                line_list[char_index] = line_list[char_index].lower()
            elif line_list[char_index].islower():
                line_list[char_index] = line_list[char_index].upper()
        elif effect == 2 and len(line_list) > 1:
            char_index = random.randint(0, len(line_list) - 2)
            line_list[char_index], line_list[char_index + 1] = line_list[char_index + 1], line_list[char_index]
        elif effect == 3 and len(line_list) > 0:
            char_index = random.randint(0, len(line_list) - 1)
            line_list.insert(char_index, line_list[char_index])
        elif effect == 4 and len(line_list) > 0:
            char_index = random.randint(0, len(line_list) - 1)
            replacements = {'a': '@', 'e': '3', 'i': '!', 'o': '0', 's': '$', 't': '7'}
            char = line_list[char_index].lower()
            if char in replacements:
                line_list[char_index] = replacements[char]
        elif effect == 5 and len(line_list) > 2:
            char_index = random.randint(1, len(line_list) - 2)
            line_list[char_index] = random.choice('xyzqwp')
    
    return ''.join(line_list)

def display_progress(current_bottles, total_bottles):
    progress = (total_bottles - current_bottles) / total_bottles * 100
    bar_length = 20
    filled_length = int(bar_length * progress // 100)
    bar = '█' * filled_length + '░' * (bar_length - filled_length)
    print(f'\n🎵 Progress: [{bar}] {progress:.1f}% ({total_bottles - current_bottles}/{total_bottles} verses)')

def save_corrupted_lyrics(lines, verse_num):
    try:
        with open(f'corrupted_lyrics_verse_{verse_num}.txt', 'w') as f:
            f.write(f'Corrupted Lyrics at Verse {verse_num}\n')
            f.write('=' * 40 + '\n')
            for i, line in enumerate(lines):
                f.write(f'Line {i+1}: {line}\n')
        return True
    except:
        return False

def main():    
    start_bottles, speed, line_pause, chaos_level = get_settings()
    
    print('\n🎵 Starting the Silly Bottles Song! (Press Ctrl-C to stop)')
    input('Press Enter to begin...')
    
    bottles = start_bottles
    verse_count = 0
    
    lines = [
        ' bottles of milk on the wall,',
        ' bottles of milk,',
        'Take one down, pass it around,',
        ' bottles of milk on the wall!'
    ]
    
    try:
        while bottles > 0:
            verse_count += 1
            
            if verse_count % 10 == 0:
                display_progress(bottles, start_bottles)
                time.sleep(1)
            
            current_line_0 = str(bottles) + lines[0]
            current_line_1 = str(bottles) + lines[1]
            
            slow_print(colorize_text(current_line_0, verse_count), speed)
            time.sleep(line_pause)
            slow_print(colorize_text(current_line_1, verse_count), speed)
            time.sleep(line_pause)
            slow_print(colorize_text(lines[2], verse_count), speed)
            time.sleep(line_pause)
            
            bottles -= 1
            
            if bottles > 0:
                final_line = str(bottles) + lines[3]
                if bottles == 1:
                    final_line = final_line.replace('bottles', 'bottle')
                slow_print(colorize_text(final_line, verse_count), speed)
            else:
                slow_print(colorize_text('No more bottles of milk on the wall!', verse_count), speed)
            
            time.sleep(line_pause)
            print()
            
            if bottles > 0:
                line_to_corrupt = random.randint(0, 3)
                original_line = lines[line_to_corrupt]
                lines[line_to_corrupt] = apply_chaos_effect(lines[line_to_corrupt], chaos_level)
                
                if verse_count % 25 == 0:
                    save_corrupted_lyrics(lines, verse_count)
                
                corruption_level = sum(1 for c1, c2 in zip(original_line, lines[line_to_corrupt]) if c1 != c2)
                if corruption_level > len(original_line) * 0.8:
                    print(f'🎭 Maximum chaos reached at verse {verse_count}! ')
                    
    except KeyboardInterrupt:
        print('\n\n🎵 Song interrupted! Thanks for listening! 🎵')
    
    print(f'\n🎊 Song completed after {verse_count} verses!')
    print(f'📊 Final corruption statistics:')
    for i, line in enumerate(lines):
        print(f'   Line {i+1}: {len([c for c in line if not c.isalnum() and c != " "])} special characters')
    
    choice = input('\nSave final corrupted lyrics? (y/n): ').lower()
    if choice in ['y', 'yes']:
        if save_corrupted_lyrics(lines, verse_count):
            print('💾 Lyrics saved!')
        else:
            print('❌ Could not save lyrics.')

if __name__ == '__main__':
    main()