from flask import app

numbers = [356, 461, 290, 120, 500]
sum = 0
total_num = 0

for i in numbers:
    if i > 0:
        sum = sum + i
        total_num = total_num + 1
    else:
        sum = sum
        print("This is an outlier!")

average = sum/total_num
print(average)

number1 = [356, 461, 290, 20000, 120, -314, 500]
sum1 = 0
total_num1 = 0

for i in number1:
    if i > 0:
        if i > 10000:
            sum1 = sum1
            print(str(i) + " is an outlier!")
        else:
            sum1 = sum1 + i
            total_num1 = total_num1 + 1
    else:
        sum1 = sum1
        print(str(i) + " is an outlier!")

average1 = sum1/total_num1
print(average1)


