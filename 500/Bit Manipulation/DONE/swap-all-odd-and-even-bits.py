
# https://www.geeksforgeeks.org/swap-all-odd-and-even-bits/

def solve(n):
    print(format(((n & 1431655765) << 1 | (n & 2863311530) >> 1), '#010b')[2:])

    return


def main():
    n = 100

    print(format(n, '#010b')[2:])

    print(int('01010101010101010101010101010101', 2))
    print(int('10101010101010101010101010101010', 2))

    solve(n)


main()

# DONE
