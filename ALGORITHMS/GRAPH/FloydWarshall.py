# Negative Cycle이 없는 그래프에서 임의의 노드들 간의 최단경로 탐색
# Negative Weight는 존재할 수 있다.

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    graph[a][a] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    # a에서 b로 가는 경로가 여러개인 경우
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print("%2d" % graph[a][b], end=' ')
    print()