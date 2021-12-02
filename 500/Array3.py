
# https://www.https://www.geeksforgeeks.org/find-subarray-with-given-sum/

def solve(arr, target):

    l = 0
    r = 0
    summ = 0

    while True:

        if summ == target:
            break

        while summ < target:
            summ += arr[r]
            r += 1

            if r == len(arr) and target != summ:
                return None

        while summ > target:
            summ -= arr[l]
            l += 1

            if r == len(arr) and target != summ:
                return None

    return [l, r - 1, "The sub array is : ", arr[l:r]]


def main():

    arr = [1, 4]
    target = 7

    print(solve(arr, target))


main()
