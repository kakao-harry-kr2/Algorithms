# 격자판 채우기

N, M = map(int, input().split())
dp = [[0] * (1 << M) for _ in range(N * M + 1)]
dp[0][0] = 1

for i in range(N):
    for j in range(M):
        for b in range(1 << M):
            # 이미 (i, j)가 채워져있는 비트인 경우
            if b & (1 << j):
                dp[i*M+j+1][b - (1 << j)] += dp[i*M+j][b]
                continue

            # 오른쪽으로 쌓는 경우
            if j != M - 1 and not(b & (1 << (j+1))):
                dp[i*M+j+2][b] += dp[i*M+j][b]
            
            # 아래쪽으로 쌓는 경우
            if i != N - 1:
                dp[i*M+j+1][b | (1 << j)] += dp[i*M+j][b]

print(dp[N*M][0] % 9901)