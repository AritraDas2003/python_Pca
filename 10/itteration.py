# Fibonacci series using iteration

def fibonacci(n):
    if n <= 0:
        print("Please enter a positive number.")
    elif n == 1:
        print(0)
    else:
        print("Fibonacci Series:")
        a = 0
        b = 1
        print(a, end=" ")
        print(b, end=" ")

        for i in range(2, n):
            c = a + b
            print(c, end=" ")
            a = b
            b = c

# Main code
n = int(input("Enter number of terms: "))
fibonacci(n)