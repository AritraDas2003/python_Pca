def is_prime(num):
    if num <= 1:
        print(num, "is not a Prime number")
    else:
        factor_count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                factor_count += 1
# for prime count the factors and if the count is 2 then its a prime number otherwise not a prime number
        if factor_count == 2:
            print(num, "is a Prime number")
        else:
            print(num, "is not a Prime number")

# Call the function
try:
    num = int(input("Enter a number: "))
    is_prime(num)
except ValueError:
    print("Please enter a valid integer")