year = int(input("Enter a year: "))

if year<1:
  print("Invalid year, please enter a valid year")
elif (year%4==0 and year%100 !=0) or (year%400==0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not leap year")