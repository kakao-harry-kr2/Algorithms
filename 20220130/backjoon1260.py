from collections import deque
import sys
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

# DFS
def dfs(visited, start):
    result.append(start)
    visited[start] = True
    for i in graph[start]:
        if not visited[i]:
            dfs(visited, i)

visited = [False] * (N+1)
result = []

dfs(visited, V)
print(*result)

# BFS
q = deque([V])

visited = [False] * (N+1)
result = [V]
visited[V] = True

while q:
    now = q.popleft()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            result.append(i)
            q.append(i)

print(*result)