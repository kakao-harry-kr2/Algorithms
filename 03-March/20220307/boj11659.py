# 구간 합 구하기 4

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = [0] + list(map(int, input().split()))

summation = [0] * (N + 1)

for i in range(1, N + 1):
    summation[i] = summation[i-1] + numList[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(summation[j] - summation[i-1])