import os
import sys


def get_terminal_size():
    try:
        size = os.get_terminal_size()
        return size.columns, size.lines
    except (AttributeError, OSError):
        return 80, 24


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_hex_pattern_1(width, height):
    hex_width = 4
    hex_height = 2
    
    x_repeat = max(1, width // hex_width)
    y_repeat = max(1, (height - 5) // hex_height)
    
    print("HEX PATTERN 1 - Classic Tessellation")
    print("=" * min(width, 50))
    
    for y in range(y_repeat):
        for x in range(x_repeat):
            print(r'/ \_', end='')
        print()
        
        for x in range(x_repeat):
            print(r'\_/ ', end='')
        print()


def draw_hex_pattern_2(width, height):
    hex_width = 6
    hex_height = 2
    
    x_repeat = max(1, width // hex_width)
    y_repeat = max(1, (height - 5) // hex_height)
    
    print("HEX PATTERN 2 - Honeycomb Style")
    print("=" * min(width, 50))
    
    for y in range(y_repeat):
        if y % 2 == 0:
            for x in range(x_repeat):
                print(r' /\_/ ', end='')
            print()
            
            for x in range(x_repeat):
                print(r' \_/\ ', end='')
            print()
        else:
            print("   ", end='')
            for x in range(max(0, x_repeat - 1)):
                print(r' /\_/ ', end='')
            print()
            
            print("   ", end='')
            for x in range(max(0, x_repeat - 1)):
                print(r' \_/\ ', end='')
            print()


def draw_animated_hex():
    width, height = get_terminal_size()
    
    patterns = ['*', '◆', '●', '▲', '■']
    
    for frame in range(20):
        clear_screen()
        pattern = patterns[frame % len(patterns)]
        
        print(f"ANIMATED HEX PATTERN - Frame {frame + 1}/20")
        print("=" * min(width, 50))
        
        x_repeat = max(1, width // 4)
        y_repeat = max(1, (height - 5) // 2)
        
        for y in range(y_repeat):
            for x in range(x_repeat):
                if (x + y + frame) % 3 == 0:
                    print(f'/{pattern}\\_', end='')
                else:
                    print(r'/ \_', end='')
            print()
            
            for x in range(x_repeat):
                if (x + y + frame) % 3 == 0:
                    print(f'\\{pattern}/ ', end='')
                else:
                    print(r'\_/ ', end='')
            print()
        
        import time
        time.sleep(0.2)


def main():
    clear_screen()
    width, height = get_terminal_size()
    
    print("╔" + "═" * 48 + "╗")
    print("║" + " " * 15 + "HEX GRID GENERATOR" + " " * 15 + "║")
    print("╚" + "═" * 48 + "╝")
    print(f"\nTerminal Size Detected: {width} × {height}")
    print("\nChoose a hex pattern:")
    print("1. Classic Tessellation")
    print("2. Honeycomb Style") 
    print("3. Animated Pattern")
    print("4. Show All Patterns")
    print("5. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                clear_screen()
                draw_hex_pattern_1(width, height)
                input("\nPress Enter to return to menu...")
                main()
                break
            elif choice == '2':
                clear_screen()
                draw_hex_pattern_2(width, height)
                input("\nPress Enter to return to menu...")
                main()
                break
            elif choice == '3':
                draw_animated_hex()
                main()
                break
            elif choice == '4':
                clear_screen()
                draw_hex_pattern_1(width, height)
                print("\n" + "─" * min(width, 50))
                draw_hex_pattern_2(width, height)
                input("\nPress Enter to return to menu...")
                main()
                break
            elif choice == '5':
                clear_screen()
                print("Thanks for using Hex Grid Generator!")
                sys.exit()
            else:
                print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
        except (EOFError, KeyboardInterrupt):
            clear_screen()
            print("\nGoodbye!")
            sys.exit()


if __name__ == '__main__':
    main()
