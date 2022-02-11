
# https://www.geeksforgeeks.org/print-words-together-set-characters/

from collections import Counter


def solve(words):
    hashmap = dict()

    for i in words:
        a = ''.join(sorted(Counter(i).keys()))

        if a in hashmap.keys():
            hashmap[a].append(i)
        else:
            hashmap[a] = [i]

    for i in hashmap:
        print(hashmap[i])

    return


def main():
    words = ['may', 'student', 'students', 'dog', 'studentssess', 'god', 'cat', 'act', 'tab', 'bat', 'flow', 'wolf',
             'lambs', 'amy', 'yam', 'balms', 'looped', 'poodle']

    solve(words)

    return


main()

# DONE
