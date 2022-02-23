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

age1 = 21
age2 = 16
if age1 > age2:
    age3 = age2
    age2 = age1
    age1 = age3

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# write a function to output the formatted matrix :
# 1 2 3
# 4 5 6
# 7 8 9

for i in range(len(matrix)):
    for j in range(3):
        print(matrix[i][j], "", end="")
    print()



if __name__ == "__main__":
    print("Age1 =", age1,"Age2 =", age2)


