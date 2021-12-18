
# https://www.geeksforgeeks.org/maximum-sum-increasing-subsequence-dp-14/

global maximum

def lis2(arr, n):
    global maximum

    if n == 1:
        return 1

    max_ending_here = 1

    for i in range(1, n):
        re


def lis1(arr):
    global maximum

    n = len(arr)
    maximum = 1

    lis2(arr, n)

    print(maximum)

    return





def solve(arr):
    pass


def main():

    arr = [10, 22, 9, 33, 21, 50, 41, 60]

    solve(arr)
    pass


main()
