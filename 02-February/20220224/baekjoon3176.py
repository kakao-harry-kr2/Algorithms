# 도로 네트워크

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))

visited = [False] * (N + 1)
depth = [0] * (N + 1)
parent = [[0] * (N + 1) for _ in range(17)]
_min = [[None] * (N + 1) for _ in range(17)]
_max = [[None] * (N + 1) for _ in range(17)]
parent[0][1] = 1
_min[0][1] = 1000000
_max[0][1] = 0

def bfs():
    q = deque()
    visited[1] = True
    q.append([1, 0])
    
    while q:
        now, d = q.popleft()
        depth[now] = d
        for node, _dist in graph[now]:
            if not visited[node]:
                visited[node] = True
                parent[0][node] = now
                _min[0][node] = _dist
                _max[0][node] = _dist
                q.append([node, d + 1])

bfs()

# parent, _min, _max 구하기
for i in range(1, 17):
    for j in range(1, N + 1):
        parent[i][j] = parent[i-1][parent[i-1][j]]
        _min[i][j] = min(_min[i-1][j], _min[i-1][parent[i-1][j]])
        _max[i][j] = max(_max[i-1][j], _max[i-1][parent[i-1][j]])

K = int(input())

for _ in range(K):
    x, y = map(int, input().split())

    depth_x = depth[x]
    depth_y = depth[y]

    min_value = 1000000
    max_value = 0

    # depth를 동일하게 맞춰주는 과정
    if depth_x > depth_y:
        diff = depth_x - depth_y
        for i in range(17):
            if 1 & (diff >> i):
                min_value = min(min_value, _min[i][x])
                max_value = max(max_value, _max[i][x])
                x = parent[i][x]
    
    if depth_x < depth_y:
        diff = depth_y - depth_x
        for i in range(17):
            if 1 & (diff >> i):
                min_value = min(min_value, _min[i][y])
                max_value = max(max_value, _max[i][y])
                y = parent[i][y]
    
    if x == y:
        print(min_value, max_value)
        continue
    
    # 올라가면서 부모가 같은지 확인
    for i in reversed(range(17)):
        if parent[i][x] != parent[i][y]:
            min_value = min(min_value, _min[i][x], _min[i][y])
            max_value = max(max_value, _max[i][x], _max[i][y])

            x = parent[i][x]
            y = parent[i][y]

    min_value = min(min_value, _min[0][x], _min[0][y])
    max_value = max(max_value, _max[0][x], _max[0][y])

    print(min_value, max_value)