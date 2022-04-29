# 00:19:50

from collections import deque

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
INF = 10 ** 3

shark_x, shark_y, shark_s = None, None, 2
for i in range(N):
    for j in range(N):
        if table[i][j] == 9:
            shark_x, shark_y = i, j
            table[i][j] = 0
            break
    if shark_x != None:
        break

time, cnt = 0, 0
while True:
    """ 먹을 수 있는 물고기 찾기 """
    visited = [[False] * N for _ in range(N)]
    visited[shark_x][shark_y] = True
    q = deque([(0, shark_x, shark_y)])
    closest_dist = INF
    closest_pos = []
    while q:
        dist, x, y = q.popleft()
        if 0 < table[x][y] < shark_s:
            if closest_dist == INF:
                closest_dist = dist
                closest_pos.append((x, y))
            else:
                if dist == closest_dist:
                    closest_pos.append((x, y))
                else:
                    break

        for k in range(4):
            next_x, next_y = x + move[k][0], y + move[k][1]
            if 0 <= next_x < N and 0 <= next_y < N and not visited[next_x][next_y] and table[next_x][next_y] <= shark_s:
                visited[next_x][next_y] = True
                q.append((dist+1, next_x, next_y))
    
    # 더 이상 먹을 수 있는 물고기가 공간에 없는 경우
    if closest_dist == INF:
        break
    
    if len(closest_pos) > 1:
        closest_pos.sort()
    
    time += closest_dist
    cnt += 1
    if cnt == shark_s:
        shark_s += 1
        cnt = 0
    shark_x, shark_y = closest_pos[0]
    table[shark_x][shark_y] = 0

print(time)