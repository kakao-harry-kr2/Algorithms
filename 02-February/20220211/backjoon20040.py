# 사이클 게임

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 사이클이 생성된 경우
    if a == b:
        return 0

    elif a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    return 1

n, m = map(int, input().split())
parent = [i for i in range(n)]
answer = 0

for i in range(1, m + 1):
    a, b = map(int, input().split())
    result = union_parent(parent, a, b)

    if result == 0 and answer == 0:
        answer = i

print(answer)