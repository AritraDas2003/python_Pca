# abc = a^n+b^n+c^n
# n is the number of digits in the number

num = int(input("enter a number:"))

original = num
num = abs(num) # to handle negative numbers

count = 0
temp = num

if temp == 0:
  count = 1
else:
  while temp >0:
    dig = temp %10
    temp= temp//10
    count = count +1

sum_of_powers = 0
temp = num # second time because if the temp becomes 0  in the previous loop,then we can not calculate the sum of powers

while temp >0:
  dig = temp %10
  sum_of_powers = sum_of_powers + dig ** count # calculating the sum of the powers of the digits of the number using the count of the digits as the power
  temp= temp//10

if (original >=0) and (sum_of_powers == original):
  print(f"{original} is an armstrong number")
else:
  print(f"{original} is not an armstrong number")