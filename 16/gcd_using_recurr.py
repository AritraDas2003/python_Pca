# Program to calculate GCD using recursion

def gcd(a, b):
    if b == 0:          # Base case
        return a
    else:
        return gcd(b, a % b)   # Recursive call


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Handle negative numbers
num1 = abs(num1)
num2 = abs(num2)

result = gcd(num1, num2)

print("GCD is:", result)