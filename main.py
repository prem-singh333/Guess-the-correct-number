from random import randint

computer = randint(1, 100)

player = 0
guess = 0

while(player != computer):
    guess += 1

    player = int(input("Guess the number: "))

    if(computer == player):
        print("")
        print(f"Congratulations! You won the game in {guess} attempts.")
        break

    if(player > computer):
        print("Higher number, please try again")
    elif(player < computer):
        print("Lower number, please try again")