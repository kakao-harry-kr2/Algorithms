# RGB거리 2

import sys
input = sys.stdin.readline
INF = int(10 ** 10)

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
cost.append(cost[0])

answer = INF

for color in range(3):
    # dp[i][j] : i번째집을 j로 칠하는 최소 비용
    dp = [[INF] * 3 for _ in range(N+1)]
    dp[0][color] = 0

    for i in range(1, N+1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]
    
    answer = min(dp[N][color], answer)

print(answer)