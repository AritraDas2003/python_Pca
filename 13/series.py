# Program to calculate e^x up to nth term

def exp_series(x, n):

    sum_series = 1  # First term is 1
    term = 1        # To calculate each term

    for i in range(1, n):
        term = term * x / i
        sum_series += term

    return sum_series

try:
    x = float(input("Enter value of x: "))
    n = int(input("Enter number of terms: "))
    result = exp_series(x, n)
    print(f"Value of e^{x} up to {n} terms is: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")