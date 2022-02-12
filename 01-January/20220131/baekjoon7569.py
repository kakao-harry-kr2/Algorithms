from collections import deque
import sys
input = sys.stdin.readline

M, N, H = map(int, input().split())
table = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

moveList = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

q = deque()

# 초기 상태에 익어있는 배추를 q에 삽입
for i in range(H):
    for j in range(N):
        for k in range(M):
            if table[i][j][k] == 1:
                q.append((1, i, j, k))

# BFS
while q:
    count, now_i, now_j, now_k = q.popleft()
    for m in moveList:
        next_i, next_j, next_k = now_i + m[0],  now_j + m[1], now_k + m[2]
        if 0 <= next_i < H and 0 <= next_j < N and 0 <= next_k < M and table[next_i][next_j][next_k] == 0:
            table[next_i][next_j][next_k] = count + 1
            q.append((count+1, next_i, next_j, next_k))

max_date = 0

for i in range(H):
    for j in range(N):
        for k in range(M):
            # 최종적으로 익지 않은 상태의 토마토 존재
            if table[i][j][k] == 0:
                print(-1)
                exit()
            max_date = max(max_date, table[i][j][k])

print(max_date-1)