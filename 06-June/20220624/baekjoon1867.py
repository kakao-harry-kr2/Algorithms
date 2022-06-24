import sys
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[] for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    graph[i-1].append(j-1)

slt = [-1] * n

def dfs(visited, src):
    if visited[src]: return False
    visited[src] = True

    for dst in graph[src]:
        if slt[dst] == -1 or dfs(visited, slt[dst]):
            slt[dst] = src
            return True
    
    return False

answer = 0
for i in range(n):
    visited = [False] * n
    if dfs(visited, i):
        answer += 1

print(answer)