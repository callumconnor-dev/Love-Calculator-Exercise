print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

name1Amount = name1.count('t') + name1.count('r') + name1.count('u') + name1.count('e') + name1.count('l') + name1.count('o') + name1.count('v') 
name2Amount = name2.count('t') + name2.count('r') + name2.count('u') + name2.count('e') + name2.count('l') + name2.count('o') + name2.count('v') 

nameAmount = int(f"{name1Amount}{name2Amount}")

if nameAmount <= 10 or nameAmount >= 90:
  print(f"Your score is {nameAmount}, you go together like coke and mentos.")

elif nameAmount <= 40 and nameAmount >= 50:
  print(f"Your score is {nameAmount}, you are alright together.")

else: 
  print(f"Your score is {nameAmount}.")