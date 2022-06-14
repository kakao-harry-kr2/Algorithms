N = int(input())
table = [list(map(int, input())) for _ in range(N)]

# dp[i][j]: 
# 현재까지 보유한 아티스트의 정보: i & 마지막으로 소유한 아티스트 -> j
# 값 -> [마지막으로 구매한 가격, 소유했던 사람의 수]
dp = [[[10, 0] for _ in range(N)] for _ in range(2 ** N)]

# 처음에 1번 아티스트가 외부 상인에게 구매
dp[1][0] = [0, 1]

answer = 0
for i in range(2 ** N):
    for j in range(N):
        # 만약 (i, j)의 상태가 유효하다면...?
        if dp[i][j][0] != 10:
            # 다음에 그림을 소유할 아티스트 후보: k
            for k in range(N):
                # 조건 1을 만족하지 않는 경우
                if table[j][k] < dp[i][j][0]:
                    continue

                # 조건 2를 만족하지 않는 경우
                if (i >> k) & 1:
                    continue

                # 같은 상태 i를 만드는데, 더 적은 비용이 들어간 경우 업데이트
                if table[j][k] < dp[i+2**k][k][0]:
                    dp[i+2**k][k] = [table[j][k], dp[i][j][1]+1]
                    answer = max(answer, dp[i+2**k][k][1])

print(answer)