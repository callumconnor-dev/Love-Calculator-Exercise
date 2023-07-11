print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = (f"{name1.lower()}{name2.lower()}")

trueAmount = name.count('t') + name.count('r') + name.count('u') + name.count('e')
loveAmount = name.count('l') + name.count('o') + name.count('v') + name.count('e')

nameAmount = int(f"{trueAmount}{loveAmount}")

if nameAmount <= 10 or nameAmount >= 90:
  print(f"Your score is {nameAmount}, you go together like coke and mentos.")

elif nameAmount >= 40 and nameAmount <= 50:
  print(f"Your score is {nameAmount}, you are alright together.")

else: 
  print(f"Your score is {nameAmount}.")