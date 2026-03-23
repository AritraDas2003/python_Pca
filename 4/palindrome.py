def is_palindrome(num):
  temp = num
  rev = 0

  while num >0:
    dig = num%10
    rev = rev*10 + dig
    num = num //10

  if rev == temp:
    print(f"{temp} is a palindrome")
  else:
    print(f"{temp} is not a palindrome")

num = input("Enter a number: ")
try:
  is_palindrome(int(num))
except ValueError:
  print("Invalid input. Please enter a valid integer.")