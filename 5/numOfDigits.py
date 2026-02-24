try:
  original_num = input("Enter a number:")
  num = float(original_num)

  num = abs(num)

  count = 0

  str_num = str(num)

  for char in str_num:
    if char != '.':
      count += 1
  print (f"number of digits in {num} is {count}")

except ValueError:
  print(f"Invalid input, please enter a valid number you entered  < {original_num} >")