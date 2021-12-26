
# https://www.geeksforgeeks.org/equilibrium-index-of-an-array/

def solve(arr):

    summ = sum(arr)
    left = 0

    for i in range(len(arr)):
        summ -= arr[i]

        if left == summ:
            return ["Index", i, "Element", arr[i]]

        left += arr[i]

    return -1


def main():
    arr = [-2, -4, 5, 9, 0, -1, 10, 4, -5]

    print(solve(arr))


main()

# DONE
