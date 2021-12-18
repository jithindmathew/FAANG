
# https://www.geeksforgeeks.org/majority-element/#

def solve(arr):
    n = len(arr)
    hashmap = {}

    for i in arr:
        if i in hashmap:
            hashmap[i] += 1
        else:
            hashmap[i] = 1

    ans = max(hashmap, key=hashmap.get)

    if hashmap[ans] > n/2:
        print(ans)
    else:
        print("No majority element")

    return


def main():

    arr = [1, 2, 3, 4, 5, 6, 7]

    solve(arr)


main()

# DONE
