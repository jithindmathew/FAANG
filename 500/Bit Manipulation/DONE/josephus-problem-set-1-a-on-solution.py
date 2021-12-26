
# https://www.geeksforgeeks.org/josephus-problem-set-1-a-on-solution/

def solve1(n, k):

    if (n == 1):
        return 1
    else:
        return (solve1(n - 1, k) + k-1) % n + 1


def solve2(n, k):
    ans = 1
    for i in range(1, n):
        ans = (ans + k - 1) % (i+1) + 1

    return ans


def main():
    n = 7
    k = 3

    sol1 = solve1(n, k)
    sol2 = solve2(n, k)

    print(n, format(n, '#010b')[2:])
    print(k, format(k, '#010b')[2:])

    print(sol1, format(sol1, '#010b')[2:])
    print(sol2, format(sol2, '#010b')[2:])

    return


main()

# DONE
