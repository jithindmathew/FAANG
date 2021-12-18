
# https://www.geeksforgeeks.org/maximum-contiguous-circular-sum/

def kadanes_algo(arr):
    glo_max = curr_max = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], arr[i] + curr_max)
        glo_max = max(glo_max, curr_max)

    return glo_max


def main():
    arr = [2, 3, -9, 5, 6]

    print(max(kadanes_algo(arr), sum(arr) + kadanes_algo(list(map(lambda x:-x , arr)))))


main()

# DONE
