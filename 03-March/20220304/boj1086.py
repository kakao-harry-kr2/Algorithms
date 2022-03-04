# 박성원

import math
import sys
input = sys.stdin.readline

N = int(input())
numList = [int(input()) for _ in range(N)]
K = int(input())

# R[i][j] : (나머지 j)(numList[i])의 나머지
R = [[(j * 10 ** len(str(numList[i])) + numList[i]) % K for j in range(K)] for i in range(N)]

dp = [[0] * K for _ in range(2 ** N)]
dp[0][0] = 1

for b in range(2 ** N):
    for i in range(N):
        # i번째에 해당하는 수를 이미 사용한 경우
        if b & (1<<i): continue

        # 이전까지 나머지가 j인 경우에
        # i번째 수를 사용하면 새로운 나머지는 R[i][j]
        for j in range(K):
            dp[b|(1<<i)][R[i][j]] += dp[b][j]

possible = dp[2 ** N - 1][0]
total = math.factorial(N)

divide = math.gcd(total, possible)
print("%d/%d" % (possible//divide, total//divide))