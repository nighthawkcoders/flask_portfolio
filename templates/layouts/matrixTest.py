# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)):
#     for f in range (3):
#         print(matrix[i][f], end="")

def swap(b, a):
    return a, b

def swap_pair(b, a):
    print("before swap: ", a, b)
    a, b = swap(a, b)
    print("after  swap: ", a, b)
    print("-------------------")

if __name__ == "__main__":
    swap_pair(100,55)
    swap_pair(88,31)
    swap_pair(15,73)