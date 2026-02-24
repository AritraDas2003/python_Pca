num = int(input("Enter a number: "))

temp = num
rev = 0

while temp >0:
  dig =temp%10
  rev = rev*10 + dig
  temp = temp//10

if rev == num:
  print("number is palindrom")
else:
  print("Its not palindrom")