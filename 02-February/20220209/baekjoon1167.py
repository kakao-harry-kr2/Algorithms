# 트리의 지름

"""
임의의 한 점에서 가장 먼 노드를 구한 후
해당 노드에서 가장 먼 노드와의 거리를 구하면
그 길이가 트리의 지름이다.

"""
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(1, V + 1):
    a, *edgeList, _ = map(int, input().split())
    for i in range(len(edgeList)//2):
        b = edgeList[2*i]
        c = edgeList[2*i+1]
        graph[a].append((b, c))

visited = [False] * (V + 1)
max_dist = 0

# 1 -> [11] / 3 -> [9] / 4 -> [4, 6] / 2 -> [] / 5 -> []
def dfs(start):
    global max_dist
    visited[start] = True
    li = []
    for node, dist in graph[start]:
        if not visited[node]:
            ret = dfs(node)
            li.append(ret+dist)

    if not li:
        return 0
    elif len(li) == 1:
        max_dist = max(max_dist, li[0])
        return li[0]
    else:
        li.sort()
        max_dist = max(max_dist, li[-2] + li[-1])
        return li[-1]

dfs(1)
print(max_dist)