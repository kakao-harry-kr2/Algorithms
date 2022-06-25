def dfs(graph, slt, visited, src):
    if visited[src]: return False
    visited[src] = True

    for dst in graph[src]:
        if slt[dst] == -1 or dfs(graph, slt, visited, slt[dst]):
            slt[dst] = src
            return True
    
    return False

cheatList = [[-1, -1], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 1]]

C = int(input())

for _ in range(C):
    N, M = map(int, input().split())
    table = [list(map(lambda x: True if x == '.' else False, list(input()))) for _ in range(N)]

    count = 0
    graph = [[] for _ in range(N*M)]
    for i in range(N):
        for j in range(M):
            if table[i][j]:
                count += 2
                for di, dj in cheatList:
                    if 0 <= i + di < N and 0 <= j + dj < M and table[i+di][j+dj]:
                        graph[i*M+j].append((i+di)*M+(j+dj))
    
    slt = [-1] * (N*M)

    for i in range(N*M):
        visited = [False] * (N*M)
        if dfs(graph, slt, visited, i):
            count -= 1
    
    print(count//2)