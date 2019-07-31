
correct = False
answer = 1
round = 1
while not(correct) and round < 4:

    print("Round ", round)
    guess = input("Guess a number between 1-10:  ")
    if int(guess) == answer:
        print("Correct")
        correct = True
    else:
        if round == 3:
            print("Game Over")
        else:
            print("Try Again\n")

    round += 1
