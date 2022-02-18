# 박성원

import math
import sys
input = sys.stdin.readline

N = int(input())
numList = [int(input()) for _ in range(N)]
K = int(input())

R = [[(j * 10 ** len(str(numList[i])) + numList[i]) % K for j in range(K)] for i in range(N)]

# dp[b][j] : 사용한 숫자를 b로 나타냈을때 나머지가 j인 경우의 수
dp = [[0] * K for _ in range(1<<N)]

# 아무것도 사용하지 않았을때 나머지 0으로 초기화
dp[0][0] = 1

for b in range(1<<N):
    for i in range(N):
        # i번째에 해당하는 수를 이미 사용한 경우
        if b & (1<<i): continue
        
        # 이전까지 나머지가 j인 경우에
        # i번째 수를 사용하면 새로운 나머지는 R[i][j]
        for j in range(K):
            dp[b|(1<<i)][R[i][j]] += dp[b][j]

p = dp[(1<<N)-1][0]
q = math.factorial(N)
g = math.gcd(p, q)

print("%d/%d" % (p//g, q//g))