# 로봇 조종하기

import sys
input = sys.stdin.readline
INF = 10 ** 9

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

dp = [[-INF] * M for _ in range(N)]

dp[0][0] = table[0][0]
for i in range(1, M):
    dp[0][i] = dp[0][i-1] + table[0][i]

for i in range(1, N):
    tmp = [dp[i-1][j] + table[i][j] for j in range(M)]
    right = [tmp[0]]
    for j in range(1, M):
        right.append(max(tmp[j], right[-1] + table[i][j]))
    
    left = [tmp[-1]]
    for j in reversed(range(M-1)):
        left.append(max(tmp[j], left[-1] + table[i][j]))
    
    left.reverse()

    for j in range(M):
        dp[i][j] = max(left[j], right[j])

print(dp[N-1][M-1])