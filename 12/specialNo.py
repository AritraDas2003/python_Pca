# Program to check Special Number
#abc=a!+b!+c!

num = int(input("Enter a number: "))

original = num
num = abs(num)

sum_of_factorials = 0
temp = num

while temp > 0:
    digit = temp % 10

    # Calculate factorial of digit
    fact = 1
    for i in range(1, digit + 1):
        fact *= i

    sum_of_factorials += fact
    temp = temp // 10

if original >= 0 and sum_of_factorials == num:
    print(original, "is a Special Number")
else:
    print(original, "is not a Special Number")