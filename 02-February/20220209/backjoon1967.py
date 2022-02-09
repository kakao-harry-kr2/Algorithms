# 트리의 지름

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def bfs(start):
    global n
    queue = deque()
    queue.append((0, start))
    visited = [False] * (n + 1)
    visited[start] = True
    _max = [0, 0]

    while queue:
        dist, now = queue.popleft()
        for node, d in graph[now]:
            if not visited[node]:
                new_d = dist + d
                queue.append((new_d, node))
                visited[node] = True
                if _max[0] < new_d:
                    _max = [new_d, node]

    return _max   

dist, node = bfs(1)
answer, node = bfs(node)

print(answer)