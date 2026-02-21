num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a Prime number")
else:
    factor_count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            factor_count += 1  # counting the number of factors of the given number

    if factor_count == 2:
        print(num, "is a Prime number") # because prime number has only two factors: 1 and itself
    else:
        print(num, "is not a Prime number")