first_number = [8, 12, 6, 20, 10]
second_number = [2, 3, 3, 4, 5]
num_problems = len(first_number)

"""
This function prints the problems out based on the type that
is passes as a parameter. It returns the number of correct
answers.
"""
def calculate(type):
    score = 0
    # Loop through all the problems
    for i in range(num_problems):
        # Print first number without going to new line
        print(first_number[i], end = " ")
        if (type == "M"):
            # Print operator without going to new line
            print(" * ", end=" ")
            correct = first_number[i] * second_number[i]
        else:
            # Print operator without going to new line
            print(" / ", end = " ")
            correct = first_number[i] / second_number[i]
        # Print second number and go to new line
        print(second_number[i])
        # Get answer  from user
        answer = int(input("Enter your answer:"))
        if answer == correct:
            # Report and add to score
            print("Correct!")
            score += 1
        else:
            print("Good try!")
        print()
    return score


numinput = input("Give 5 numbers between 1-100")
numbers = []


def number():
    print("What numbers would you like to use?")




if __name__ == "__main__":
    print("Welcome to my Math Quiz!")
    type = input("Please select (M)ultipliction or (D)ivision:")
    # Call function to print problems
    score = calculate(type) * 100 / num_problems

    print("Your score on the test: " + str(score) + "%")
