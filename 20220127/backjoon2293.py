import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coinList = [int(input()) for _ in range(n)]

dp = [0] * (k+1)
dp[0] = 1

for coin in coinList:
    for i in range(coin, k+1):
        dp[i] += dp[i-coin]

print(dp[k])