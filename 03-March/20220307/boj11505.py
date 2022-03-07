# 구간 곱 구하기

import sys
input = sys.stdin.readline
MAX = 1000000007

def init(node, start, end):
    global tree, numList
    # leaf node
    if start == end:
        tree[node] = numList[start]
        return tree[node]
    
    else:
        tree[node] = (init(node*2, start, (start+end)//2) * init(node*2+1, (start+end)//2+1, end)) % MAX
        return tree[node]

def subMul(node, start, end, left, right):
    global tree
    # 포함되지 않는 경우
    if end < left or right < start:
        return 1
    
    # 완전히 포함하는 경우
    if left <= start and end <= right:
        return tree[node]

    # 부분적으로 포함하는 경우
    return (subMul(node*2, start, (start+end)//2, left, right) * subMul(node*2+1, (start+end)//2+1, end, left, right)) % MAX

def update(node, start, end, index, value):
    global tree
    # 포함되지 않는 경우
    if index < start or end < index:
        return

    # leaf node
    if start == end:
        tree[node] = value
        return

    update(node*2, start, (start+end)//2, index, value)
    update(node*2+1, (start+end)//2+1, end, index, value)

    tree[node] = (tree[node*2] * tree[node*2+1]) % MAX

N, M, K = map(int, input().split())
numList = [int(input()) for _ in range(N)]
tree = [0] * 3000000

init(1, 0, N-1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        b = b - 1
        update(1, 0, N-1, b, c)
        numList[b] = c
    
    elif a == 2:
        print(subMul(1, 0, N-1, b-1, c-1))