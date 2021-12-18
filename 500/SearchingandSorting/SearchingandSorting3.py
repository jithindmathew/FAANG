
# https://www.geeksforgeeks.org/find-a-repeating-and-a-missing-number/

def solve(arr):

    xor = arr[0]
    x = 0
    y = 0

    for i in range(1, len(arr)):
        xor ^= arr[i]
    
    for i in range(1, len(arr) + 1):
        xor ^= i

    set_bit = xor & ~(xor - 1)

    for i in range(len(arr)):
        if arr[i] & set_bit != 0:
            x ^= arr[i]
        else:
            y ^= arr[i]
    
    for i in range(1, len(arr) + 1):
        if i & set_bit != 0:
            x ^= i
        else:
            y ^= i
    
    print("Missing : ", x, "Repeated : ", y)


def main():
    arr = [1, 2, 5, 4, 5, 6, 7, 8, 9]

    solve(arr)
    
    return


main()