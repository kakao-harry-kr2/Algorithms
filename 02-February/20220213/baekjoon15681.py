# 트리와 쿼리

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

def dfs(graph, visited, children, start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            children[start].append(node)
            dfs(graph, visited, children, node)

def count_nodes(dp, root):
    # 이미 계산한 경우
    if dp[root] != -1:
        return dp[root]
    
    num_of_nodes = 1

    for child in children[root]:
        num_of_nodes += count_nodes(dp, child)
    
    dp[root] = num_of_nodes

    return num_of_nodes


N, R, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

# 각 노드들의 자식 노드
children = [[] for _ in range(N+1)]

dfs(graph, visited, children, R)

dp = [-1] * (N+1)

for _ in range(Q):
    U = int(input())
    ans = count_nodes(dp, U)
    print(ans)