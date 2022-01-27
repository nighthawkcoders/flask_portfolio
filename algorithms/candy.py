import random

goal=int(input("Enter the amount of kilos you want to use"))
smallpack = 0
if(goal<0):
    print ("-1")
elif(goal%5==4):
    print ("4 small packs")
elif(goal%5==3):
    print ("3 small packs")
elif(goal%5==2):
    print ("2 small packs")
elif(goal%5==1):
    print ("1 small pack")
elif(goal%5==0):
    print ("No small packs")



