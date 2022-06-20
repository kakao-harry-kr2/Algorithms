""" Bipartite Matching Algorithm """

# n개의 src -> m개의 dst
n, m = 5, 5
graph = [[1, 4], [1, 2, 3], [0, 4], [0, 1, 4], [1]]

# 해당 dst가 어떤 src에게 선택되어 있는지
slt = [-1] * m

def dfs(visited, src):
    if visited[src]: return False
    visited[src] = True

    # src x에서 연결할 수 있는 dst들을 탐색
    for dst in graph[src]:
        # 핵심 point!!
        # dst가 아직 선택되지 않았거나
        # dst를 선택한 다른 src가 새로운 dst를 선택할 수 있는 경우
        if slt[dst] == -1 or dfs(visited, slt[dst]):
            slt[dst] = src
            return True
    
    return False

cnt = 0 # 매칭 수
for i in range(n):
    visited = [False] * n
    if dfs(visited, i):
        cnt += 1
    
print("Matching #:", cnt)