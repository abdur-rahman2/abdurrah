import random
DiceRolling = True
while DiceRolling:
    print(random.randint(1,6))
    playAgain = input("Would you like to play again?[y/n]:y")
    if playAgain == "y":
        continue
    else:
        print("Thank you for playing")

        break
