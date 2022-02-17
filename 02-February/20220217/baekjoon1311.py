# 할 일 정하기 1

import sys
input = sys.stdin.readline

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]

# dp[i] : i를 2진수로 바꾸었을 때
# 1인 자리는 일이 분배된 자리이고
# 0인 자리는 일이 분배되지 않음
dp = [-1] * (2 ** N)

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

def assignJob(dp, ten):
    global N
    if dp[ten] != -1:
        return dp[ten]
    
    two = ten2two(ten)
    # 몇번째 사람이 작업을 배정받을 차례인지?
    i = two.count(True)

    # 모든 작업이 배정이 끝난 경우
    if i == N:
        return 0
    
    # dp[ten]
    answer = 200000

    for j in range(N):
        # j번째에 해당하는 작업이 배정되지 않은 경우
        if not two[j]:
            two[j] = True
            assigned_ten = two2ten(two)
            ans = assignJob(dp, assigned_ten) + D[i][j]
            if ans < answer:
                answer = ans
            two[j] = False
    
    dp[ten] = answer

    return answer

assignJob(dp, 0)

print(dp[0])