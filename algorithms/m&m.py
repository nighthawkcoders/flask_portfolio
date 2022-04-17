import random

goal=int(input("Enter the amount of kilos of M&M's you want "))
x = 5
y = "smallbags"
if(goal<0):
    print("-1")
elif(goal%x==0):
    print("0 smallbags")
elif(goal%x==1):
    print("1 smallbag")
elif(goal%x==2):
    print("2 smallbags")
elif(goal%x==3):
    print("3 smallbags")
elif(goal%x==4):
    print("4 smallbags")
