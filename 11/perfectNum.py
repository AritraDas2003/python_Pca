# Program to check Perfect Number
# perfect number is a positive integer that is equal to the sum of its proper divisors, 'excluding itself'. For example, 6 is a perfect number because its divisors are 1, 2, and 3, and their sum is 6.

def check_perfect_number(num):

    if num <= 0:
        print("Please enter a positive number.")
        return False

    sum_of_factors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_factors += i

    if sum_of_factors == num:
        print(num, "is a Perfect Number")
        return True
    else:
        print(num, "is not a Perfect Number")
        return False


# Main code
num = int(input("Enter a number: "))
check_perfect_number(num)