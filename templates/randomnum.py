import random


def randomnum():
    randomnumber = int(random.randint(1, 100))
    i = 0
    print(randomnumber)
    if randomnumber % 2 == 0:
        print("The number is even")
    elif randomnumber % 2 != 0:
        print("The number is odd")
        if randomnumber > 1:
            for i in range(2, int(randomnumber/2) + 1):
                if (randomnumber % i) == 0:
                    print("Is not Prime")
                    break
            else:
                print("Is Prime")
        else:
            print("Is not Prime")


if __name__ == "__main__":
    randomnum()