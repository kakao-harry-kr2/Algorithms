# DVDs

import sys
input = sys.stdin.readline

def init(tree, N):
    for i in range(N):
        tree[N + i] = [i, i]
    
    for i in reversed(range(1, N)):
        min1, max1 = tree[i << 1]
        min2, max2 = tree[i << 1 | 1]
        tree[i] = [min(min1, min2), max(max1, max2)]

def query(tree, N, left, right):
    _min, _max = 10 ** 6, -1
    left += N
    right += N
    
    while left < right:
        if left % 2 == 1:
            _min, _max = min(_min, tree[left][0]), max(_max, tree[left][1])
            left += 1
        if right % 2 == 1:
            _min, _max = min(_min, tree[right-1][0]), max(_max, tree[right-1][1])
            right -= 1
        left //= 2
        right //= 2
    
    return _min, _max

def update(tree, N, i, val):
    tree[N + i] = [val, val]
    i += N
    while i > 1:
        tree[i >> 1][0] = min(tree[i][0], tree[i ^ 1][0])
        tree[i >> 1][1] = max(tree[i][1], tree[i ^ 1][1])
        i = i >> 1

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    numList = [i for i in range(N)]
    tree = [[0, 0] for _ in range(2*N)]

    init(tree, N)

    for _ in range(K):
        Q, A, B = map(int, input().split())

        if Q == 0:
            update(tree, N, A, numList[B])
            update(tree, N, B, numList[A])
            numList[A], numList[B] = numList[B], numList[A]
        
        elif Q == 1:
            _min, _max = query(tree, N, A, B + 1)
            if _min == A and _max == B:
                print("YES")
            else:
                print("NO")