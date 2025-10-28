def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

while True:
    while True:
        try:
            num_terms = int(input("Enter the number of terms in the Fibonacci sequence you want: "))
            if num_terms <= 0:
                print("Please enter a positive integer.")
                continue
            sequence = fibonacci_sequence(num_terms)
            print(f"The first {num_terms} terms of the Fibonacci sequence are: \n{','.join(map(str, sequence))}")
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    again = input("Do you want to generate another Fibonacci sequence? (yes/no): ").strip().lower()
    if again != 'yes':
        print("Thank you for using the Fibonacci sequence generator. Goodbye!")
        break