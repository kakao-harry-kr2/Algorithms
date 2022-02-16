# 선분 그룹

import sys
input = sys.stdin.readline

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

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())

parent = [i for i in range(N)]
lines = []

for i in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    lines.append((x1, y1, x2, y2))

    # 0 ~ i-1번째 선분들과 교차하는지 확인
    for j in range(i):
        x3, y3, x4, y4 = lines[j]

        ccw132 = ccw([x1, y1], [x3, y3], [x2, y2])
        ccw324 = ccw([x3, y3], [x2, y2], [x4, y4])
        ccw241 = ccw([x2, y2], [x4, y4], [x1, y1])
        ccw413 = ccw([x4, y4], [x1, y1], [x3, y3])

        # 3개의 점이 일직선 상에 존재하면서 교차하는 경우
        if ccw132 == 0 and min(x1, x2) <= x3 <= max(x1, x2) and min(y1, y2) <= y3 <= max(y1, y2):
            cross = True
        elif ccw324 == 0 and min(x3, x4) <= x2 <= max(x3, x4) and min(y3, y4) <= y2 <= max(y3, y4):
            cross = True
        elif ccw241 == 0 and min(x1, x2) <= x4 <= max(x1, x2) and min(y1, y2) <= y4 <= max(y1, y2):
            cross = True
        elif ccw413 == 0 and min(x3, x4) <= x1 <= max(x3, x4) and min(y3, y4) <= y1 <= max(y3, y4):
            cross = True

        # 어떤 3개의 점도 일직선 상에 존재하지 않는 경우 : 선분 교차 1
        elif ccw132 == ccw324 == ccw241 == ccw413 and ccw413 != 0:
            cross = True
        else:
            cross = False
        
        if cross:
            union_parent(parent, i, j)

freq = [0] * N

for i in range(N):
    find_parent(parent, i)
    freq[parent[i]] += 1

print(sum([1 if freq[i] != 0 else 0 for i in range(N)]))
print(max(freq))