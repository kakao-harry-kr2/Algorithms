# 파일 합치기

import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
    K = int(input())
    sizeList = list(map(int, input().split()))

    summation = [[0] * K for _ in range(K)]
    for i in range(K):
        for j in range(i, K):
            summation[i][j] = sum(sizeList[i:j+1])

    dp = [[INF] * K for _ in range(K)]
    for i in range(K):
        dp[i][i] = 0
    
    for diff in range(1, K):
        for i in range(K - diff):
            min_value = INF
            # i ~ j / j+1 ~ i+diff
            for j in range(i, i+diff):
                min_value = min(min_value, dp[i][j] + dp[j+1][i+diff] + summation[i][i+diff])
            dp[i][i+diff] = min_value
    
    print(dp[0][K-1])