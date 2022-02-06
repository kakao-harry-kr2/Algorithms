# 가장 긴 증가하는 부분 수열 4
import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

dp = [1] * N

for i in range(1, N):
    # i번째를 고려할 때 이전 것들을 모두 고려
    for j in range(i):
        if numList[j] < numList[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

value = max(dp)
li = []
for i in range(N-1, -1, -1):
    if dp[i] == value:
        li.append(numList[i])
        value -= 1

for ans in li[::-1]:
    print(ans, end=' ')