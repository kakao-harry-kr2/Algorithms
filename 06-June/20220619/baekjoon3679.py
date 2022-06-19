from functools import cmp_to_key
import sys
input = sys.stdin.readline

def my_cmp(p1, p2):
    if p1[4] * p2[3] < p1[3] * p2[4]:
        return -1
    elif p1[4] * p2[3] > p1[3] * p2[4]:
        return 1
    else:
        if p1[3] ** 2 + p1[4] ** 2 < p2[3] ** 2 + p2[4] ** 2:
            return -1
        else:
            return 1

c = int(input())

for _ in range(c):
    inputs = list(map(int, input().split()))

    points = []
    for i in range(1, len(inputs)-1, 2):
        points.append([inputs[i], inputs[i+1], i//2])

    points.sort()

    l_point, *points = points
    for i in range(len(points)):
        points[i].append(points[i][0] - l_point[0])
        points[i].append(points[i][1] - l_point[1])
    
    points.sort(key=cmp_to_key(my_cmp))

    last_index = len(points) - 1
    while True:
        if points[last_index][4] * points[last_index-1][3] != points[last_index][3] * points[last_index-1][4]:
            break
        
        last_index -= 1

    answer = [l_point[2]] + [i for _, _, i, _, _ in points[:last_index]+points[last_index:][::-1]]
    print(*answer)