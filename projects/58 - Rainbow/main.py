import time, sys

try:
    import bext
except ImportError:
    sys.exit('This program requires the bext module. Install it with: pip install bext')

def main():
    indent = 0
    increasing = True
    colors = ['red', 'yellow', 'green', 'blue', 'cyan', 'purple']

    try:
        while True:
            print(' ' * indent, end='')
            for color in colors:
                bext.fg(color)
                print('##', end='')
            print()

            if increasing:
                indent += 1
                if indent == 60:
                    increasing = False
            else:
                indent -= 1
                if indent == 0:
                    increasing = True
            
            time.sleep(0.02)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
