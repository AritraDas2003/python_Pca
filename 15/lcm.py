# Program to calculate LCM using GCD

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

num1 = abs(num1)
num2 = abs(num2)

lcm = (num1 * num2) // gcd(num1, num2)

print("LCM is:", lcm)