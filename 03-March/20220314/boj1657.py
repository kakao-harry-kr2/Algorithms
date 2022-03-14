# 두부장수 장홍준

import sys
input = sys.stdin.readline

grade = [[10, 8, 7, 5, 0, 1], [8, 6, 4, 3, 0, 1], [7, 4, 3, 2, 0, 1], [5, 3, 2, 2, 0, 1], [0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0]]

N, M = map(int, input().split())
table = [list(map(lambda x: ord(x)-65, list(input().rstrip()))) for _ in range(N)]

dp = [[0] * (1 << M) for _ in range(N * M + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(M):
        for b in range(1 << M):
            # 이미 (i, j)를 사용한 경우 또는
            if b & (1 << j):
                dp[i*M+j+1][b - (1 << j)] = max(dp[i*M+j+1][b - (1 << j)], dp[i*M+j][b])
                continue
                
            # (i, j)를 사용하지 않고 건너뛰는 경우
            dp[i*M+j+1][b] = max(dp[i*M+j+1][b], dp[i*M+j][b])
            
            # 오른쪽이랑 묶이는 경우
            if j != M - 1 and not(b & 1 << (j+1)):
                dp[i*M+j+2][b] = max(dp[i*M+j+2][b], dp[i*M+j][b] + grade[table[i][j]][table[i][j+1]])

            # 아래쪽과 묶이는 경우
            if i != N - 1:
                dp[i*M+j+1][b + (1 << j)] = max(dp[i*M+j+1][b + (1 << j)], dp[i*M+j][b] + grade[table[i][j]][table[i+1][j]])
            
print(dp[N*M][0])