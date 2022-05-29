"""
n: 총 node의 수
paths: [출발지, 도착지, 가중치]...
gates: 출입구
summits: 산봉우리
출입구에서 출발해서 쉼터들을 지나 산봉우리를 찍고 다시 출입구로 오는 경로 중에서
최대 가중치의 값을 최소로 하는 경로를 찾아라
return [산봉우리의 번호, 최대 가중치의 최솟값]
최대 가중치의 최솟값이 동일하다면, 산봉우리의 번호가 작은 경로
"""

def dfs(graph, visited, idx2type, now, L):
    # 출입구에 도착
    if idx2type[now] == 1:
        return True
    
    visited[now] = True

    for next, w in graph[now]:
        if idx2type[next] != 2 and not visited[next] and w <= L:
            if dfs(graph, visited, idx2type, next, L):
                return True
    
    return False

# Parametric Search
def solution(n, paths, gates, summits):
    summits.sort()

    # 0: 쉼터, 1: 출입구, 2: 쉼터
    idx2type = [0] * (n+1)
    for gate in gates:
        idx2type[gate] = 1
    for summit in summits:
        idx2type[summit] = 2
    
    graph = [[] for _ in range(n+1)]
    max_weight = 0
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        max_weight = max(max_weight, w)
    
    answer = [None, None]
    start, end = 0, max_weight
    while start <= end:
        L = (start + end) // 2
        isOk = False

        visited = [False] * (n+1)
        for summit in summits:
            # summit에서 출발해서 가중치 L이하의 경로만 이용해서 gate에 도달할 수 있는가?
            if dfs(graph, visited, idx2type, summit, L):
                answer = [summit, L]
                end = L - 1
                isOk = True
                break
        
        if not isOk:
            start = L + 1
    
    return answer

print(solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5])) # [5, 3]
print(solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])) # [3, 4]
print(solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])) # [5, 1]
print(solution(5, [[1, 3, 10], [1, 4, 20], [2, 3, 4], [2, 4, 6], [3, 5, 20], [4, 5, 6]], [1, 2], [5])) # [5, 6]