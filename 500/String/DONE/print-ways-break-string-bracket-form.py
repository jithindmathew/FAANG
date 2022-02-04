
# https://www.geeksforgeeks.org/print-ways-break-string-bracket-form/

def solve(string, index, output):
    if index == len(string):
        print(output)

        return

    for i in range(index, len(string)):
        solve(string, i+1, output + "(" + string[index:i+1] + ")")

    return


def main():
    string = "qwer"
    solve(string, 0, "")
    return


if __name__ == '__main__':
    main()

# DONE
