import sys
sys.setrecursionlimit(20000)
input = sys.stdin.readline

K = int(input())

def bfs(graph, visited, start):
    type = visited[start]
    for node in graph[start]:
        if visited[node] == -1:
            visited[node] = 1 - type
            bfs(graph, visited, node)

for _ in range(K):
    V, E = map(int, input().split())

    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        a, b = map(int, input().split())
        graph[b].append(a)
        graph[a].append(b)
    
    # -1 : 방문하지 않음
    #  0 : 첫번째 집합
    #  1 : 두번쨰 집합
    visited = [-1] * (V+1)

    for i in range(1, V+1):
        if visited[i] == -1:
            visited[i] = 0
            bfs(graph, visited, i)
    
    isBiGraph = True

    for i in range(1, V+1):
        if isBiGraph == False:
            break
        for j in graph[i]:
            if visited[i] == visited[j]:
                isBiGraph = False
                break
    
    print('YES' if isBiGraph else 'NO')
