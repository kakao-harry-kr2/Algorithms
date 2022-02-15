# 선분 교차2

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

# 3개의 점이 일직선 상에 존재하면서 교차하는 경우
if ccw132 == 0 and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
    print(1)
elif ccw324 == 0 and min(x3, x4) <= x2 <= max(x3, x4) and min(y3, y4) <= y2 <= max(y3, y4):
    print(1)
elif ccw241 == 0 and min(x1, x2) <= x4 <= max(x1, x2) and min(y1, y2) <= y4 <= max(y1, y2):
    print(1)
elif ccw413 == 0 and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4):
    print(1)

# 어떤 3개의 점도 일직선 상에 존재하지 않는 경우 : 선분 교차 1
elif ccw132 == ccw324 == ccw241 == ccw413 and ccw413 != 0:
    print(1)
else:
    print(0)