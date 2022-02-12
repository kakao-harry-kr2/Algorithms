# 별자리 만들기

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

n = int(input())
coordinates = []

for _ in range(n):
    x, y = map(float, input().split())
    coordinates.append((x, y))

distances = []

for i in range(1, n):
    for j in range(i):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[j]
        dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        distances.append((dist, j, i))

distances.sort()

parent = [i for i in range(n)]
count = 0
result = 0

for dist, i, j in distances:
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        result += dist
        count += 1
    
    if count == n - 1:
        break

print(result)