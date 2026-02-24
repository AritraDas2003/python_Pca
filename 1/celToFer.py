try:
  temp = float(input('enter temp in cel..: '))
  ferr = (temp *1.8) + 32
  #  for fer to cell
  # c = (f-32)/1.8

  print(f'temp in fer is {ferr}')

except ValueError:
  print('invalid type')