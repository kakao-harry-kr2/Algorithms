# 00:30:48

import sys
sys.setrecursionlimit(10 ** 9)

def rotate(table, x, k):
    global N, M
    i = x - 1
    while i < N:
        table[i] = [table[i][(j-k+M)%M] for j in range(M)]
        i += x

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def bfs(table, visited, i, j, li:list):
    visited[i][j] = True
    li.append((i, j))
    for k in range(4):
        next_i, next_j = (i + move[k][0] + N+1) % (N+1), (j + move[k][1] + M) % M
        if not visited[next_i][next_j] and table[next_i][next_j] == table[i][j]:
            bfs(table, visited, next_i, next_j, li)


def process(table):
    global N, M
    change = False
    visited = [[False] * M for _ in range(N+1)]
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and table[i][j] > 0:
                li = []
                bfs(table, visited, i, j, li)
                if len(li) > 1:
                    change = True
                    for x, y in li:
                        table[x][y] = 0
    
    if not change:
        total = 0
        count = 0
        for i in range(N):
            for j in range(M):
                if table[i][j] > 0:
                    total += table[i][j]
                    count += 1
        if count == 0:
            return
        
        average = total / count
        for i in range(N):
            for j in range(M):
                if table[i][j] != 0:
                    if table[i][j] > average:
                        table[i][j] -= 1
                    elif table[i][j] < average:
                        table[i][j] += 1

N, M, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)] + [[0] * M]

for _ in range(T):
    x, d, k = map(int, input().split())

    k = M - k if d else k
    rotate(table, x, k)

    process(table)

answer = 0
for i in range(N):
    for j in range(M):
        answer += table[i][j]

print(answer)