# Egg

import sys
input = sys.stdin.readline
MAX = 10 ** 5

T = int(input())

def propagation(tree, node, start, end):
    if start != end:
        tree[node*2][1] += tree[node][1]
        tree[node*2+1][1] += tree[node][1]
    
    tree[node][0] += tree[node][1] * (end - start + 1)

    tree[node][1] = 0
    return

# tree에 [left, right] 범위 +val
def update(tree, node, start, end, left, right, val):
    # 포함되지 않는 경우
    if end < left or right < start:
        return
    
    if left <= start and end <= right:
        tree[node][1] +=  val
        return
    
    mid = (start + end) // 2
    update(tree, node*2, start, mid, left, right, val)
    update(tree, node*2+1, mid+1, end, left, right, val)

    return

# tree에서 k의 개수
def find(tree, k):
    node, start, end = 1, 0, MAX

    while start < end:
        if tree[node][1] != 0:
            propagation(tree, node, start, end)
        mid = (start + end) // 2
        if k <= mid:
            node = node * 2 
            end = mid
        else:
            node = node * 2 + 1
            start = mid + 1
    
    tree[node][0] += tree[node][1]
    tree[node][1] = 0

    return tree[node][0]

for _ in range(T):
    n, m = map(int, input().split())

    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append([x, y])

    points.sort()

    lines = []
    for _ in range(m):
        l, r, b, t = map(int, input().split())
        lines.append([l, b, t, 1])
        lines.append([r, b, t, -1])
    
    lines.sort(key=lambda x: (x[0], -x[3]))

    tree = [[0, 0] for _ in range(2 ** 18)]

    index = 0

    answer = 0
    for x, y in points:
        while index < 2 * m and (lines[index][0] < x or (lines[index][0] == x and lines[index][3] == 1)):
            update(tree, 1, 0, MAX, lines[index][1], lines[index][2], lines[index][3])
            index += 1
        
        answer += find(tree, y)

    print(answer)