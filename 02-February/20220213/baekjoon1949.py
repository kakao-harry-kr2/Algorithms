# 우수 마을

import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

N = int(input())
numList = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dp = [[numList[i], 0] for i in range(N+1)]
visited = [False] * (N+1)

def dfs(start):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)
            dp[start][0] += dp[node][1]
            dp[start][1] += max(dp[node])

dfs(1)

print(max(dp[1]))