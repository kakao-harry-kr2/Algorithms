import sys
input = sys.stdin.readline

N = int(input())
sizeList = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(N)]

# 기본값 초기화
for i in range(N):
    dp[i][i] = 0

for i in range(1, N):
    for j in range(N-i):
        # j ~ j+i 까지의 행렬에 대한 최소 연산
        answer = int(1e9)
        for k in range(j, j+i):
            # j ~ k 와 k+1 ~ j+i로 나누어서 행렬 연산을 하는 경우
            tmp = dp[j][k] + dp[k+1][j+i] + sizeList[j][0] * sizeList[k][1] * sizeList[j+i][1]
            if tmp < answer:
                answer = tmp
        dp[j][j+i] = answer

print(dp[0][N-1])