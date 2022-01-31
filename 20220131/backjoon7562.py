from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

x_list = [-2, -2, -1, -1, 1, 1, 2, 2]
y_list = [-1, 1, -2, 2, -2, 2, -1, 1]

for _ in range(T):
    I = int(input())
    visited = [[False] * I for _ in range(I)]
    i, j = map(int, input().split())
    end_i, end_j = map(int, input().split())

    q = deque([[0, i, j]])
    while q:
        count, now_i, now_j = q.popleft()
        if now_i == end_i and now_j == end_j:
            print(count)
            break
        for k in range(8):
            next_i, next_j = now_i + x_list[k], now_j + y_list[k]
            if 0 <= next_i < I and 0 <= next_j < I and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                q.append([count+1, next_i, next_j])