
# https://www.geeksforgeeks.org/swap-two-nibbles-byte/

def solve(n):
    print(format(15, '#010b')[2:], 'binary for 15')
    print(format(240, '#010b')[2:], 'binary for 240')

    print(format(((n & 15) << 4 | (n & 240) >> 4), '#010b')[2:])

    return


def main():
    n = 100

    print(format(n, '#010b')[2:])

    solve(n)

    return


main()

# DONE
