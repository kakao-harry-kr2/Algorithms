import sys
sys.setrecursionlimit(10 ** 5)

def dfs(graph, visited, node2type, now, L):
    if node2type[now] == 1:
        return True
    
    visited[now] = True
    for next, w in graph[now]:
        if not visited[next] and node2type[next] != 2 and w <= L:
            if dfs(graph, visited, node2type, next, L):
                return True
    
    return False

def solution(n, paths, gates, summits):
    summits.sort()
    graph = [[] for _ in range(n+1)]
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))

    # 쉼터: 0, 출입구: 1, 산봉우리: 2
    node2type = {i: 0 for i in range(1, n+1)}
    for gate in gates:
        node2type[gate] = 1
    for summit in summits:
        node2type[summit] = 2
    
    answer = [None, None]
    start, end = 1, 10000000
    while start <= end:
        L = (start + end) // 2

        # weight가 L이하인 경로들만을 통해서 문제의 조건을 만족시킬수 있는지?
        visited = [False] * (n+1)
        isOk = False
        for summit in summits:
            if dfs(graph, visited, node2type, summit, L):
                isOk = True
                answer = [summit, L]
                end = L - 1
                break
        
        if not isOk:
            start = L + 1
    
    return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5]))
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4]))
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5]))
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5]))
