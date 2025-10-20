import os, time

seven_seg_digits = {
        '0': "┌───┐\n│   │\n│   │\n│   │\n└───┘",
        '1': "  ┐  \n  │  \n  │  \n  │  \n──┴──",
        '2': "────┐\n    │\n┌───┘\n│    \n└────",
        '3': "────┐\n    │\n────┤\n    │\n────┘",
        '4': "│   │\n│   │\n└───┤\n    │\n    │",
        '5': "┌────\n│    \n└───┐\n    │\n────┘",
        '6': "┌────\n│    \n├───┐\n│   │\n└───┘",
        '7': "────┐\n    │\n    │\n    │\n    │",
        '8': "┌───┐\n│   │\n├───┤\n│   │\n└───┘",
        '9': "┌───┐\n│   │\n└───┤\n    │\n────┘",
        ':': "     \n  ░  \n     \n  ░  \n     "
    }

def print_seven_seg_clock(hrs, mins, secs):
    

    time_str = f"{hrs:02}:{mins:02}:{secs:02}"
    lines = ["", "", "", "", ""]
    for char in time_str:
        digit_lines = seven_seg_digits[char].split('\n')
        for i in range(5):
            lines[i] += digit_lines[i] + "  "
    clear_screen()
    for line in lines:
        print(line)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

seconds_left = int(input("Enter the number of seconds to count down from: "))
while seconds_left > 0:
    hrs, rem = divmod(seconds_left, 3600)
    mins, secs = divmod(rem, 60)
    print_seven_seg_clock(hrs, mins, secs)
    time.sleep(1)
    seconds_left -= 1