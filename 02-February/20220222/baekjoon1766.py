# 문제집

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

q = []
result = []

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

while q:
    now = heapq.heappop(q)
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            heapq.heappush(q, i)

print(*result)