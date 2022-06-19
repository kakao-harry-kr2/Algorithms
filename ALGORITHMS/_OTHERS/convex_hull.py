import sys
input = sys.stdin.readline

# lp와 rp를 잇는 직선: ax + by + c = 0
def get_line(lp, rp):
    a = lp[1] - rp[1]
    b = rp[0] - lp[0]
    c = lp[0] * rp[1] - lp[1] * rp[0]

    return a, b, c

def convex_hull_impl(points, lp, rp):
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

    return convex_hull_impl(points1, lp, max_point) + convex_hull_impl(points2, max_point, rp)[1:]

def convex_hull(points:list):
    if len(points) < 3:
        return points
    
    points.sort()

    lp, rp = points[0], points[-1]
    a, b, c = get_line(lp, rp)

    upper = [lp]
    lower = [rp]
    for point in points:
        val = a * point[0] + b * point[1] + c
        if val > 0:
            upper.append(point)
        elif val < 0:
            lower.append(point)
    upper.append(rp)
    lower.append(lp)

    upper_points = convex_hull_impl(upper, lp, rp)
    lower_points = convex_hull_impl(lower, rp, lp)

    return upper_points[:-1] + lower_points[:-1]

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

print(convex_hull(points))