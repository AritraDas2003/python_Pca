def is_leap_year(year):
  if year < 1:
    print("Please enter a valid year")
  elif (year%4 == 0 and year%100 != 0) or (year %400 == 0 ):
    print("year Is a leap year ")
  else:
    print("year is not a leap year")

try:
  user_input = input("enter year to check :")
  is_leap_year(int(user_input))
except ValueError:
  print(f"Invalid input you entered: {user_input}")