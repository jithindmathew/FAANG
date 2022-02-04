
# https://www.geeksforgeeks.org/program-nth-catalan-number/

def solve(n):  # TC : O(n^2)

    arr = [0]*(n+1)

    arr[0] = 1
    arr[1] = 1

    for i in range(2, n+1):
        for j in range(i):
            arr[i] += arr[j]*arr[i-j-1]

    return arr[n]


def solve2(n):

    if n > 1:
        ans = 1
        ans2 = 1

        for i in range(2, n+1):
            ans *= (i + n)

        for i in range(2, n+1):
            ans2 *= i

        return ans//ans2

    return 1


def main():
    n = 30

    print(solve2(n))

    return


if __name__ == '__main__':
    main()

# DONE
