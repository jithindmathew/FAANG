
# https://www.geeksforgeeks.org/zigzag-or-diagonal-traversal-of-matrix/

def printt(matrix, x, y):

    while x > -1:
        print(matrix[x][y], end="")
        x -= 1
        y += 1

        if y > len(matrix[0]) - 1:
            break

    print(end='\n')
    return


def solve(matrix):
    row = len(matrix)
    col = len(matrix[0])

    for i in range(row):
        printt(matrix, i, 0)

    for i in range(1, col, 1):
        printt(matrix, row - 1, i)

    return


def main():
    matrix = [
        [3, 4, 8, 2, 5, 6],
        [2, 9, 0, 2, 5, 6],
        [0, 9, 7, 2, 5, 6],
        [3, 3, 0, 2, 5, 6]
    ]

    solve(matrix)

    return


main()

# DONE
