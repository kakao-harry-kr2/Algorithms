# 북서풍

import sys
input = sys.stdin.readline

# segment tree에 k 값을 추가
def add(tree, node, start, end, value):
    if value < start or end < value:
        return
    
    tree[node] += 1

    if start == end:
        return

    mid = (start + end) // 2
    add(tree, node*2, start, mid, value)
    add(tree, node*2+1, mid+1, end, value)

# segment tree에서 k이상 값의 개수
def find(tree, node, start, end, k):
    count = 0
    while start < end:
        mid = (start + end) // 2

        if k > mid:
            node = node * 2 + 1
            start = mid + 1
        
        else:
            count += tree[node*2+1]
            node = node * 2
            end = mid
    
    return count + tree[node]

T = int(input())

for _ in range(T):
    n = int(input())
    islands = []
    for _ in range(n):
        x, y = map(int, input().split())
        islands.append([x, y])

    islands.sort(key=lambda x: x[1])

    # y좌표의 값을 0 ~ n-1로
    y_value = 0
    y_list = [0]
    for i in range(1, n):
        if islands[i][1] != islands[i-1][1]:
            y_value += 1
        y_list.append(y_value)

    for i in range(n):
        islands[i][1] = y_list[i]

    islands.sort(key=lambda x : (x[0], -x[1]))

    # segment tree
    tree = [0] * (2 ** 18)

    answer = 0

    for island in islands:
        answer += find(tree, 1, 0, n-1, island[1])
        add(tree, 1, 0, n-1, island[1])

    print(answer)