import sys
input = sys.stdin.readline

# lp와 rp를 잇는 직선: ax + by + c = 0
def get_line(lp, rp):
    a = lp[1] - rp[1]
    b = rp[0] - lp[0]
    c = lp[0] * rp[1] - lp[1] * rp[0]

    return a, b, c

def convex_hull(points, lp, rp):
    if len(points) <= 3:
        return points

    a, b, c = get_line(lp, rp)

    max_dist, max_point = 0, None
    for point in points:
        dist = a * point[0] + b * point[1] + c
        if dist > max_dist:
            max_dist = dist
            max_point = point

    a1, b1, c1 = get_line(lp, max_point)
    a2, b2, c2 = get_line(max_point, rp)

    points1, points2 = [lp], [max_point]

    for point in points:
        if a1 * point[0] + b1 * point[1] + c1 > 0:
            points1.append(point)
        
        if a2 * point[0] + b2 * point[1] + c2 > 0:
            points2.append(point)

    points1.append(max_point)
    points2.append(rp)

    return convex_hull(points1, lp, max_point) + convex_hull(points2, max_point, rp)[1:]

T = int(input())

for _ in range(T):
    n = int(input())
    points = [list(map(int, input().split())) for _ in range(n)]

    points.sort()

    lp, rp = points[0], points[-1]
    a, b, c = get_line(lp, rp)

    upper = [lp, rp]
    lower = [rp, lp]
    for point in points:
        val = a * point[0] + b * point[1] + c
        if val > 0:
            upper.append(point)
        elif val < 0:
            lower.append(point)
    
    border_points = convex_hull(upper, lp, rp)[:-1] + convex_hull(lower, rp, lp)[:-1]

    max_dist, answer = 0, None
    for i in range(len(border_points)-1):
        for j in range(i+1, len(border_points)):
            dist = (border_points[i][0] - border_points[j][0]) ** 2 + (border_points[i][1] - border_points[j][1]) ** 2
            if dist > max_dist:
                max_dist = dist
                answer = border_points[i] + border_points[j]

    print(*answer)