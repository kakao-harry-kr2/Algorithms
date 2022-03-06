# 아이돌

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def num2node(N, num):
    if num < 0:
        return N - num
    else:
        return num

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

while True:
    try:
        N, M = map(int, input().split())
    except:
        break

    graph = [[] for _ in range(2 * N + 1)]
    reverse_graph = [[] for _ in range(2 * N + 1)]

    for _ in range(M):
        i, j = map(int, input().split())
        graph[num2node(N, -i)].append(num2node(N, j))
        graph[num2node(N, -j)].append(num2node(N, i))
        reverse_graph[num2node(N, j)].append(num2node(N, -i))
        reverse_graph[num2node(N, i)].append(num2node(N, -j))

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

    num2scc = [None] * (2 * N + 1)

    for i in range(len(result)):
        for r in result[i]:
            num2scc[r] = i

    isTrue = True
    for i in range(1, N + 1):
        if num2scc[i] == num2scc[N + i]:
            isTrue = False

    if not isTrue:
        print('no')
        continue

    def flip(num):
        if num > N:
            return num - N
        else:
            return num + N

    value = [-1] * (2 * N + 1)

    for i in range(len(result)):
        for r in result[i]:
            if value[r] == -1:
                value[r] = 0
                value[flip(r)] = 1

    print('yes' if value[1] else 'no')