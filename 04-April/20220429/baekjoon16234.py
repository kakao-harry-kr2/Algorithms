# 00:23:08

import sys
sys.setrecursionlimit(2500)

N, L, R = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(N)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
next = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        for k in range(4):
            next_i, next_j = i + move[k][0], j + move[k][1]
            if 0 <= next_i < N and 0 <= next_j < N:
                next[i][j].append((next_i, next_j))

def bfs(visited, i, j, union:list):
    visited[i][j] = True
    union.append((i, j))
    for next_i, next_j in next[i][j]:
        if not visited[next_i][next_j] and L <= abs(population[i][j] - population[next_i][next_j]) <= R:
            bfs(visited, next_i, next_j, union)

count = 0
while True:
    moving = False
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                union = []
                bfs(visited, i, j, union)
                total = 0
                for k, l in union:
                    total += population[k][l]
                avg = total // len(union)
                for k, l in union:
                    if not moving and population[k][l] != avg:
                        moving = True
                    population[k][l] = avg
    
    if not moving:
        print(count)
        break
    
    count += 1