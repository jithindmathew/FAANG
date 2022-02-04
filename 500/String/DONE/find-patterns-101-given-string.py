
# https://www.geeksforgeeks.org/find-patterns-101-given-string/

def solve(string):

    ans = 0

    string_l = len(string)

    for i in range(string_l - 2):
        if string[i] == "1":

            if (string_l - i) % 2 == 0:
                j_high = (string_l - i) // 2
            else:
                j_high = (string_l - i) // 2 + 1

            for j in range(1, j_high):
                if string[i + j] == "0" and string[i + 2*j] == "1":
                    ans += 1

    print(ans)

    return


def main():

    string = "1001ab010abc01001"

    solve(string)

    return


if __name__ == '__main__':
    main()

# DONE
