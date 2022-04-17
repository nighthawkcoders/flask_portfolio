

def matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for i in range(3):
        for j in range(3):
            print(matrix[i][j], end="")
        print()


if __name__ == "__main__":
    matrix()