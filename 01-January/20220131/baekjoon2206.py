from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[[-1, -1] for _ in range(M)]  for _ in range(N)]

x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

# (count, i, j, used)
q = deque([(1, 0, 0, False)])
visited[0][0][0] = True

while q:
    count, i, j, used = q.popleft()
    if i == N-1 and j == M-1:
        print(count)
        exit()
    for k in range(4):
        next_i, next_j = i + x_list[k], j + y_list[k]
        if 0 <= next_i < N and 0 <= next_j < M:
            # 이미 한 개의 벽을 부순 경우
            if used:
                if not visited[next_i][next_j][1] and table[next_i][next_j] == 0:
                    visited[next_i][next_j][1] = True
                    q.append((count+1, next_i, next_j, True))
            # 아직 벽을 부수지 않은 경우
            else:
                if not visited[next_i][next_j][0] and table[next_i][next_j] == 0:
                    visited[next_i][next_j][0] = True
                    q.append((count+1, next_i, next_j, False))
                elif table[next_i][next_j] == 1:
                    visited[next_i][next_j][1] = True
                    q.append((count+1, next_i, next_j, True))

print(-1)