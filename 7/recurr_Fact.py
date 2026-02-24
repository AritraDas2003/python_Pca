def fact(num):
  if num<0:
    print("can not perform on numbers less than 0")
  elif(num ==0 or num ==1):
    return 1
  else:
    return num*fact(num-1)

num = int(input("enter the number: "))

print(f"factorial of {num} is {fact(num)}")
