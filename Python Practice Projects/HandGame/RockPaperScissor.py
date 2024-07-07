import random

gameSet = ['rock', 'paper', 'scissor']
userWon = 0
compWon = 0
draw = 0
while True:
    randomNum = random.randint(0, 2)
    compChoice = gameSet[randomNum]

    choice = input('Enter rock or paper or scissor or q to quite the game : ')

    if choice.lower() == 'q':
        print(f'You won total {userWon} matches and computer won {compWon} matches. and {draw} draws.')
        break

    if choice.lower() == 'rock' and compChoice == 'rock':
        print(f'Both choose {choice}. Match Draw.')
        draw += 1

    elif choice.lower() == 'rock' and compChoice == 'paper':
        print(f'Computer chose {compChoice}')
        print('You lose.')
        compWon += 1

    elif choice.lower() == 'rock' and compChoice == 'scissor':
        print(f'Computer chose {compChoice}')
        print('You won.')
        userWon += 1

    elif choice.lower() == 'paper' and compChoice == 'rock':
        print(f'Computer chose {compChoice}')
        print('You won.')
        userWon += 1

    elif choice.lower() == 'paper' and compChoice == 'paper':
        print(f'Both choose {choice}. Match Draw.')
        draw += 1

    elif choice.lower() == 'paper' and compChoice == 'scissor':
        print(f'Computer chose {compChoice}')
        print('You lose.')
        compWon += 1

    elif choice.lower() == 'scissor' and compChoice == 'rock':
        print(f'Computer chose {compChoice}')
        print('You lose.')
        compWon += 1

    elif choice.lower() == 'scissor' and compChoice == 'paper':
        print(f'Computer chose {compChoice}')
        print('You won.')
        userWon += 1

    elif choice.lower() == 'scissor' and compChoice == 'scissor':
        print(f'Both choose {choice}. Match Draw.')
        draw += 1

    else:
        print("PLEASE CHOOSE A VALID STRING")
