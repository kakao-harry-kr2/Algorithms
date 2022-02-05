# 부분합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numList = list(map(int, input().split()))

answer = N+1
i, j = 0, 0

# i번째 숫자부터 j번째 숫자까지의 합
value = numList[0]

while True:
    if value >= S:
        answer = min(answer, j+1-i)
        value -= numList[i]
        i += 1
    else:
        j += 1
        if j == N:
            break
        value += numList[j]

print(answer if answer != N+1 else 0)