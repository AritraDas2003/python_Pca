try:
  temp = float(input("Enter a temperature in Fahrenheit: "))
  celcious = (temp-32)* 5/9
  print(f"{temp} degrees Farenheit is equal to {celcious} degrees celcious")

except ValueError:
  print('value error, please enter a number')