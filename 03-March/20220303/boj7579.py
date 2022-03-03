# 앱

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

dp = [-1] * 10001
dp[0] = 0

for i in range(N):
    for j in reversed(range(10001-cost[i])):
        if dp[j] != -1:
            dp[j+cost[i]] = max(dp[j+cost[i]], dp[j] + memory[i])

for i in range(10001):
    if dp[i] >= M:
        print(i)
        break