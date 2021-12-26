
# https://www.geeksforgeeks.org/a-boolean-matrix-question/

def solve(matrix):
    row = len(matrix)
    col = len(matrix[0])

    row_bool = [False]*row
    col_bool = [False]*col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 1:
                row_bool[i] = True
                col_bool[j] = True

    for i in range(row):
        for j in range(col):
            if row_bool[i] or col_bool[j]:
                matrix[i][j] = 1

    print(matrix)

    return


def main():
    matrix = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]

    solve(matrix)

    return


main()

# DONE
