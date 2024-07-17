print("Welcome to the rollercoaster")
height = int(input("What is your height in cm?\n"))
if height >= 120:
  print("you can ride the rollercoaster")
  age = int(input("What is your age?\n"))
  if age <= 12:
    print("please pay $5")
  elif age <=18:
    print("please pay $12")
  else:
    print("please pay $17")
else:
  print("Sorry you cannot ride rollercoaster")
  