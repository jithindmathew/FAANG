
# https://www.geeksforgeeks.org/smallest-window-contains-characters-string/


from collections import Counter


def lenn(s):
    return len(Counter(s))


def solve(string):

    if len(string) <= 1:
        print(string)

        return

    n = lenn(string)

    i = 0
    j = len(string)



    return


def main():

    string = "aabcbcdbca"

    solve(string)

    return


if __name__ == '__main__':
    main()

