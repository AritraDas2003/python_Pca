def find_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a

def find_lcm(a, b):
    gcd = find_gcd(a, b)
    return (a * b) // gcd

# Input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))