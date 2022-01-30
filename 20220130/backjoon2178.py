from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

start = (0, 0)
end = (N - 1, M - 1)

q = deque([(1, start)])

while q:
    count, now = q.popleft()
    if now[0] == end[0] and now[1] == end[1]:
        print(count)
        break

    for k in range(4):
        next_i, next_j = now[0] + x_list[k], now[1] + y_list[k]
        if 0 <= next_i < N and 0 <= next_j < M and table[next_i][next_j] == 1 and not visited[next_i][next_j]:
            visited[next_i][next_j] = True
            q.append((count+1, (next_i, next_j)))