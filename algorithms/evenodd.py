num1=int(input("Enter your number:"))
if(num1%2==0):
    print("{} is even".format(num1))
else:
    print("{} is odd".format(num1))

if (num1>=1):
        for i in range(2, int(num1/2)):
            if (num1 % i) == 0:
                print("{} is not a prime number".format(num1))
                break
        else:
            print("{} is a prime number".format(num1))


