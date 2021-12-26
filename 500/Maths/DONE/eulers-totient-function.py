
# https://www.geeksforgeeks.org/eulers-totient-function/

def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def solve(num):
    if num == 1 or num == 2:
        return 1

    result = 1

    for i in range(2, num, 1):
        if gcd(i, num) == 1:
            result += 1

    return result


def main():
    n = 30

    for i in range(1, n+1, 1):
        print(i, solve(i))

    return


if __name__ == "__main__":
    main()

# DONE
