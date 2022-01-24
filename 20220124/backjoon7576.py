from collections import deque
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
dx_list = [0, 0, -1, 1]
dy_list = [-1, 1, 0, 0]

def bfs(searchList):
    queue = deque()
    for search in searchList:
        queue.append([search[0], search[1], 1])
    while queue:
        tomato_i, tomato_j, distance = queue.popleft()
        for k in range(4):
            next_i, next_j = tomato_i + dx_list[k], tomato_j + dy_list[k]
            if 0 <= next_i < N and 0 <= next_j < M and table[next_i][next_j] == 0:
                queue.append([next_i, next_j, distance+1])
                table[next_i][next_j] = distance+1

searchList = []
for i in range(N):
    for j in range(M):
        if table[i][j] == 1:
            searchList.append([i, j])

bfs(searchList)

answer = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 0:
            print(-1)
            exit()
        if table[i][j] > answer:
            answer = table[i][j]

print(answer-1)