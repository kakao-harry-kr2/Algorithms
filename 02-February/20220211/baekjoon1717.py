# 집합의 표현

import sys
sys.setrecursionlimit(10 ** 9)
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

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    opr, a, b = map(int, input().split())
    if opr == 0:
        union_parent(parent, a, b)

    elif opr == 1:
        a = find_parent(parent, a)
        b = find_parent(parent, b)

        print("YES" if a == b else "NO")