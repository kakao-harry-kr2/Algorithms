# Mowing the Lawn

from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
E = [int(input()) for _ in range(N)]

summation = [E[0]]
for i in range(1, N):
    summation.append(summation[-1]+E[i])

m = deque()
dp = [0] * N
m.append([0, -1])

for i in range(N):
    while m and m[0][1] < i - K:
        m.popleft()
    
    value = dp[i-1] - summation[i]
    while m and m[-1][0] < value:
        m.pop()
    m.append([value, i])
    
    dp[i] = summation[i] + m[0][0]
    
print(dp[N-1])