num = int (input("enter a number"))
count = 0

# base condion for 0 as it has 1 digit
# the loop comes to this condition when the number is reduced to 0 after removing all digits
if num == 0:
  count = 1
else:
  while num>0:
    dig = num%10 #to get the last digit
    count = count +1 #to count the number of digits
    num = num//10 #to remove the last digit


print(f"number of digits in the number is {count}")
