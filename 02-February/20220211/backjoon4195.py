# 친구 네트워크

import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, count, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)

    # 두 사람이 이미 친구 관계인 경우
    if x == y:
        print(count[x])

    # 두 사람이 친구 관게가 아닌 경우
    elif x < y:
        parent[y] = x
        count[x], count[y] = count[x] + count[y], 0
        print(count[x])
    else:
        parent[x] = y
        count[x], count[y] = 0, count[x] + count[y]
        print(count[y])

T = int(input())

for _ in range(T):
    F = int(input())
    name2num = dict()
    parent = [i for i in range(200200)]
    count = [1 for _ in range(200200)]
    total = 0

    for _ in range(F):
        p1, p2 = input().split()
        for p in [p1, p2]:
            if p not in name2num.keys():
                name2num[p] = total
                total += 1
        
        n1, n2 = name2num[p1], name2num[p2]
        union_parent(parent, count, n1, n2)