import random

lowerBound = int(input("Choose the smallest number for your range "))
higherBound = int(input("Choose the largest number for your range "))
computer = random.randint(lowerBound, higherBound)
guessCount = 10

guess = int(input(f"Welcome to the Random Number Guessing Game! Please pick a number between your bounds {lowerBound} and {higherBound}\n"))

while guessCount > 0:
    print("Amount of guesses left: ", guessCount)
    if guess > computer:
        guessCount = guessCount - 1
        guess = int(input("You guessed to high, try to guess something a bit lower.\n "))
    elif guess < computer:
        guessCount = guessCount - 1
        guess = int(input("You guessed to low, try to guess something a bit higher.\n "))
    elif guess == computer:
        guessCount = guessCount - 1
        print("You have won! Good job! \n")
        break
    if guessCount == 0:
        print("Sorry, you lost. Better luck next time.")
    else:
        print("Enter a number instead!")

