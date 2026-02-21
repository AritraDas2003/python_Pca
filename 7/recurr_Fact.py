def fact(num):
  if num<0:
    return "negetive number can not be factorial"
  elif(num==0 or num ==1): # base case
    return 1
  else:
    return num * fact(num-1) # callinf the same function with num-1 until base case( 0 or 1)

num = int (input("Enter a number: "))
print(f"factorial of {num} is {fact(num)}")