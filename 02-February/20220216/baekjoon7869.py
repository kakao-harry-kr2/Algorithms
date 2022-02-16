# 두 원

import math

def getArea(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area

x1, y1, r1, x2, y2, r2 = map(float, input().split())

# 첫번째 원의 반지름이 두번째 원보다 크게
if r1 < r2:
    x1, y1, r1, x2, y2, r2 = x2, y2, r2, x1, y1, r1

dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

if dist >= r1 + r2:
    print("%.3f" % 0)

elif dist <= r1 - r2:
    print("%.3f" % (math.pi * (r2 ** 2)))

# 둔각삼각형을 이루는 경우
elif r1 ** 2 > r2 ** 2 + dist ** 2:
    area = getArea(r1, r2, dist)
    h = (2 * area) / dist
    theta1 = math.asin(h / r1) * 2
    area1 = 0.5 * (r1 ** 2) * (theta1 - math.sin(theta1))
    theta2 = 2 * math.pi - 2 * math.asin(h / r2)
    area2 = 0.5 * (r2 ** 2) * (theta2 - math.sin(theta2))
    print("%.3f" % (area1 + area2))

# 예각삼각형을 이루는 경우
else:
    area = getArea(r1, r2, dist)
    h = 2 * area / dist
    theta1 = math.asin(h / r1) * 2
    area1 = 0.5 * (r1 ** 2) * (theta1 - math.sin(theta1))
    theta2 = 2 * math.asin(h / r2)
    area2 = 0.5 * (r2 ** 2) * (theta2 - math.sin(theta2))
    print("%.3f" % (area1 + area2))