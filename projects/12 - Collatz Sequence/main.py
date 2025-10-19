import numpy as np
import matplotlib.pyplot as plt

def collatz_sequence(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

def plot_collatz_sequence(sequence):
    plt.figure(figsize=(10, 6))
    plt.plot(sequence, marker='o')
    plt.title('Collatz Sequence')
    plt.xlabel('Step')
    plt.ylabel('Value')
    plt.grid(True)
    plt.show()

while True:
    n = int(input("Enter a positive integer to generate its Collatz sequence: "))
    if n > 0:
        break
    print("Please enter a positive integer.")

sequence = collatz_sequence(n)
print("Collatz sequence:", sequence)
plot_collatz_sequence(sequence)