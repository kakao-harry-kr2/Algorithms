import time, random
import sys
sys.setrecursionlimit(10 ** 8)

def dfs(graph, visited, children, start):
    visited[start] = True

    for node in graph[start]:
        if not visited[node]:
            dfs(graph, visited, children, node)
            children[start].append(1 + sum(children[node]))

def solution(n, edges):
    graph = [[] for _ in range(n)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = [False] * n
    children = [[] for _ in range(n)]

    dfs(graph, visited, children, 0)

    answer = 0
    for i in range(n):
        tmpList = children[i] + [n-1-sum(children[i])]
        tmp = (n-1) ** 2
        for t in tmpList:
            tmp -= t ** 2
        
        answer += tmp
    
    return answer

n = 300000
edges = []
for v1 in range(n-1):
    v2 = random.randint(v1+1, n-1)
    edges.append([v1, v2])

start = time.time()

print(solution(n, edges))

end = time.time()

print(end-start)