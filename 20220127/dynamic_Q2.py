import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().rstrip().split()))

dp = [0] * N
dp[0], dp[1] = numList[0], max(numList[0], numList[1])

for i in range(2, N):
    dp[i] = max(dp[i-1], dp[i-2] + numList[i])

print(max(dp[-1], dp[-2]))