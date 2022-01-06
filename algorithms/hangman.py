
from blueprints
import random

    word = input()

    letters = []
    for character in word:
        letters.append(character)

    attempts = 8
    outputletters = []
    for x in range(len(letters)):
        outputletters.append(0)
    output = ''

    while attempts > 0:
        print("You have " , attempts , " incorrect guesses left")
        guess = input('Guess a letter:  ')
        if guess in letters:
            while guess in letters:
                index = letters.index(guess)
        outputletters[index] = guess
        letters.remove(guess)
        else:
        attempts -= 1
        print('Incorrect')
        if not(0 in outputletters):
            for a in outputletters:
                output += a
        break

    if attempts == 0:
        print("I am sorry. You have lost ")