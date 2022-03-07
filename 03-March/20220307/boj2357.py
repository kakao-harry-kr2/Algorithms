# 최솟값과 최댓값

import sys
input = sys.stdin.readline

def init(node, start, end):
    global tree, numList
    if start == end:
        num = numList[start]
        tree[node] = [num, num]
        return tree[node]
    
    min1, max1 = init(node*2, start, (start+end)//2)
    min2, max2 = init(node*2+1, (start+end)//2+1, end)

    tree[node] = [min(min1, min2), max(max1, max2)]
    return tree[node]

def search(node, start, end, left, right):
    global tree
    if end < left or right < start:
        return 10**9, 1
    
    if left <= start and end <= right:
        return tree[node]
    
    min1, max1 = search(node*2, start, (start+end)//2, left, right)
    min2, max2 = search(node*2+1, (start+end)//2+1, end, left, right)

    return min(min1, min2), max(max1, max2)

N, M = map(int, input().split())
numList = [int(input()) for _ in range(N)]
tree = [[0, 0] for _ in range(320000)]
init(1, 0, N-1)

for _ in range(M):
    a, b = map(int, input().split())
    _min, _max = search(1, 0, N-1, a-1, b-1)
    print(_min, _max)