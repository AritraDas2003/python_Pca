def fact(num):
  if num < 0:
    print("Can not operate on numbers less than 0")
    exit()
  elif(num ==1 or num ==0):
    return 1
  else:
    return num*fact(num-1)


num = int(input("enter the number: "))
factorial = fact(num)
print(f"factorial of {num} is {factorial}")
