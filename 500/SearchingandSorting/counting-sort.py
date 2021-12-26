
# https://www.geeksforgeeks.org/counting-sort/

def solve(arr):
    min_element = min(arr)
    max_element = max(arr)

    num_range = max_element - min_element + 1

    ans = [0]*len(arr)
    count_arr = [0]*num_range

    for i in arr:
        count_arr[i - min_element] += 1

    i = 0
    count = 0

    while i < num_range:
        temp = i
        j = 0

        while j < count_arr[i]:
            ans[count] = temp + min_element
            count += 1
            j += 1

        i += 1

    print(ans)

    return


def main():
    input = [-1, 4, -2, 2, -7, 50, 2]

    solve(input)

    return


main()

# DONE
