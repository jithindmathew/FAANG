
# https://www.geeksforgeeks.org/overlapping-subproblems-property-in-dynamic-programming-dp-1/

def fibo1(n1, lookup1):
    if n1 <= 1:
        lookup1[n1] = n1

    if lookup1[n1] is None:
        lookup1[n1] = fibo1(n1 - 1, lookup1) + fibo1(n1 - 2, lookup1)
    
    return lookup1[n1]


def solve1(n1):
    lookup1 = [None]*(n1 + 5)

    print(fibo1(n1, lookup1))

    return


def solve2(n2):
    lookup2 = [0]*(n2 + 2)

    lookup2[1] = 1

    for i in range(2, n2 + 2):
        lookup2[i] = lookup2[i - 1] + lookup2[i - 2]

    print(lookup2[n2])

    return


def main():
    n1 = 16
    n2 = 16

    solve1(n1)
    solve2(n2)

    return


main()

# DONE
