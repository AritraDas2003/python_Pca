marks =[]
# taking inputs for marks of 4 subjects
for i in range(1,5):
  mark =float(input(f"Enter the marks of subject {i}: "))
  if 0<= mark <=100:
    marks.append(mark)
  else:
    print("Invalid mark, please enter a number between 0 and 100")
    exit()

#sum of marks
total=0

for i in marks:
  total = total + i

aggregate = total/4

print(f"total marks:{total}")
print(f"Aggregate marks:{aggregate}")

if aggregate >=60:
  print("1st division")
elif aggregate >=45:
  print("2nd division")
elif aggregate >=30:
  print("3rd division")
else: print ("Fail")
