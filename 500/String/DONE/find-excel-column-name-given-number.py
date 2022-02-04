
# https://www.geeksforgeeks.org/find-excel-column-name-given-number/

def solve(n):

    if n == 0:
        return "INVALID"

    ans = ""

    while n:
        rem = n % 26

        if rem == 0:
            ans = 'Z' + ans
            n -= 1
        else:
            ans = chr(64 + rem) + ans

        n //= 26

    return ans


def main():

    a = [26, 51, 52, 80, 676, 702, 705]

    for i in a:
        print(solve(i))

    return


if __name__ == '__main__':
    main()

# DONE
