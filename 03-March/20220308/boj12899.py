# 데이터 구조

import sys
input = sys.stdin.readline
MAX = 2000000

def type1(tree, x):
    node, start, end = 1, 0, MAX - 1

    while start < end:
        tree[node] += 1
        mid = (start + end) // 2
        if x <= mid:
            end = mid
            node = node * 2
        else:
            start = mid + 1
            node = node * 2 + 1
    
    tree[node] += 1

def type2(tree, x):
    node, start, end = 1, 0, MAX - 1

    while start < end:
        tree[node] -= 1
        mid = (start + end) // 2
        if x <= tree[node*2]:
            end = mid
            node = node * 2
        else:
            start = mid + 1
            x -= tree[node*2]
            node = node * 2 + 1
    
    tree[node] -= 1
    return start + 1

N = int(input())
tree = [0] * (2 ** 22)

for _ in range(N):
    T, X = map(int, input().split())
    if T == 1:
        type1(tree, X-1)
    elif T == 2:
        print(type2(tree, X))