# Program to calculate GCD using recursion

def gcd(a, b):
    # Handle negative numbers inside the function
    a = abs(a)
    b = abs(b)

    if b == 0:          # Base case
        return a
    else:
        return gcd(b, a % b)   # Recursive call

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = gcd(num1, num2)
    print("GCD is:", result)
except ValueError:
    print("Invalid input. Please enter integers.")