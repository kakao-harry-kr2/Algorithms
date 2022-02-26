# 축구 전술

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

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

T = int(input())

for testNum in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V)]
    reverse_graph = [[] for _ in range(V)]

    for _ in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        reverse_graph[B].append(A)

    stack = []
    visited = [False] * V

    for i in range(V):
        if not visited[i]:
            dfs(i, visited, stack)

    visited = [False] * V
    result = []

    while stack:
        scc = []
        node = stack.pop()
        if not visited[node]:
            reverse_dfs(node, visited, scc)
            result.append(scc)

    # SCC 관계를 그래프로
    node2scc = [None] * V
    len_scc = len(result)
    indegree = [0] * len_scc

    for i in range(len_scc):
        for res in result[i]:
            node2scc[res] = i
    
    for i in range(V):
        for j in graph[i]:
            if node2scc[i] != node2scc[j]:
                indegree[node2scc[j]] = 1

    if indegree.count(0) != 1:
        print("Confused")
    else:
        for i in sorted(result[indegree.index(0)]):
            print(i)
    
    if testNum != T - 1:
        input()
        print()