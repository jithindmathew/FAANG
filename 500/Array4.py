
# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

def solve(arr):

    summ = sum(arr)
    left = 0

    for i in range(len(arr)):
        summ -= arr[i]

        if left == summ:
            return i

        left += arr[i]

    return -1


def main():
    arr = [-7, 1, 5, 2, -4, 3, 0]

    print(solve(arr))


main()
