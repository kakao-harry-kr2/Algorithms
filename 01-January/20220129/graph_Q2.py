# Minimum Spanning Tree
from collections import deque
import sys
input = sys.stdin.readline

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

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
edges = []
result = 0

count = 0
index = 0

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))

edges.sort()

while count < N - 2: # 길이 N - 2개면 두 개의 분리된 마을 형성
    cost, A, B = edges[index]
    if find_parent(parent, A) != find_parent(parent, B):
        union_parent(parent, A, B)
        result += cost
        count += 1

    index += 1

print(result)