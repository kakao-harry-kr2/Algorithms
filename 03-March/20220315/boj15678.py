# 연세워터파크

from collections import deque
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
numList = list(map(int, input().split()))

m = deque()
dp = [0] * N
m.append([0, -1])

for i in range(N):
    while m and m[0][1] < i - D:
        m.popleft()

    dp[i] = numList[i] + max(m[0][0], 0)

    while m and m[-1][0] < dp[i]:
        m.pop()
    
    m.append([dp[i], i])

print(max(dp))