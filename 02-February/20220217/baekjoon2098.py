# 외판원 순회

import sys
input = sys.stdin.readline

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# dp[i][j] : 현재 i번째 도시에 존재하고 j를 2진수로 바꾸고나면
# 1인 자리는 이미 방문한 도시
# 0인 자리는 방문하지 않은 도시
dp = [[-1] * (2 ** N) for _ in range(N)]

# 10진수를 N자리 2진수로
def ten2two(ten):
    global N
    two = [False] * N
    for i in reversed(range(N)):
        if ten % 2 == 1:
            two[i] = True
        ten //= 2

    return two

def two2ten(two):
    global N
    ten = 0
    for i in range(N):
        if two[i]:
            ten += 2 ** (N - i - 1)
    
    return ten

def travel(dp, i, ten):
    global N

    if dp[i][ten] != -1:
        return dp[i][ten]

    two = ten2two(ten)
    
    answer = 16000000

    for j in range(N):
        # j번째 도시에 방문하지 않은 경우
        if not two[j] and W[i][j] != 0:
            two[j] = True
            assigned_ten = two2ten(two)
            if assigned_ten == 2 ** N - 1:
                dp[j][assigned_ten] = W[j][0] if W[j][0] != 0 else 10000
            ans = travel(dp, j, assigned_ten) + W[i][j]
            if ans < answer:
                answer = ans
            two[j] = False
    
    dp[i][ten] = answer

    return answer

travel(dp, 0, 2 ** (N-1))

print(dp[0][2 ** (N-1)])