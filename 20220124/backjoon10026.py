import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

N = int(input())
table = [list(input().rstrip()) for _ in range(N)]
dx_list = [0, 0, -1, 1]
dy_list = [-1, 1, 0, 0]

general = {'R': 0, 'G': 1, 'B': 2}
not_general = {'R': 0, 'G': 0, 'B': 1}

def dfs(i, j, visited, dict):
    visited[i][j] = True
    color = table[i][j]
    for k in range(4):
        next_i, next_j = i + dx_list[k], j + dy_list[k]
        if 0 <= next_i < N and 0 <= next_j < N and dict[table[next_i][next_j]] == dict[color] and visited[next_i][next_j] == False:
            dfs(next_i, next_j, visited, dict)

visited1 = [[False] * N for _ in range(N)]
count1 = 0
for i in range(N):
    for j in range(N):
        if visited1[i][j] == False:
            dfs(i, j, visited1, general)
            count1 += 1

visited2 = [[False] * N for _ in range(N)]
count2 = 0
for i in range(N):
    for j in range(N):
        if visited2[i][j] == False:
            dfs(i, j, visited2, not_general)
            count2 += 1

print(count1, count2)