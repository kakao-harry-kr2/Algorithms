# LCA 2

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

visited = [False] * (N + 1)
depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(17)]
parent[0][1] = 1

def bfs():
    q = deque()
    visited[1] = True
    q.append([1, 0])
    
    while q:
        now, d = q.popleft()
        depth[now] = d
        for node in graph[now]:
            if not visited[node]:
                visited[node] = True
                parent[0][node] = now
                q.append([node, d + 1])

bfs()

for i in range(1, 17):
    for j in range(1, N + 1):
        parent[i][j] = parent[i-1][parent[i-1][j]]

M = int(input())

for _ in range(M):
    x, y = map(int, input().split())

    depth_x = depth[x]
    depth_y = depth[y]

    # depth를 동일하게 맞춰주는 과정
    if depth_x > depth_y:
        diff = depth_x - depth_y
        for i in range(17):
            if 1 & (diff >> i):
                x = parent[i][x]
    
    if depth_x < depth_y:
        diff = depth_y - depth_x
        for i in range(17):
            if 1 & (diff >> i):
                y = parent[i][y]
    
    if x == y:
        print(x)
        continue

    # 올라가면서 부모가 같은지 확인
    for i in reversed(range(17)):
        if parent[i][x] != parent[i][y]:
            x = parent[i][x]
            y = parent[i][y]
    
    print(parent[0][x])