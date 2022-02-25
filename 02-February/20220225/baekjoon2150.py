# Strongly Connected Component

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

V, E = map(int, input().split())
graph = [[] for _ in range(V + 1)]
reverse_graph = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B = map(int, input().split())
    graph[A].append(B)
    reverse_graph[B].append(A)

def dfs(start:int, visited:list, stack:list):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited, stack)
    
    stack.append(start)

def reverse_dfs(start:int, visited:list, stack:list):
    visited[start] = True
    stack.append(start)
    for node in reverse_graph[start]:
        if not visited[node]:
            reverse_dfs(node, visited, stack)

stack = []
visited = [False] * (V + 1)

for i in range(1, V + 1):
    if not visited[i]:
        dfs(i, visited, stack)

visited = [False] * (V + 1)
result = []

while stack:
    scc = []
    node = stack.pop()
    if not visited[node]:
        reverse_dfs(node, visited, scc)
        result.append(sorted(scc))

print(len(result))

results = sorted(result)
for res in results:
    print(*res, -1)