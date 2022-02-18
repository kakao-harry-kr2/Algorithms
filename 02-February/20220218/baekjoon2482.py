# 색상환

N = int(input())
K = int(input())

if K > N // 2:
    print(0)
    exit()

answer = 0

# 0번째 색 선택하는 경우 : l = 0
# 0번째 색 선택하지 않는 경우 : l = 1
for l in range(2):
    # dp[i][j] : i번째까지 j개의 색 선택
    dp = [[[0, 0] for _ in range(K+1)] for _ in range(N)]

    if l == 1:
        for i in range(N):
            dp[i][0] = [0, 1]
    else:
        dp[0][1] = [1, 0]

    for i in range(1, N):
        for j in range(1, K+1):
            # i번째까지 j개의 색 선택 [i번째 선택, i번째 선택X]
            dp[i][j] = [dp[i-1][j-1][1], sum(dp[i-1][j])]

    if l == 0:
        answer += dp[N-1][K][1]
    else:
        answer += sum(dp[N-1][K])

print(answer % 1000000003)