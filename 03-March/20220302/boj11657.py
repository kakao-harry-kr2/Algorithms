# 타임머신

import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
outgoings = [[] for _ in range(N + 1)]
incomings = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B, C  = map(int, input().split())
    outgoings[A].append((B, C))
    incomings[B].append((A, C))

dist = [2 * INF] * (N + 1)
start = 1
dist[start] = 0

for i in outgoings[start]:
    dist[i[0]] = i[1]

for k in range(2, N + 1):
    for u in range(1, N + 1):
        for i in incomings[u]:
            if dist[i[0]] < INF and dist[u] > dist[i[0]] + i[1]:
                if k == N:
                    print(-1)
                    exit()
                else:
                    dist[u] = dist[i[0]] + i[1]

for d in dist[2:]:
    print(d if d < INF else -1)