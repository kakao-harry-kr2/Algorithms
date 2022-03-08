# 수열과 쿼리 21

import sys
input = sys.stdin.readline

def init(tree, node, start, end):
    global numList

    # leaf node
    if start == end:
        tree[node][0] = numList[start]
        return tree[node][0]
    
    else:
        mid = (start + end) // 2
        tree[node][0] = init(tree, node*2, start, mid) + init(tree, node*2+1, mid+1, end)
        return tree[node][0]

def propagation(tree, node, start, end):
    # not leaf node
    # lazy 값을 자식 노드에게 전달
    if start != end:
        tree[node*2][1] += tree[node][1]
        tree[node*2+1][1] += tree[node][1]
    
    # 현재 노드에 업데이트
    tree[node][0] += tree[node][1] * (end - start + 1)

    # 현재 노드의 lazy를 제거
    tree[node][1] = 0

    return

def update(tree, node, start, end, left, right, value):
    # 포함되지 않는 경우
    if end < left or right < start:
        return tree[node][0]

    # leaf node
    if start == end:
        if tree[node][1] != 0:
            tree[node][0] += tree[node][1]
            tree[node][1] = 0
        
        tree[node][0] += value
        return tree[node][0]
    
    if tree[node][1] != 0:
        propagation(tree, node, start, end)
    
    if left <= start and end <= right:
        tree[node][0] += (end - start + 1) * value

        if start != end:
            tree[node*2][1] += value
            tree[node*2+1][1] += value
        return tree[node][0]
    
    mid = (start + end) // 2
    update(tree, node*2, start, mid, left, right, value)
    update(tree, node*2+1, mid+1, end, left, right, value)

    tree[node][0] = tree[node*2][0] + tree[node*2+1][0]
    return tree[node][0]

def query(tree, node, start, end, left, right):
    # 포함되지 않는 경우
    if end < left or right < start:
        return 0

    # leaf node
    if start == end:
        if tree[node][1] != 0:
            tree[node][0] += tree[node][1]
            tree[node][1] = 0
        return tree[node][0]
    
    if tree[node][1] != 0:
        propagation(tree, node, start, end)
    
    mid = (start + end) // 2

    a = query(tree, node*2, start, mid, left, right)
    b = query(tree, node*2+1, mid+1, end, left, right)

    tree[node][0] = tree[node*2][0] + tree[node*2+1][0]

    return a + b

N = int(input())
numList = list(map(int, input().split()))
M = int(input())
tree = [[0, 0] for _ in range(300000)]
init(tree, 1, 0, N-1)

for _ in range(M):
    cmd = input().split()

    if cmd[0] == '1':
        update(tree, 1, 0, N-1, int(cmd[1])-1, int(cmd[2])-1, int(cmd[3]))
    
    elif cmd[0] == '2':
        print(query(tree, 1, 0, N-1, int(cmd[1])-1, int(cmd[1])-1))