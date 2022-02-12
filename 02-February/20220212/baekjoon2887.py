# 행성 터널

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

N = int(input())
parent = [i for i in range(N)]
x_coordinates = []
y_coordinates = []
z_coordinates = []

for i in range(N):
    x, y, z = map(int, input().split())
    x_coordinates.append((x, i))
    y_coordinates.append((y, i))
    z_coordinates.append((z, i))

x_coordinates.sort()
y_coordinates.sort()
z_coordinates.sort()

dist = []
dist += [(x_coordinates[i+1][0] - x_coordinates[i][0], x_coordinates[i][1], x_coordinates[i+1][1]) for i in range(N-1)]
dist += [(y_coordinates[i+1][0] - y_coordinates[i][0], y_coordinates[i][1], y_coordinates[i+1][1]) for i in range(N-1)]
dist += [(z_coordinates[i+1][0] - z_coordinates[i][0], z_coordinates[i][1], z_coordinates[i+1][1]) for i in range(N-1)]

dist.sort()

result = 0
count = 0

for d, i, j in dist:
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        result += d
        count += 1
    
    if count == N - 1:
        break

print(result)