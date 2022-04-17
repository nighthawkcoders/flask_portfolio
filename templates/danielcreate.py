import random

# define global variables
try_counter = 0     # counts the number of tries to guess number
MIN = 1             # min & max are the parameters
MAX = 100
GUESS = 1           # Current guess
tries = []          # list of tried numbers


# fnc that generates a number between a & b
def gen_random( a,  b):
    randomnumber = int(random.randint(a, b))
    return randomnumber


# main function for the game
def comparisonInput(answer):
    global try_counter, MIN, MAX, GUESS

    #print("playing a game...", tries, try_counter, answer, MIN, MAX)

    # computer sets parameters after each game
    if try_counter == 0:
        MIN = 1
        MAX = 100
        tries.clear()     # clears previous guesses
        try_counter = try_counter + 1
        # return current list when nothing selected
        if answer is None:
            return tries

    # display current list
    if len(tries) > 0:
        print("list content:")
        for i in tries:
            print(i)

    # analyze user inputs
    # if clicked on LESS, adjust max
    if answer == "Less":
        MAX = GUESS - 1

    # if clicked on MORE, adjust min
    if answer == "More":
        MIN = GUESS + 1

    if answer == "Correct":
        GUESS = " .... I win!"
        try_counter = -1
    else:
        if try_counter >= 6:  # max attempts reached
            GUESS = " .... you win!"
            try_counter = -1
        else:
            GUESS = gen_random(MIN,MAX)   # makes new guess

    tries.append(str(GUESS))              # add to prev tries
    try_counter = try_counter + 1

    return tries


if __name__ == "__main__":
    gen_random(1,100)