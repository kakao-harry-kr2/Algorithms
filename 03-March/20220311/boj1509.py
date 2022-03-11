# 팰린드롬 분할

import sys
input = sys.stdin.readline
INF = 2500

inputStr = input().rstrip()
N = len(inputStr)

dp = [[0] * N for _ in range(N)]
result = [INF] * (N + 1)
result[-1] = 0

for i in range(N):
    dp[i][i] = 1

for i in range(1, N):
    if inputStr[i-1] == inputStr[i]:
        dp[i-1][i] = 1

for i in range(2, N):
    for j in range(N-i):
        if inputStr[j] == inputStr[j+i] and dp[j+1][i+j-1] == 1:
            dp[j][i+j] = 1

for i in range(N):
    result[i] = min(result[i], result[i-1]+1)

    for j in range(i+1, N):
        # i ~ j까지 펠린드롬
        if dp[i][j] != 0:
            result[j] = min(result[j], result[i-1]+1)

print(result[N-1])