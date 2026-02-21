# Program to calculate e^x up to nth term

x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum_series = 1  # First term is 1
term = 1        # To calculate each term

for i in range(1, n):
    term = term * x / i
    sum_series += term

print("Value of e^", x, "up to", n, "terms is:", sum_series)