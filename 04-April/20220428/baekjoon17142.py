# 00:44:21

from itertools import combinations
from collections import deque
INF = 2500

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
notWalls = 0
for i in range(N):
    for j in range(N):
        if table[i][j] == 0:
            notWalls += 1

virus = [(i, j) for i in range(N) for j in range(N) if table[i][j] == 2]
move = [(0, -1), (0, 1), (-1, 0), (1, 0)]

answer = INF
for comb in combinations(virus, M):
    q = deque()
    visited = [[False] * N for _ in range(N)]

    for i, j in comb:
        q.append((0, i, j))
        visited[i][j] = True
    
    value = 0
    count = 0
    while q:
        dist, i, j = q.popleft()
        if table[i][j] != 2:
            value = max(value, dist)
            count += 1
        
        for k in range(4):
            next_i, next_j = i + move[k][0], j + move[k][1]
            if 0 <= next_i < N and 0 <= next_j < N and not visited[next_i][next_j] and table[next_i][next_j] != 1:
                q.append((dist+1, next_i, next_j))
                visited[next_i][next_j] = True

    if count != notWalls:
        continue
    answer = min(answer, value)

print(answer if answer != 2500 else -1)