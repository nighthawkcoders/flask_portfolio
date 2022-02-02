import unittest
import random

while True:

    minimum = (input("Enter minimum"))

    try:
        int(minimum)
    except:
        break

    maximum = (input("Enter maximum"))

    try:
        int(maximum)
    except:
        break

    correctGuess = random.randint(minimum, maximum)

    print(correctGuess)

    playAgain = input("Do you want to play again?")
    if playAgain == false:
        break

if type(minimum) != int or type(maximum) != int :
    print("Oops! That wasn\'t an integer! Run the program again.")

if __name__ == '__main__':
    unittest.main()