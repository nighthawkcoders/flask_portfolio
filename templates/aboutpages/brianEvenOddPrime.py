import random

def NumberCheck(num):
    if (num % 2) == 0:
        print(num, "is even")
        return
    else:
        print(num, "is odd")
        return

def PrimeCheck(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                return
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

if __name__ == "__main__":
    num = random.randint(1,100)
    NumberCheck(num)
    PrimeCheck(num)