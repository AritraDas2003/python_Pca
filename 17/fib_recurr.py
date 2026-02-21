# Recursive function to calculate Fibonacci term

def fibonacci(n):
    if n == 0:          # Base case
        return 0
    elif n == 1:        # Base case
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Main program
n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Series:")
    for i in range(n):
        print(fibonacci(i), end=" ")