from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx_list = [0, 0, -1, 1]
dy_list = [-1, 1, 0, 0]

def bfs():
    visited[0][0] = True
    queue = deque([[0, 0, 1]])
    while queue:
        i, j, count = queue.popleft()
        for k in range(4):
            next_i, next_j = i + dx_list[k], j + dy_list[k]
            if next_i == N-1 and next_j == M-1:
                print(count+1)
                exit()
            if 0 <= next_i < N and 0 <= next_j < M and table[next_i][next_j] == 1 and visited[next_i][next_j] == False:
                queue.append([next_i, next_j, count+1])
                visited[next_i][next_j] = True

bfs()