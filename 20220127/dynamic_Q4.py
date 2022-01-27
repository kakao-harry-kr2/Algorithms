import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
moneyList = [int(input()) for _ in range(N)]

dp = [-1] * (M+1)
dp[0] = 0

for i in range(1, M+1):
    li = []
    for money in moneyList:
        if i >= money and dp[i-money] != -1:
            li.append(dp[i-money])
    
    if len(li) > 0:
        dp[i] = min(li) + 1

print(dp[M])