# 1로 만들기 2
N = int(input())

dp = [None] * (N+1)
dp[1] = [0, 1] # [연산횟수, 어떤 숫자로부터 만들어졌는지]

for i in range(2, N+1):
    # +1해서 만들어진 경우
    answer = [dp[i-1][0] + 1, i-1]

    # x2해서 만들어진 경우가 더 최소 연산인 경우
    if i % 2 == 0 and dp[i//2][0] + 1 < answer[0]:
        answer = [dp[i//2][0] + 1, i//2]
    
    # x3해서 만들어진 경우가 더 최소 연산인 경우
    if i % 3 == 0 and dp[i//3][0] + 1 < answer[0]:
        answer = [dp[i//3][0] + 1, i//3]

    dp[i] = answer

print(dp[N][0])

num = N
print(num, end=' ')
while num > 1:
    print(dp[num][1], end=' ')
    num = dp[num][1]