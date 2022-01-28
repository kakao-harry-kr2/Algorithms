INF = int(1e9)
N, M = map(int, input().split())

graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    graph[i][i] = 1
    
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][K]+graph[K][X]

print(answer if answer < INF else -1)