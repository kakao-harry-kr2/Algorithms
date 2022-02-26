# 2-SAT - 3

# x_1 ~ x_N : 1 ~ N
# not x_1 ~ not x_N : N + 1 ~ N + N

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M = map(int, input().split())

graph = [[] for _ in range(2 * N + 1)]
reverse_graph = [[] for _ in range(2 * N + 1)]

def num2node(num):
    if num > 0:
        return num
    else:
        return N - num

for _ in range(M):
    a, b = map(int, input().split())
    # not a -> b
    # not b -> a
    graph[num2node(-a)].append(num2node(b))
    graph[num2node(-b)].append(num2node(a))
    reverse_graph[num2node(b)].append(num2node(-a))
    reverse_graph[num2node(a)].append(num2node(-b))

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
visited = [False] * (2 * N + 1)

for i in range(1, 2 * N + 1):
    if not visited[i]:
        dfs(i, visited, stack)

visited = [False] * (2 * N + 1)
result = []

while stack:
    scc = []
    node = stack.pop()
    if not visited[node]:
        reverse_dfs(node, visited, scc)
        result.append(scc)

for res in result:
    visited = [False] * (N + 1)
    for r in res:
        if r > N:
            r -= N
        if not visited[r]:
            visited[r] = True
        else:
            print(0)
            exit()

print(1)