from collections import deque
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for u in range(1, N+1):
    graph[u] = sorted(graph[u], reverse=True)

visited = [False] * (N+1)

visited[R] = True
q = deque([R])

answer = [0] * (N+1)
count = 0
while q:
    now = q.popleft()

    count += 1
    answer[now] = count

    for next in graph[now]:
        if not visited[next]:
            visited[next] = True
            q.append(next)

for num in answer[1:]:
    print(num)