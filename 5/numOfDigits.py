def count_digits_safe(num):
    if not isinstance(num,int):
       print("Input is not an integer!!, Please enter a valid input:")
       exit()
    if num == 0:
        return 1
    else:
        if num < 0:
           num = -num # using unary operator to make a negetive number positive - (-2) = 2

        count = 0

        while num > 0:
            count = count + 1
            num = num //10
        return count

try:
    user_input = input("Enter an integer: ")
    num = int(user_input)
    digit_count = count_digits_safe(num)
    print(f"The number of digits in {num} is: {digit_count}")
except ValueError:
    print("Invalid input. Please enter an integer.")