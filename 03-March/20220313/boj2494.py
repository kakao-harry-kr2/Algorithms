# 숫자 맞추기

import sys
input = sys.stdin.readline
INF = 10 ** 5

N = int(input())
initial = input()
final = input()

total = []
for i in range(N):
    value = (int(final[i]) - int(initial[i]) + 10) % 10
    total.append(value)

dp = [[[INF, None] for _ in range(10)] for _ in range(N)]
dp[0][total[0]][0] = total[0]
dp[0][0][0] = (10 - total[0]) % 10

for i in range(N-1):
    for j in range(10):
        tmp = dp[i][j][0] + (10 + j - total[i+1]) % 10
        if tmp < dp[i+1][j][0]:
            dp[i+1][j][0] = tmp
            dp[i+1][j][1] = j
        
        tmp = dp[i][j][0] + (10 + total[i+1] - j) % 10
        if tmp < dp[i+1][total[i+1]][0]:
            dp[i+1][total[i+1]][0] = tmp
            dp[i+1][total[i+1]][1] = j

min_index = None
min_value = INF

for j in range(10):
    if dp[N-1][j][0] < min_value:
        min_value = dp[N-1][j][0]
        min_index = j

print(dp[N-1][min_index][0])

now = min_index

backtrack = []
for i in reversed(range(1, N)):
    next = dp[i][now][1]
    if next == now:
        backtrack.append(dp[i-1][next][0] - dp[i][now][0])
    
    else:
        backtrack.append(dp[i][now][0] - dp[i-1][next][0])
    
    now = next

if now:
    backtrack.append(dp[0][now][0])
else:
    backtrack.append(-dp[0][0][0])
    
backtrack.reverse()

for i in range(N):
    print("%d %d" % (i+1, backtrack[i]))