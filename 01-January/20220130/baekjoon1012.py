import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    table = [[0] * M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        table[y][x] = 1

    visited = [[False] * M for _ in range(N)]

    count = 0

    x_list = [0, 0, -1, 1]
    y_list = [-1, 1, 0, 0]

    def bfs(i, j):
        global count
        for k in range(4):
            next_i, next_j = i + x_list[k], j + y_list[k]
            if 0 <= next_i < N and 0 <= next_j < M and table[next_i][next_j] == 1 and not visited[next_i][next_j]:
                visited[next_i][next_j] = True
                bfs(next_i, next_j)

    for i in range(N):
        for j in range(M):
            if table[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j)
                count += 1
    
    print(count)