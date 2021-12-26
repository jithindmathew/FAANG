
# https://www.geeksforgeeks.org/euclidean-algorithms-basic-and-extended/

def solve(x, y):
    if x == 0:
        return y

    return solve(y % x, x)


def main():
    x = 22685788
    y = 5646745676

    print(solve(x, y))

    return


main()

# DONE
