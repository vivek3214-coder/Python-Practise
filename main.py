print("welcome to the rollercoaster")
height = int(input("what is your height in cm? "))
bill = 0
if height >= 120:
  print("you can ride the rollercoaster")
  age = int(input("what is your age? "))
  if age < 12:
    bill = 5
    print("Child pay $5")
  elif age <= 18:
    bill = 7
    print("Youth pay $7")
  else:
    bill = 12
    print("Adult pay $12")
  photo = input("Do you need a photo copy? Y or N ")
  if photo == "Y":
    bill = bill + 3
    print(f"Your total is {bill}")
  else:
    bill = bill + 0
    print(f"Your total is {bill}")
else:
  print("sorry, you have to grow taller before you can ride")