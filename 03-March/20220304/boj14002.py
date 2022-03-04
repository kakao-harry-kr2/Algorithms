# 가장 긴 증가하는 부분 수열 4

import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

dp_count = [1] * N
dp_prev = [None] * N

for i in range(1, N):
    for j in range(i):
        if numList[j] < numList[i] and dp_count[j] + 1 > dp_count[i]:
            dp_count[i] = dp_count[j] + 1
            dp_prev[i] = j

max_count = max(dp_count)
max_index = dp_count.index(max_count)

print(max_count)

li = []
while max_index != None:
    li.append(numList[max_index])
    max_index = dp_prev[max_index]

print(*li[::-1])