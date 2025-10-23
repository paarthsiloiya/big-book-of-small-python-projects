import sys, time

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

    for line in lines:
        print(line)

while True:
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Clear the console
    sys.stdout.write("\033c")

    print_seven_seg_clock(hours, minutes, seconds)
    time.sleep(1)