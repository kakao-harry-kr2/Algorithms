# 우주신과의 교감

import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

distances = []

for i in range(1, N):
    for j in range(i):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        distances.append((dist, j, i))

distances.sort()

parent = [i for i in range(N)]

# 이미 연결된 통로에 대한 처리
for _ in range(M):
    i, j = map(lambda x: int(x) - 1, input().split())
    union_parent(parent, i, j)

result = 0
for i in range(N):
    find_parent(parent, i)

count = len(set(parent)) - 1

for dist, i, j in distances:
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        result += dist
        count -= 1
    
    if count == 0:
        break

print("%.2f" % result)