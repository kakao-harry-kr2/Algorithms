# 다리 만들기 2

from collections import deque
import sys
input = sys.stdin.readline

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력 받기
N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

def bfs(islands:list, visited:list, i, j):
    global N, M
    island = [(i, j)]
    visited[i][j] = True
    queue = deque([[i, j]])
    x_list = [-1, 1, 0, 0]
    y_list = [0, 0, -1, 1]
    while queue:
        now_i, now_j = queue.popleft()
        for k in range(4):
            next_i, next_j = now_i + x_list[k], now_j + y_list[k]
            if 0 <= next_i < N and 0 <= next_j < M and table[next_i][next_j] == 1 and not visited[next_i][next_j]:
                island.append((next_i, next_j))
                visited[next_i][next_j] = True
                queue.append((next_i, next_j))
    
    islands.append(island)


# 섬을 판단하기
islands = []
visited = [[False] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if table[i][j] == 1 and not visited[i][j]:
            bfs(islands, visited, i, j)

# 섬의 개수
len_islands = len(islands)

# 두 섬 사이의 다리 길이 계산
bridges = []

for i in range(1, len_islands):
    for j in range(i):
        island1 = islands[i]
        island2 = islands[j]

        bridge = 10
        for x1, y1 in island1:
            for x2, y2 in island2:
                if x1 == x2 and abs(y1 - y2) > 2:
                    able = True
                    for k in range(min(y1, y2) + 1, max(y1, y2)):
                        if table[x1][k] == 1:
                            able = False
                            break
                    if able:
                        bridge = min(bridge, abs(y1 - y2) - 1)
                
                if y1 == y2 and abs(x1 - x2) > 2:
                    able = True
                    for k in range(min(x1, x2) + 1, max(x1, x2)):
                        if table[k][y1] == 1:
                            able = False
                            break
                    if able:
                        bridge = min(bridge, abs(x1 - x2) - 1)
        
        if bridge != 10:
            bridges.append((bridge, i, j))

bridges.sort()

# minimum spanning tree
result, count = 0, 0
parent = [i for i in range(len_islands)]

for dist, i, j in bridges:
    if find_parent(parent, i) != find_parent(parent, j):
        union_parent(parent, i, j)
        result += dist
        count += 1
    
    if count == len_islands - 1:
        break

print(result if count == len_islands - 1 else -1)