from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False] * (N + 1)
depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(17)]
parent[0][1] = 1

# bfs를 통해서 depth, parent[0] 계산
def bfs(start):
    q = deque()
    visited[start] = True
    q.append([start, 0])

    while q:
        now, _depth = q.popleft()
        depth[now] = _depth
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                parent[0][node] = now
                q.append([node, _depth + 1])

bfs(1)

# parent(sparse table) 계산
for i in range(1, 17):
    for j in range(1, N + 1):
        parent[i][j] = parent[i-1][parent[i-1][j]]