import random
while True:
  n = random.randint(1,6)
  y = random.randint(1,6)
  x = input("Enter To roll The Dice")
  if x == "":
    print(f"The number in DICE of ur turn is {n}")
    if n == 6:
      print("Computer Won")
      break
    
    elif y == 6:
       print("you won")
       print(f"The number in DICE of computer turn is {y}")
       break
    print(f"The number in DICE of computer turn is {y}")
