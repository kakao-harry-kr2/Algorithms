# 도미노

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

for _ in range(T):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    reverse_graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        A, B = map(int, input().split())
        graph[A].append(B)
        reverse_graph[B].append(A)

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
            result.append(scc)

    # SCC 관계를 그래프로 나타냈을때 incoming edge가 없는 것의 개수
    node2scc = [None] * (V + 1)
    len_scc = len(result)
    indegree = [0] * len_scc

    for i in range(len_scc):
        for res in result[i]:
            node2scc[res] = i
    
    for i in range(1, V + 1):
        for j in graph[i]:
            if node2scc[i] != node2scc[j]:
                indegree[node2scc[j]] = 1
    
    print(indegree.count(0))
