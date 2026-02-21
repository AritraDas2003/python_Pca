# Program to check Perfect Number

num = int(input("Enter a number: "))

if num <= 0:
    print("Please enter a positive number.")
else:
    sum_of_factors = 0

    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i

    if sum_of_factors == num:
        print(num, "is a Perfect Number")
    else:
        print(num, "is not a Perfect Number")