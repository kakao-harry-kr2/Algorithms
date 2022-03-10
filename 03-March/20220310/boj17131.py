# 여우가 정보섬에 올라온 이유

import sys
input = sys.stdin.readline
MAX = 10 ** 9 + 7

def add(tree, node, start, end, value):
    if end < value or value < start:
        return
    
    tree[node] += 1

    if start != end:
        mid = (start + end) // 2
        add(tree, node*2, start, mid, value)
        add(tree, node*2+1, mid+1, end, value)

def remove(tree, node, start, end, value):
    if end < value or value < start:
        return

    tree[node] -= 1

    if start != end:
        mid = (start + end) // 2
        remove(tree, node*2, start, mid, value)
        remove(tree, node*2+1, mid+1, end, value)

# tree에서 value보다 큰 값의 개수
def find(tree, value):
    global N
    count = 0
    node, start, end = 1, 0, N-1
    while start < end:
        mid = (start + end) // 2
        if value <= mid:
            count += tree[node*2+1]
            node = node * 2
            end = mid
        else:
            node = node * 2 + 1
            start = mid + 1
    
    return count

N = int(input())

stars = []
for _ in range(N):
    stars.append(list(map(int, input().split())))

stars.sort(key=lambda x: x[1])
count = 0
y_list = [0]
for i in range(1, N):
    if stars[i][1] != stars[i-1][1]:
        count += 1
    y_list.append(count)

for i in range(N):
    stars[i][1] = y_list[i]

stars.sort(key=lambda x: x[0])

tree_l = [0] * (2 ** 19)
tree_r = [0] * (2 ** 19)

for star in stars:
    add(tree_r, 1, 0, N-1, star[1])

tmp_list = [stars[0]]
x_value = stars[0][0]

answer = 0

for i in range(1, N+1):
    if i != N:
        # x좌표가 같은 것끼리 tmp_list에 추가
        if stars[i][0] == x_value:
            tmp_list.append(stars[i])
            continue

    # tree_r에서 tmp_list에 존재하는 별들 제거
    for tmp in tmp_list:
        remove(tree_r, 1, 0, N-1, tmp[1])

    for tmp in tmp_list:
        left = find(tree_l, tmp[1])
        right = find(tree_r, tmp[1])
        answer = (answer + left * right) % MAX

    # tree_l에서 tmp_list에 존재하는 별들 추가
    for tmp in tmp_list:
        add(tree_l, 1, 0, N-1, tmp[1])

    if i != N:
        tmp_list = [stars[i]]
        x_value = stars[i][0]

print(answer)