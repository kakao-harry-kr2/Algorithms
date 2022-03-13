# 방법을 출력하지 않는 숫자 맞추기

import sys
input = sys.stdin.readline
INF = 10 ** 5

N = int(input())
initial = input()
final = input()

total = []
for i in range(N):
    value = (int(final[i]) - int(initial[i]) + 10) % 10
    total.append(value)

dp = [[INF] * 10 for _ in range(N)]
dp[0][total[0]] = total[0]
dp[0][0] = (10 - total[0]) % 10

for i in range(N-1):
    for j in range(10):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j] + (10 + j - total[i+1]) % 10)
        dp[i+1][total[i+1]] = min(dp[i+1][total[i+1]], dp[i][j] + (10 + total[i+1] - j) % 10)

print(min(dp[N-1]))