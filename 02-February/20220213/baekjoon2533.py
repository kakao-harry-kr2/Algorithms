# 사회망 서비스(SNS)

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

dp = [[1, 0] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)
            dp[start][0] += min(dp[node])
            dp[start][1] += dp[node][0]

dfs(1)

print(min(dp[1]))