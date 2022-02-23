# 가장 가까운 공통 조상

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    parent = [0] * (N + 1)

    for _ in range(N - 1):
        A, B = map(int, input().split())
        parent[B] = A

    # 가장 가까운 공통 조상을 구할 두 노드
    X, Y = map(int, input().split())

    parent_X = []
    parent_Y = []

    while X:
        parent_X.append(X)
        X = parent[X]
    
    while Y:
        parent_Y.append(Y)
        Y = parent[Y]

    answer = None

    for i, j in zip(reversed(parent_X), reversed(parent_Y)):
        if i == j:
            answer = i
        else:
            break
    
    print(answer)