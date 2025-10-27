import math, sys

while True:
    if len(sys.argv) > 1:
        num = sys.argv[1]

        try:
            num = int(num)
            if num < 1:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")
            sys.exit(1)

    else:
        num = input("Enter a positive integer to find its factors: ")

        try:
            num = int(num)
            if num < 1:
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid positive integer.")
            continue

factors = set()
for i in range(1, math.isqrt(num) + 1):
    if num % i == 0:
        factors.add(i)
        factors.add(num // i)

print(f"The factors of {num} are: {', '.join(map(str, factors))}")