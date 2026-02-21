num = int(input("Enter a number: "))
if (num < 0):
  print("negetive number can not be squared")

# first taking root of the number and then, checking if the squre of  the 'root' i.e: root*root = original_number
else:
  root = num ** 0.5
  # the square of the root is the original number-- must satisfy to be a perfect square number
  if (root*root == num):
    print("the number is perfect square")
  else:
    print("the number is not perfect square")