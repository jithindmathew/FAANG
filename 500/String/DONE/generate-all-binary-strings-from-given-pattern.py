
# https://www.geeksforgeeks.org/generate-all-binary-strings-from-given-pattern/


def solve(string):
    if '?' in string:
        s1 = string.replace('?', '0', 1)
        s2 = string.replace('?', '1', 1)

        solve(s1)
        solve(s2)

    else:
        result.append(string)
        # print(string)

    return


def main():
    string = "1??0?101"

    solve(string)

    print(result)

    return


result = []


main()

# DONE
