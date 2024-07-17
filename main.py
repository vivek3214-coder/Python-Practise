print("welcome to the caluclator")
bill = float(input("what was your total bill $?\n"))
tip = int(input("what percentage tip do you want to give?\n"))
people = int(input("how many people are splitting the bill?\n"))
total_with_tip = int(tip/100 * bill + bill)
print(total_with_tip)
if total_with_tip > 50:
  print("That's a good tip Thank you!!")
     