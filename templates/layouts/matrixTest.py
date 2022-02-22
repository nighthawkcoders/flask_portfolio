matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(matrix)):
    for f in range (3):
        print(matrix[i][f], end="")

def swap1(b, a):
    if a > b:
        b, a = a, b
    return a, b

def swap1_maker(b, a):
    print("python swap")
    print("original: ", a, b)
    a, b = swap1(a, b)
    print("after: ", a, b)
    print()

if __name__ == "__main__":
    print()
    print(swap1_maker(100,55))
    print(swap1_maker(88,31))