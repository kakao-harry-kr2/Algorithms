# 선분 교차 3

def ccw(point1, point2, point3):
    tmp = 0
    tmp += point1[0] * point2[1] + point2[0] * point3[1] + point3[0] * point1[1]
    tmp -= point1[1] * point2[0] + point2[1] * point3[0] + point3[1] * point1[0]

    if tmp > 0:
        return 1
    elif tmp < 0:
        return -1
    else:
        return 0

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

point1 = [x1, y1]
point2 = [x2, y2]
point3 = [x3, y3]
point4 = [x4, y4]

ccw132 = ccw(point1, point3, point2)
ccw324 = ccw(point3, point2, point4)
ccw241 = ccw(point2, point4, point1)
ccw413 = ccw(point4, point1, point3)

answer = 0

# 3개의 점이 일직선 상에 존재하면서 교차하는 경우
if ccw132 == 0 and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
    answer = 1
elif ccw324 == 0 and min(x3, x4) <= x2 <= max(x3, x4) and min(y3, y4) <= y2 <= max(y3, y4):
    answer = 1
elif ccw241 == 0 and min(x1, x2) <= x4 <= max(x1, x2) and min(y1, y2) <= y4 <= max(y1, y2):
    answer = 1
elif ccw413 == 0 and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4):
    answer = 1

# 어떤 3개의 점도 일직선 상에 존재하지 않는 경우 : 선분 교차 1
elif ccw132 == ccw324 == ccw241 == ccw413 and ccw413 != 0:
    answer = 1
else:
    pass

print(answer)

if answer:
    if x3 != x4 and y3 != y4:
        a = (x2 - x1) / (x4 - x3)
        b = (x1 - x3) / (x4 - x3)
        c = (y2 - y1) / (y4 - y3)
        d = (y1 - y3) / (y4 - y3)
        
        # 두 선분이 평행한 경우
        if a == c:
            # p1과 p3가 일치하는 경우 : p2와 p4는 반대편에 위치
            if point1 == point3 and min(x2, x4) <= x1 <= max(x2, x4):
                print(*point1)
            if point1 == point4 and min(x2, x3) <= x1 <= max(x2, x3):
                print(*point1)
            if point2 == point3 and min(x1, x4) <= x2 <= max(x1, x4):
                print(*point2)
            if point2 == point4 and min(x1, x3) <= x2 <= max(x1, x3):
                print(*point2)

        else:
            t = (b - d) / (c - a)
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2
            print(x, y)
    
    elif x3 == x4:
        if x1 != x2:
            t = (x3 - x1) / (x2 - x1)
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2
            print(x, y)
        else:
            # 모든 점의 x좌표가 동일한 경우
            # p1과 p3가 일치하면 p2과 p4는 p1(p3)기준 반대편에 있어야 함
            if y1 == y3 and min(y2, y4) <= y1 <= max(y2, y4):
                print(x1, y1)
            if y1 == y4 and min(y2, y3) <= y1 <= max(y2, y3):
                print(x1, y1)
            if y2 == y3 and min(y1, y4) <= y2 <= max(y1, y4):
                print(x2, y2)
            if y2 == y4 and min(y1, y3) <= y2 <= max(y2, y4):
                print(x2, y2)
    
    elif y3 == y4:
        if y1 != y2:
            t = (y3 - y1) / (y2 - y1)
            x = (1 - t) * x1 + t * x2
            y = (1 - t) * y1 + t * y2
            print(x, y)
        else:
            # 모든 점의 y좌표가 동일한 경우
            if x1 == x3 and min(x2, x4) <= x1 <= max(x2, x4):
                print(x1, y1)
            if x1 == x4 and min(x2, x3) <= x1 <= max(x2, x3):
                print(x1, y1)
            if x2 == x3 and min(x1, x4) <= x2 <= max(x1, x4):
                print(x2, y2)
            if x2 == x4 and min(x1, x3) <= x2 <= max(x2, x4):
                print(x2, y2)