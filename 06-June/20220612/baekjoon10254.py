import sys
input = sys.stdin.readline

def get_dist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

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
    
    upper_points = convex_hull(upper, lp, rp)
    lower_points = convex_hull(lower, rp, lp)

    border_points = upper_points[:-1] + lower_points[:-1]

    """ 회전하는 캘리퍼스 """
    left, right = 0, len(upper_points) - 1
    m = len(border_points)

    # 값 초기화
    max_dist = get_dist(lp, rp)
    answer = border_points[left] + border_points[right]
    count = 0

    while count < m:
        # 캘리퍼스를 어느 부분에 맞춰서 돌릴 것인가?
        left_vec = [border_points[(left+1)%m][0] - border_points[left][0], border_points[(left+1)%m][1] - border_points[left][1]]
        right_vec = [border_points[(right+1)%m][0] - border_points[right][0], border_points[(right+1)%m][1] - border_points[right][1]]
        right_vec_inv = [-right_vec[0], -right_vec[1]]

        # left_vec x right_vec_inv 의 값이 양수인 경우: right 기준 / 음수인 경우: left 기준
        if left_vec[0] * right_vec_inv[1] - left_vec[1] * right_vec_inv[0] > 0:
            right = (right + 1) % m

        else:
            left = (left + 1) % m

        count += 1

        new_dist = get_dist(border_points[left], border_points[right])
        if new_dist > max_dist:
            max_dist = new_dist
            answer = border_points[left] + border_points[right]
    
    print(*answer)