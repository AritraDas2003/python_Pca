num = int (input("Enter a number: "))
if (num < 0):
  print("negetive number can not be factorial")
elif (num ==0 or num ==1):
  print(f"factorial of {num} is 1")
else:
  fact =1
  for i in range(2,num+1):
    fact = fact * i
  print(f"factorial of {num} is {fact}")

