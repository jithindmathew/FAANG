from math import isqrt

# https://www.geeksforgeeks.org/sieve-eratosthenes-0n-time-complexity/


def solve(n):
    isprime = [True]*n
    isprime[0] = isprime[1] = False

    for i in range(2, isqrt(n)):
        if not isprime[i]:
            continue

        for j in range(i*i, n, i):
            isprime[j] = False

    for i in range(n):
        if not isprime[i]:
            continue
        print(i)

    return


def main():
    n = 3009

    solve(n)

    return


main()

# DONE
