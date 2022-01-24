import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = []
for _ in range(N):
    row = []
    inputStr = input()
    for j in range(M):
        row.append(int(inputStr[j]))
    table.append(row)

visited = [[False] * M for _ in range(N)]

dx_list = [0, 0, 1, -1]
dy_list = [1, -1, 0, 0]

def search(i, j, visited):
    visited[i][j] = True
    for k in range(4):
        dx = dx_list[k]
        dy = dy_list[k]        
        if 0 <= i + dx < N and 0 <= j + dy < M and table[i+dx][j+dy] == 0 and visited[i+dx][j+dy] == False:
            search(i+dx, j+dy, visited)

count = 0
for i in range(N):
    for j in range(M):
        if table[i][j] == 0 and visited[i][j] == False:
            search(i, j, visited)
            count += 1

print(count)