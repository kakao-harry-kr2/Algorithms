# Topology sort
from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0] * (N + 1)
    result = [0] * (N + 1)

    for _ in range(K):
        x, y = map(int, input().split())
        graph[x].append(y)
        indegree[y] += 1
    
    W = int(input())

    q = deque()

    for i in range(1, N+1):
        if indegree[i] == 0:
            q.append(i)
            result[i] = times[i]

    while q:
        now = q.popleft()
        if now == W:
            break
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + times[i])
            if indegree[i] == 0:
                q.append(i)

    print(result[W])