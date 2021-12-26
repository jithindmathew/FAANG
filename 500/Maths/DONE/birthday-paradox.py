
# https://www.geeksforgeeks.org/birthday-paradox/

def solve(percent):

    ans = 1
    n = 365

    while n >= 0:

        ans *= (n/365)
        n -= 1

        if 1 - ans >= percent:
            print(365 - n)

            return


def main():

    target = 0.5

    solve(target)

    return

main()

# DONE
