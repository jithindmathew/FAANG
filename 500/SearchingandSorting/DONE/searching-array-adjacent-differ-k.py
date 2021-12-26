
# https://www.geeksforgeeks.org/searching-array-adjacent-differ-k/

def solve(arr, target, gap):
    i = 0

    while i < len(arr):
        if arr[i] == target:
            print(i)
            return
        
        i += max(1, int(abs(arr[i] - target)/gap))
    
    print("The number is not present")
    return



def main():
    arr = [20, 40, 50, 70, 70, 60]
    target = 60
    gap = 20

    solve(arr, target, gap)

    return


main()

# DONE
