# 직사각형

import sys
input = sys.stdin.readline

def update(cnt_tree, val_tree, node, start, end, left, right, val):
    # 포함되지 않는 경우
    if end < left or right < start:
        return
    
    if left <= start and end <= right:
        cnt_tree[node] += val * (end - start + 1)
    else:
        mid = (start + end) // 2
        update(cnt_tree, val_tree, node*2, start, mid, left, right, val)
        update(cnt_tree, val_tree, node*2+1, mid+1, end, left, right, val)
    
    if cnt_tree[node]:
        val_tree[node] = idx2val[end+1] - idx2val[start]
    else:
        if start == end: val_tree[node] = 0
        else:
            val_tree[node] = val_tree[node*2] + val_tree[node*2+1]

N = int(input())
lines = []
y_list = []

for _ in range(N):
    x1, x2, y1, y2 = map(int, input().split())
    lines.append([x1, y1, y2, 1]) # 직사각형의 왼쪽 변
    lines.append([x2, y1, y2, -1]) # 직사각형의 오른쪽 변
    
    y_list.append(y1)
    y_list.append(y2)

# y좌표들 압축
y_list.sort()

y_index = 0
y_value = y_list[0]
idx2val = [y_value]
val2idx = {y_value: 0}

for i in range(1, 2 * N):
    if y_list[i] != y_list[i-1]:
        y_index += 1
        idx2val.append(y_list[i])
    
    val2idx[y_list[i]] = y_index

for i in range(2 * N):
    lines[i][1] = val2idx[lines[i][1]]
    lines[i][2] = val2idx[lines[i][2]]

# segment tree
cnt_tree = [0] * (2 ** 20)
val_tree = [0] * (2 ** 20)

lines.sort()
prev_x = 0
answer = 0

for line in lines:
    curr_x, y1, y2, val = line
    width = curr_x - prev_x
    height = val_tree[1]
    answer += width * height
    prev_x = curr_x

    update(cnt_tree, val_tree, 1, 0, y_index, y1, y2-1, val)

print(answer)