import sys
input = sys.stdin.readline

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

# 두개의 convex_hull이 서로 만나는지 체크
def check_intersection(convex_black, convex_white):
    for i in range(len(convex_black)):
        for j in range(len(convex_white)):
            (x1, y1), (x2, y2) = convex_black[i-1], convex_black[i]
            (x3, y3), (x4, y4) = convex_white[j-1], convex_white[j]

            # 두 선분의 기울기가 같은 경우
            if (x2 - x1) * (y4 - y3) == (x4 - x3) * (y2 - y1):
                # 두 선분이 같은 직선 위에 존재하는 경우
                if (x2 - x1) * (y3 - y1) == (x3 - x1) * (y2 - y1):
                    if max(x1, x2) < min(x3, x4):
                        continue
                    elif max(x3, x4) < min(x1, x2):
                        continue
                    else:
                        return True

                # 두 선분이 다른 직선 위에 존재하는 경우
                else:
                    continue
            
            # 두 선분의 기울기가 다른 경우
            t = (x4 - x3) * (y3 - y1) - (x3 - x1) * (y4 - y3)
            s = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
            v = (x4 - x3) * (y2 - y1) - (x2 - x1) * (y4 - y3)

            # 두 선분이 교차하는 경우 
            if 0 <= t <= v and 0 <= s <= v:
                return True
    
    return False

# convex1이 convex2를 내부에 포함하는지 체크
def contain_another(convex1, convex2):
    x0, y0 = convex2[0]
    for i in range(len(convex1)):
        (x1, y1), (x2, y2) = convex1[i-1], convex1[i]
        if (x2 - x1) * (y0 - y1) - (x0 - x1) * (y2 - y1) > 0:
            return False
    
    return True

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())

    black = sorted([list(map(int, input().split())) for _ in range(n)])
    white = sorted([list(map(int, input().split())) for _ in range(m)])

    blp, brp = black[0], black[-1]
    wlp, wrp = white[0], white[-1]

    ba, bb, bc = get_line(blp, brp)
    wa, wb, wc = get_line(wlp, wrp)

    b_upper, b_lower = [blp], [brp]
    w_upper, w_lower = [wlp], [wrp]

    for black_p in black:
        val = ba * black_p[0] + bb * black_p[1] + bc
        if val > 0:
            b_upper.append(black_p)
        elif val < 0:
            b_lower.append(black_p)
    
    for white_p in white:
        val = wa * white_p[0] + wb * white_p[1] + wc
        if val > 0:
            w_upper.append(white_p)
        elif val < 0:
            w_lower.append(white_p)

    b_upper.append(brp)
    b_lower.append(blp)
    w_upper.append(wrp)
    w_lower.append(wlp)

    convex_black = convex_hull(b_upper, blp, brp)[:-1] + convex_hull(b_lower, brp, blp)[:-1]
    convex_white = convex_hull(w_upper, wlp, wrp)[:-1] + convex_hull(w_lower, wrp, wlp)[:-1]

    if len(black) == 1:
        convex_black = black
    if len(white) == 1:
        convex_white = white

    if len(convex_black) == 1 and len(convex_white) == 1:
        print("YES")
        continue
    
    if len(convex_black) == 1:
        if contain_another(convex_white, convex_black):
            print("NO")
        else:
            print("YES")
        
        continue
    
    if len(convex_white) == 1:
        if contain_another(convex_black, convex_white):
            print("NO")
        else:
            print("YES")
        
        continue

    # 두 convex_hull이 서로 만나면 분리 불가능
    if check_intersection(convex_black, convex_white):
        print("NO")
        continue

    # convex_hull 내부에 다른 convex_hull이 존재하면 분리 불가능
    if len(convex_black) >= 3 and contain_another(convex_black, convex_white):
        print("NO")
        continue

    if len(convex_white) >= 3 and contain_another(convex_white, convex_black):
        print("NO")
        continue
    
    print("YES")