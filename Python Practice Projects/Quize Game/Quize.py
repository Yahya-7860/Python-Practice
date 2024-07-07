print("Welcome to the Quize Game Show.")

GameChoice = input("Do you Want to play the game (y/n) : ")
score = 0

if GameChoice == 'y':
    print("AMAZING ! Let's play the GK Game.")

    if input("1. Who is the prime minister of india ?\n ans: ").lower() == 'narendra modi':
        print("CORRECT")
        score += 1
    else:
        print('WRONG!!!!')

    if input("1. what is the capital of india ?\n ans: ").lower() == 'delhi':
        print("CORRECT")
        score += 1
    else:
        print('WRONG!!!!')

    if input("1. which gas is known as life line gas ?\n ans: ").lower() == 'oxygen':
        print("CORRECT")
        score += 1
    else:
        print('WRONG!!!!')

else:
    print("Thanks for Visiting the Game. See you next time.")
    exit()

print('**************************************************')
print(f"You gave total {score} correct answers and {3-score} wrong answers.")
print(f'Your total score is {score}.')
print("Thanks for playing with us.")
