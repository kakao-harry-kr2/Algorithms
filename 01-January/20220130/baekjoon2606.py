from collections import deque

V = int(input())
E = int(input())

graph = [[] for _ in range(V+1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited = [False] * (V + 1)
visited[1] = True

while q:
    now = q.popleft()
    for i in graph[now]:
        if not visited[i]:
            visited[i] = True
            q.append(i)

print(visited.count(True) - 1)