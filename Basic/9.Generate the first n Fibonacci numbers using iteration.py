#Generate the first n Fibonacci numbers using iteration.

# Program to generate the first n Fibonacci numbers using iteration

def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1   # first two Fibonacci numbers

    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # update values iteratively

    return fib_sequence


# Main program
if __name__ == "__main__":
    n = int(input("Enter how many Fibonacci numbers you want: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = fibonacci_iterative(n)
        print(f"First {n} Fibonacci numbers are: {result}")


#output
# Enter how many Fibonacci numbers you want: 9
# First 9 Fibonacci numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21]
