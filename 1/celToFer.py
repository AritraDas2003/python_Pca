try:
  temp = float(input("Enter the number in celcious: "))
  ferhenhiet = (temp/ 5)*9 + 32
  print(f"{temp} degrees Celcious is equal to {ferhenhiet} degrees Ferhenhiet")
except ValueError:
  print('Vallue Error,please enter corrrect number ')