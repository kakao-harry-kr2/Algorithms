import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N+1):
    graph[i] = sorted(graph[i])

answer = [0] * (N+1)
count = 0

def dfs(visited, now):
    global count
    visited[now] = True

    count += 1
    answer[now] = count

    for next in graph[now]:
        if not visited[next]:
            dfs(visited, next)

visited = [False] * (N+1)

dfs(visited, R)

for num in answer[1:]:
    print(num)