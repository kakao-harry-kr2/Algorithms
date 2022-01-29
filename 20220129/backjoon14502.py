from itertools import combinations
from collections import deque
import copy

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

# array : 빈 칸의 좌표들
array = [(i, j) for i in range(N) for j in range(M) if table[i][j] == 0]
# virus
virus = [(i, j) for i in range(N) for j in range(M) if table[i][j] == 2]

# 움직일 수 있는 방향
x_list = [0, 0, -1, 1]
y_list = [-1, 1, 0, 0]

# 안전영역의 최댓값
answer = 0

# array에서 3개를 뽑아서 벽을 세우고 안전 영역을 계산
for comb in combinations(array, 3):
    new_table = copy.deepcopy(table)
    for i, j in comb:
        new_table[i][j] = 1

    # BFS
    q = deque(virus)
    while q:
        now_x, now_y = q.popleft()
        # 상하좌우 움직임에 대해
        for i in range(4):
            next_x, next_y = now_x + x_list[i], now_y + y_list[i]
            if 0 <= next_x < N and 0 <= next_y < M and new_table[next_x][next_y] == 0:
                # 다음 좌표가 지도 내부에 존재하고, 빈 칸인 경우 -> 바이러스 감염
                new_table[next_x][next_y] = 2
                q.append((next_x, next_y))
    
    safe_count = 0
    # 모든 바이러스가 퍼진 후에 안전영역 계산
    for i in range(N):
        for j in range(M):
            if new_table[i][j] == 0:
                safe_count += 1

    answer = max(answer, safe_count)

print(answer)