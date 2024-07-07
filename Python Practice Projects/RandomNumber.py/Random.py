import random

userRange = 0
while True:
    userRange = int(input("Enter max Range : "))
    if userRange > 0:
        break
    else:
        print("Please provide greater than 0 value.")


randomNumber = random.randint(0, userRange)
trys = 0

while True:
    userNumber = int(input("Enter your choice : "))
    trys += 1
    if userNumber == randomNumber:
        print(f"You got the number in {trys} tries:")
        break
    if userNumber > randomNumber:
        print("You are above the number.")
    else:
        print("You are below the number.")
