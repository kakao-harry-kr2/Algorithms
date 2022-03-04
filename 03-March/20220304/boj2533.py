# 사회망 서비스(SNS)

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N + 1)

# 해당 노드가 early adapter인 경우 / 아닌 경우
dp = [[1, 0] for _ in range(N + 1)]

def dfs(start):
    visited[start] = True
    for child in graph[start]:
        if not visited[child]:
            dfs(child)
            dp[start][0] += min(dp[child])
            dp[start][1] += dp[child][0]

dfs(1)

print(min(dp[1]))