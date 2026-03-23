def find_gcd(a, b):
    while b != 0:
        remainder = a % b
        a = b
        b = remainder
    return a


# Taking input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

gcd = find_gcd(num1, num2)

print("GCD of", num1, "and", num2, "is:", gcd)