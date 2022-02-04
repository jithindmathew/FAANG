
# https://www.geeksforgeeks.org/orientation-3-ordered-points/

def solve(p):
    val = (p[1][1] - p[0][1])*(p[2][0] - p[1][0]) - (p[2][1] - p[1][1])*(p[1][0] - p[0][0])
    
    if val > 0:
        print("clockwise")
    elif val < 0:
        print("counter clockwise")
    else:
        print("collinear")

    return


def main():
    points = [
        [1, 1],
        [2, 3],
        [6, -3]
    ]

    solve(points)

    return


if __name__ == '__main__':
    main()

# DONE
