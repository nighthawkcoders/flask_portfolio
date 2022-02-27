from flask import app



matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()

def swap1(a, b):
    if a > b:
        b, a = a, b
    return a, b

def swap1_helper(a, b):
    print("python swap")
    print("original: ", a, b)
    a, b = swap1(a, b)
    print("after: ", a, b)
    print()



if __name__ == "__main__":
    print()
    print(swap1_helper(12, 10))
    print(swap1_helper(51, 23))
def func(age1,age2):
    if age1 > age2:
        age3 = age2
        age2 = age1
        age1 = age3
        print(age1, age2)
    else:
        print(age1, age2)


def func2():
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
    age1 = int(input("Give a number"))
    age2 = int(input("Give a second number"))
    func2()
    func(age1, age2)


