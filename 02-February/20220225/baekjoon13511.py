# 트리와 쿼리 2

from collections import deque
import math
import sys
input = sys.stdin.readline

N = int(input())
LOG = int(math.log2(N)) + 1

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    graph[v].append((u, w))

visited = [False] * (N + 1)
depth = [0] * (N + 1)

parent = [[0] * (N + 1) for _ in range(LOG)]
parent[0][1] = 1

dist = [[0] * (N + 1) for _ in range(LOG)]
dist[0][1] = 0

# bfs를 통해서 depth, parent[0] 계산
def bfs(start):
    q = deque()
    visited[start] = True
    q.append([start, 0])

    while q:
        now, _depth = q.popleft()
        depth[now] = _depth
        for node, _dist in graph[now]:
            if not visited[node]:
                visited[node] = True
                parent[0][node] = now
                dist[0][node] = _dist
                q.append([node, _depth + 1])

bfs(1)

# parent, dist 계산
for i in range(1, LOG):
    for j in range(1, N + 1):
        tmp_parent = parent[i-1][j]
        parent[i][j] = parent[i-1][tmp_parent]
        dist[i][j] = dist[i-1][j] + dist[i-1][tmp_parent]

M = int(input())

# 1 u v : u에서 v로 가는 비용 출력
def opr1(u, v):
    # depth[u] < depth[v]가 되도록 변경
    if depth[u] > depth[v]:
        v, u = u, v

    # u에서 v로 가는 비용
    _dist = 0

    # u와 v의 depth를 동일하게 처리
    diff = depth[v] - depth[u]
    for i in range(LOG):
        if 1 & (diff >> i):
            _dist += dist[i][v]
            v = parent[i][v]
    
    if u == v:
        return _dist

    # LCA를 찾는 과정
    for i in reversed(range(LOG)):
        if parent[i][u] != parent[i][v]:
            _dist += dist[i][u] + dist[i][v]
            u = parent[i][u]
            v = parent[i][v]
    
    _dist += dist[0][u] + dist[0][v]

    return _dist

# 2 u v k : u에서 v로 가는 경로에 존재하는 정점 중에서 k번째 정점을 출력
def opr2(u, v, k):
    origin_u = u
    origin_v = v

    # 먼저 LCA를 찾자
    if depth[u] > depth[v]:
        v, u = u, v

    diff = depth[v] - depth[u]
    for i in range(LOG):
        if 1 & (diff >> i):
            v = parent[i][v]
    
    if u == v:
        LCA = u

    else:
        for i in reversed(range(LOG)):
            if parent[i][u] != parent[i][v]:
                u = parent[i][u]
                v = parent[i][v]
        
        LCA = parent[0][u]
    
    depth_u = depth[origin_u]
    depth_v = depth[origin_v]
    depth_lca = depth[LCA]

    if depth_u - depth_lca >= k - 1:
        for i in range(LOG):
            if 1 & ((k-1) >> i):
                origin_u = parent[i][origin_u]

        return origin_u

    else:
        diff = depth_u + depth_v - 2 * depth_lca - (k - 1)
        for i in range(LOG):
            if 1 & (diff >> i):
                origin_v = parent[i][origin_v]

        return origin_v

for _ in range(M):
    command = list(map(int, input().split()))

    if command[0] == 1:
        u, v = command[1:]
        print(opr1(u, v))

    else:
        u, v, k = command[1:]
        print(opr2(u, v, k))