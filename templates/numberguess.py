import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, it's yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min(attempts_list)))
def start_game():
    random_number = int(random.randint(1, 10))
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? ")
    play = input("Hi, {}, would you like to play the guessing game? (Enter Yes/No) ".format(player_name))
    attempts = 0
    show_score()
    while play.lower() == "yes":
        try:
            guess = input("Pick a number between 1 and 10 ")
            if int(guess) < 1 or int(guess) > 10:
                raise ValueError("Please guess a number within the given range")
            if int(guess) == random_number:
                print("Nice! You got it!")
                attempts += 0
            elif int(guess) > random_number:
                print("Lower")
                attempts += 1
            elif int(guess) < random_number:
                print("It's Higher")
                attempts += 1
        except ValueError as err:
            print("That is not a valid value. Try again")
    if play.lower() == "no":
        print("That's cool, have a good one!")
    elif play.lower() != "yes" or "no":
        print("That's not a valid response")
        start_game()

if __name__ == '__main__':
    start_game()
