import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[] for _ in range(N)]
slt = [-1] * M

for i in range(N):
    works = list(map(int, input().split()))[1:]
    for j in works:
        graph[i].append(j-1)

def dfs(visited, src):
    if visited[src]:
        return False
    
    visited[src] = True

    for dst in graph[src]:
        if slt[dst] == -1 or dfs(visited, slt[dst]):
            slt[dst] = src
            return True
    
    return False

# 각 직원이 최소 1개의 일 담당: 이분매칭
cnt = 0
for i in range(N):
    visited = [False] * N
    if dfs(visited, i):
        cnt += 1

# 각 직원마다 추가적인 업무가 가능한지 파악
for i in range(N):
    while K > 0:
        visited = [False] * N
        if dfs(visited, i):
            K -= 1
            cnt += 1
        else:
            break

print(cnt)