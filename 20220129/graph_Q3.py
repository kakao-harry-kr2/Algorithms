# Topology sort
from collections import deque

N = int(input())
times = [0] * (N + 1)
graph = [[] for _ in range(N+1)]
indegree = [0] * (N + 1)
result = [0] * (N + 1)

for i in range(1, N+1):
    time, *prerequisites, _ = map(int, input().split())
    times[i] = time
    for pre in prerequisites:
        graph[pre].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, N+1):
    if indegree[i] == 0:
        q.append(i)
        result[i] = times[i]

while q:
    now = q.popleft()
    for i in graph[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + times[i])
        if indegree[i] == 0:
            q.append(i)

for res in result[1:]:
    print(res)