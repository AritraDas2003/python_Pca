# abc = a^n + b^n + c^n where n is the number of digits in the number
def check_armstrong_number(num):

  original = num
  num = abs(num)

  temp = num
  count = 0

  # count digits
  if temp ==0:
    return 1
  else:
    while temp > 0:
       count += 1
       temp = temp //10

  #  sum of power
  temp = num
  sum_of_pow = 0

  while temp > 0:
     dig = temp % 10 # --> we get digit form here
     sum_of_pow += dig ** count
     temp = temp // 10

  if original >= 0 and sum_of_pow == original:
    print(f"{original} is an Armstrong number")
  else:
    print(f"{original} is not an Armstrong number")


try:
  num = int(input("enter a number: "))
  check_armstrong_number(num)
except ValueError:
  print("Please enter a valid integer")
