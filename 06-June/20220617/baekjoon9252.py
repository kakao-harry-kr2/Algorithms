s1 = input().rstrip()
s2 = input().rstrip()

dp = [[[0, (-1, -1)] for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(len(s1)):
    for j in range(len(s2)):
        if s1[i] == s2[j]:
            prev1 = dp[i][j-1][0]
            prev2 = dp[i-1][j][0]
            prev3 = dp[i-1][j-1][0] + 1

            if prev1 == max(prev1, prev2, prev3):
                dp[i][j] = [dp[i][j-1][0], (i, j-1)]
            elif prev2 == max(prev1, prev2, prev3):
                dp[i][j] = [dp[i-1][j][0], (i-1, j)]
            else:
                dp[i][j] = [dp[i-1][j-1][0]+1, (i-1, j-1)]

        else:
            if dp[i-1][j][0] < dp[i][j-1][0]:
                dp[i][j] = [dp[i][j-1][0], (i, j-1)]
            else:
                dp[i][j] = [dp[i-1][j][0], (i-1, j)]

print(dp[len(s1)-1][len(s2)-1][0])

now = (len(s1)-1, len(s2)-1)
answer = ""
while now[0] >= 0 and now[1] >= 0:
    prev = dp[now[0]][now[1]][1]
    if now[0] == prev[0]+1 and now[1] == prev[1]+1:
        answer += s1[now[0]]
    
    now = prev

print(answer[::-1])