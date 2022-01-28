N, M = map(int, input().split())

graph = [[0] * (N + 1) for _ in range(N + 1)]

for a in range(1, N + 1):
    graph[a][a] = 1

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            if graph[a][k] == 1 and graph[k][b] == 1:
                graph[a][b] = 1

count = 0

for i in range(1, N + 1):
    count_in, count_out = -1, -1
    for j in range(1, N + 1):
        if graph[j][i] != 0:
            count_in += 1
        if graph[i][j] != 0:
            count_out += 1

    if count_in + count_out == N - 1:
        count += 1

print(count)