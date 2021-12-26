
# https://www.geeksforgeeks.org/fermats-last-theorem/

def main():
    limit = 15
    n = 2

    for i in range(1, limit + 1, 1):
        for j in range(i, limit + 1):
            if pow(i, n) + pow(j, n) == pow(int(pow(pow(i, n) + pow(j, n), 1/n)), n):
                print("Counter example found")
                return

    return


if __name__ == '__main__':
    main()

# DONE
