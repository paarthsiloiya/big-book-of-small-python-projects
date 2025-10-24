import random, time, os, sys

STREAM_CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{}|;:,.<>?"

GREEN = '\033[92m'
LIGHT_GREEN = '\033[32m'
WHITE = '\033[97m'
RESET = '\033[0m'

def get_terminal_size():
    try:
        if os.name == 'nt':
            import shutil
            columns, rows = shutil.get_terminal_size()
        else:
            rows, columns = os.popen('stty size', 'r').read().split()
            rows, columns = int(rows), int(columns)
    except:
        columns, rows = 80, 24
    return columns, rows

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def hide_cursor():
    print('\033[?25l', end='', flush=True)

def show_cursor():
    print('\033[?25h', end='', flush=True)

def goto(x, y):
    print(f'\033[{y};{x}H', end='', flush=True)

class DigitalStream:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.streams = []
        self.screen = [[' ' for _ in range(width)] for _ in range(height)]
        self.colors = [[RESET for _ in range(width)] for _ in range(height)]
        self.prev_screen = [[' ' for _ in range(width)] for _ in range(height)]
        self.prev_colors = [[RESET for _ in range(width)] for _ in range(height)]
        for x in range(width):
            stream = {
                'x': x,
                'y': random.randint(-height, 0),
                'length': random.randint(5, 25),
                'speed': random.choice([1, 2, 3]),
                'chars': [random.choice(STREAM_CHARS) for _ in range(random.randint(5, 25))],
                'frame_counter': 0
            }
            self.streams.append(stream)
    
    def update_streams(self):
        new_screen = [[' ' for _ in range(self.width)] for _ in range(self.height)]
        new_colors = [[RESET for _ in range(self.width)] for _ in range(self.height)]
        
        for stream in self.streams:
            stream['frame_counter'] += 1
            if stream['frame_counter'] >= stream['speed']:
                stream['frame_counter'] = 0
                stream['y'] += 1
                if random.random() < 0.3:
                    char_index = random.randint(0, len(stream['chars']) - 1)
                    stream['chars'][char_index] = random.choice(STREAM_CHARS)
            
            if stream['y'] > self.height + stream['length']:
                stream['y'] = random.randint(-stream['length'], -1)
                stream['length'] = random.randint(5, 25)
                stream['speed'] = random.choice([1, 2, 3])
                stream['chars'] = [random.choice(STREAM_CHARS) for _ in range(stream['length'])]
            
            for i, char in enumerate(stream['chars']):
                char_y = stream['y'] + i
                if 0 <= char_y < self.height:
                    new_screen[char_y][stream['x']] = char
                    if i == 0:
                        new_colors[char_y][stream['x']] = WHITE
                    elif i < len(stream['chars']) // 3:
                        new_colors[char_y][stream['x']] = LIGHT_GREEN
                    else:
                        new_colors[char_y][stream['x']] = GREEN
        
        self.screen = new_screen
        self.colors = new_colors
    
    def draw_streams(self):
        for y in range(self.height):
            for x in range(self.width):
                if (self.screen[y][x] != self.prev_screen[y][x] or 
                    self.colors[y][x] != self.prev_colors[y][x]):
                    goto(x + 1, y + 1)
                    color = self.colors[y][x]
                    char = self.screen[y][x]
                    print(f"{color}{char}{RESET}", end='', flush=True)
        
        self.prev_screen = [row[:] for row in self.screen]
        self.prev_colors = [row[:] for row in self.colors]

def main():
    try:
        width, height = get_terminal_size()
        print("Digital Stream - Matrix Effect")
        print(f"Terminal size: {width} x {height}")
        print("Press Ctrl+C to exit...")
        time.sleep(1)
        clear_screen()
        hide_cursor()
        digital_stream = DigitalStream(width, height)
        while True:
            digital_stream.update_streams()
            digital_stream.draw_streams()
            time.sleep(0.02)
    except KeyboardInterrupt:
        clear_screen()
        show_cursor()
        print("\nDigital stream terminated.")
        sys.exit()
    except Exception as e:
        show_cursor()
        print(f"\nError: {e}")
        sys.exit()

if __name__ == "__main__":
    main()