INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]
memory = [[None] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            new_value = graph[a][k] + graph[k][b]
            if new_value < graph[a][b]:
                graph[a][b] = new_value
                memory[a][b] = k

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()

def trace(start, end):
    k = memory[start][end]
    if k == None:
        return []
    return trace(start, k) + [k] + trace(k, end)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == 0 or graph[i][j] == INF:
            print(0)
            continue

        walk = [i] + trace(i, j) + [j]
        print(len(walk), *walk)