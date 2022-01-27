X = int(input())

dp = [0] * (X+1)

for i in range(2, X+1):
    li = [dp[i-1]]
    if i % 5 == 0:
        li.append(dp[i//5])
    if i % 3 == 0:
        li.append(dp[i//3])
    if i % 2 == 0:
        li.append(dp[i//2])

    dp[i] = min(li) + 1

print(dp[X])