from random import randint

print("")

while True:
    try:
        minimum = float(input("Enter a minimum value:"))
        maximum = float(input("Enter a maximum value:"))
    except:
        print("Oh no! That's not an integer :(. Rerun the program to try again.")
        break

    correctGuess = randint(minimum, maximum)
    print(correctGuess)

    try:
        userGuess = float(input("The program has generated a random number between " + str(minimum) + " and " + str(maximum) + "! Guess what it is!"))
    except:
        print("Oh no! That's not an integer :(. Rerun the program to try again.")
        break

    while userGuess != correctGuess:

        if userGuess > correctGuess:
            print("Guess lower!")

        elif userGuess < correctGuess:
            print("Guess higher!")

        try:
            userGuess = int(input("Guess the number!"))
        except:
            print("Oh no! That's not an integer :(. Rerun the program to try again.")
            break

    if (userGuess == correctGuess):
        print('You got the number right!')

    try:
        userPlayAgain = str(input("Do you want to play again? (y/n)"))
        if (userPlayAgain == "y" or userPlayAgain == "yes"):
            print("Ok! Starting again...")

        elif (userPlayAgain == "n" or userPlayAgain == "no"):
            print ("Ok! Breaking Loop...")
            break

        else:
            print("Oh no! That's not an accepted answer :(. Rerun the program to try again.")
            break
    except:
        print("Oh no! That's not a string :(. Rerun the program to try again.")
        break