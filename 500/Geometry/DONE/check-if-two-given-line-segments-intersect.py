
# https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/

def solve2(p):
    val = (p[1][1] - p[0][1]) * (p[2][0] - p[1][0]) - (p[2][1] - p[1][1]) * (p[1][0] - p[0][0])

    if val > 0:
        return "clockwise"
    elif val < 0:
        return "counter clockwise"
    else:
        return "collinear"


def solve(points):

    a1 = solve2([points[0], points[1], points[2]])
    a2 = solve2([points[0], points[1], points[3]])
    a3 = solve2([points[2], points[3], points[0]])
    a4 = solve2([points[2], points[3], points[1]])

    if a1 != a2 and a3 != a4:
        print("intersects")
        return

    else:
        if [a1, a2, a3, a4] == ["collinear"]*4:
            if not (max(points[0][0], points[1][0]) < max(points[2][0], points[3][0]) and max(points[0][1], points[1][1]) < max(points[2][1], points[3][1])):
                print("intersects")
                return

    print("does not intersect")

    return


def main():

    """
    (p1) o-------------------o (q1)


    (p2) o--------------o (q2)

    """

    points = [
        [-5, -5],   # p1
        [0, 0],   # q1
        [1, 1],   # p2
        [10, 10]    # q2
    ]

    solve(points)

    return


if __name__ == '__main__':
    main()

# DONE
