# CCW

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 첫번째 점과 두번째 점을 잇는 직선의 기울기
# 무한대일때
if x1 == x2:
    if y1 < y2:
        if x3 < x1:
            print(1)
        elif x3 == x1:
            print(0)
        else:
            print(-1)
    else:
        if x3 < x1:
            print(-1)
        elif x3 == x1:
            print(0)
        else:
            print(1)
    exit()

# 기울기가 0일때
if y1 == y2:
    if x1 < x2:
        if y3 < y1:
            print(-1)
        elif y3 == y1:
            print(0)
        else:
            print(1)
    else:
        if y3 < y1:
            print(1)
        elif y3 == y1:
            print(0)
        else:
            print(-1)
    exit()

value = (y2 - y1) * x3 + (x1 - x2) * y3 - x1 * y2 + x2 * y1

if x1 < x2:
    if value < 0:
        print(1)
    elif value == 0:
        print(0)
    else:
        print(-1)

else:
    if value > 0:
        print(-1)
    elif value == 0:
        print(0)
    else:
        print(1)