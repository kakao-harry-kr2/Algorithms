# LCS 2
inputStr1 = input()
inputStr2 = input()

len1 = len(inputStr1)
len2 = len(inputStr2)

dp = [[[0, (-1, -1)]] * (len2+1) for _ in range(len1+1)]

for i in range(len1):
    for j in range(len2):
        answer = [dp[i-1][j][0], (i-1, j)]
        answer2 = [dp[i][j-1][0], (i, j-1)]

        if answer2[0] > answer[0]:
            answer = answer2

        if inputStr1[i] == inputStr2[j]:
            answer3 = [dp[i-1][j-1][0]+1, (i-1, j-1)]
            if answer3[0] > answer[0]:
                answer = answer3

        dp[i][j] = answer

print(dp[len1-1][len2-1][0])

li = ""
i, j = len1-1, len2-1
while i >= 0 and j >= 0:
    next_i, next_j = dp[i][j][1][0], dp[i][j][1][1]
    if next_i + 1 == i and next_j + 1 == j:
        li += inputStr1[i]

    i, j = next_i, next_j

print(li[::-1])