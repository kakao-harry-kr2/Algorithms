import sys
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[INF] * (V+1) for _ in range(V+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_cycle = INF
for i in range(1, V+1):
    min_cycle = min(min_cycle, graph[i][i])

print(min_cycle if min_cycle != INF else -1)