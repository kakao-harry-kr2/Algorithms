# 선분 교차 1

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

ccw1 = ccw(point1, point3, point2)
ccw2 = ccw(point3, point2, point4)
ccw3 = ccw(point2, point4, point1)
ccw4 = ccw(point4, point1, point3)

if ccw1 == ccw2 == ccw3 == ccw4:
    print(1)
else:
    print(0)