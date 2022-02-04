
# https://www.geeksforgeeks.org/check-if-two-given-strings-are-isomorphic-to-each-other/

def solve(s1, s2):

    if len(s1) == len(s2):
        s1_arr = [0]*26
        s2_arr = [0]*26

        for i in range(len(s2)):
            s1_arr[ord(s1[i]) - 97] += 1
            s2_arr[ord(s2[i]) - 97] += 1

            if s1_arr[ord(s1[i]) - 97] != s2_arr[ord(s2[i]) - 97]:
                return False

        return True

    return False


def main():
    s1 = "abc"
    s2 = "xyy"

    print(solve(s1, s2))

    return


if __name__ == '__main__':
    main()

# DONE
