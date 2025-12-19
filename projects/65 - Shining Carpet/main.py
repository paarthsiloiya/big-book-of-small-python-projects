import sys

try:
    width = int(input('Enter width (number of repeats): '))
    height = int(input('Enter height (number of repeats): '))
except ValueError:
    print('Please enter valid integers.')
    sys.exit()

if width <= 0 or height <= 0:
    print('Values must be positive.')
    sys.exit()

for i in range(height):
    print(r'_ \ \ \_/ __' * width)
    print(r' \ \ \___/ _' * width)
    print(r'\ \ \_____/ ' * width)
    print(r'/ / / ___ \_' * width)
    print(r'_/ / / _ \__' * width)
    print(r'__/ / / \___' * width)
