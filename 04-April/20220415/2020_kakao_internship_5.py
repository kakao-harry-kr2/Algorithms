import sys
sys.setrecursionlimit(10 ** 7)

def dfs(graph, visited, outgoings, now):
    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            outgoings[now].append(next)
            dfs(graph, visited, outgoings, next)

def dfs_solving(outgoings, total_visited, now_visited, now):
    total_visited[now] = True
    
    now_visited[now] = True
    for next in outgoings[now]:
        # 현재 dfs 탐색에서 이미 방문한 경우 -> cycle 발생
        if now_visited[next]:
            return False
            
        if not total_visited[next]:
            if not dfs_solving(outgoings, total_visited, now_visited, next):
                return False
    
    now_visited[now] = False
    return True


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for x, y in path:
        graph[x].append(y)
        graph[y].append(x)

    outgoings = [[] for _ in range(n)]
    visited = [False] * n
    dfs(graph, visited, outgoings, 0)

    for prev, next in order:
        outgoings[prev].append(next)

    # outgoings 내에 cycle이 존재하면 false 존재하지 않으면 true

    total_visited = [False] * n
    for i in range(n):
        if not total_visited[i]:
            now_visited = [False] * n
            if not dfs_solving(outgoings, total_visited, now_visited, i):
                return False

    return True


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]], [[4,1],[5,2]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))