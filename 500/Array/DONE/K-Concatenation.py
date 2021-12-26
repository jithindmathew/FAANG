
# https://www.codechef.com/JAN18/problems/KCON/

def kadanes_algo(arr):

    dparr = [0]*len(arr)

    ans = dparr[0] = arr[0]

    for i in range(1, len(arr)):
        dparr[i] = max(arr[i], arr[i] + dparr[i - 1])
        ans = max(ans, dparr[i])

    return ans


def solve(arr, k):

    if k == 1:
        print(kadanes_algo(arr))

    else:
        summ = sum(arr)
        newarr = arr*2
        print(max(kadanes_algo(newarr), kadanes_algo(newarr) + summ*(k - 2)))


def main():
    t = int(input())

    for i in range(t):
        n, k = map(int, input().split(" "))

        arr = list(map(int, input().split(" ")))

        solve(arr, k)


main()

# DONE
