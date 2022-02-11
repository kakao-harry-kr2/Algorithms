# 여행 가자

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N = int(input())
M = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(lambda x: int(x) - 1, input().split()))
parent = [i for i in range(N)]

for i in range(N):
    for j in range(N):
        # i 도시와 j 도시에 도로가 있으면 union 연산
        if i < j and graph[i][j] == 1:
            union_parent(parent, i, j)

# 여행 가능 여부
available = True
group = find_parent(parent, plans[0])

for plan in plans[1:]:
    par = find_parent(parent, plan)
    if par != group:
        available = False
        break

print("YES" if available else "NO")