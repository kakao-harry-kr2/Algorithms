N = int(input())
sharks = sorted([list(map(int, input().split())) for _ in range(N)])

graph = [[] for _ in range(N)]
for i in range(N-1):
    for j in range(i+1, N):
        if sharks[i][0] - sharks[j][0] <= 0 and sharks[i][1] - sharks[j][1] <= 0 and sharks[i][2] - sharks[j][2] <= 0:
            graph[j].append(i)

slt = [-1] * N

def dfs(visited, src):
    if visited[src]: return False
    visited[src] = True

    for dst in graph[src]:
        if slt[dst] == -1 or dfs(visited, slt[dst]):
            slt[dst] = src
            return True
    
    return False

cnt = 0
for i in range(N):
    for _ in range(2):
        visited = [False] * N
        if dfs(visited, i):
            cnt += 1
    
print(N - cnt)