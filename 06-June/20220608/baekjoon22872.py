p2idx = {(1, 2, 3): 0, (1, 3, 2): 1, (2, 1, 3): 2, (2, 3, 1): 3, (3, 1, 2): 4, (3, 2, 1): 5}
t2idx = {(0, 0, 0): 0, (0, 0, 1): 1, (0, 1, 0): 2, (0, 1, 1): 3, (1, 0, 0): 4, (1, 0, 1): 5, (1, 1, 0): 6, (1, 1, 1): 7}

# dp[n][(p1, p2, p3)][(t1, t2, t3)][cnt(숫자), ans]
dp = [[[[None, None] for _ in range(8)] for _ in range(6)] for _ in range(27)]
dp[0] = [[[0, ""] for _ in range(8)] for _ in range(6)]
dp[1] = [[[1, "1 3\n"]] * 8, [[1, "1 2\n"]] * 8, [[1, "2 3\n"]] * 8, [[1, "2 1\n"]] * 8, [[1, "3 2\n"]] * 8, [[1, "3 1\n"]] * 8]

def solution_impl(n, p1, p2, p3, t1, t2, t3):
    cnt, ans = 0, ""
    
    # 옮기기 전과 후의 순서가 동일할 때
    # n-1개에 대한 subproblem
    if t1 == t3:
        # n-1개에 대한 subproblem을 p1 -> p2로 이동
        if dp[n-1][p2idx[(p1, p3, p2)]][t2idx[(t1^1, t3, t2)]][0] == None:
            solution_impl(n-1, p1, p3, p2, t1^1, t3, t2)
        cnt += dp[n-1][p2idx[(p1, p3, p2)]][t2idx[(t1^1, t3, t2)]][0]
        ans += dp[n-1][p2idx[(p1, p3, p2)]][t2idx[(t1^1, t3, t2)]][1]
        
        # 가장 밑에 있는 수를 p1 -> p3로 이동
        cnt += 1
        ans += str(p1) + ' ' + str(p3) + '\n'

        # n-1개에 대한 subproblem을 p2 -> p3로 이동
        if dp[n-1][p2idx[(p2, p1, p3)]][t2idx[(t2, t1, t3^1)]][0] == None:
            solution_impl(n-1, p2, p1, p3, t2, t1, t3^1)
        cnt += dp[n-1][p2idx[(p2, p1, p3)]][t2idx[(t2, t1, t3^1)]][0]
        ans += dp[n-1][p2idx[(p2, p1, p3)]][t2idx[(t2, t1, t3^1)]][1]
    
    # 옮기기 전과 후의 순서가 바뀔 때
    # n-2개에 대한 subproblem
    else:
        if dp[n-2][p2idx[(p1, p3, p2)]][t2idx[(t1, t3, t2)]][0] == None:
            solution_impl(n-2, p1, p3, p2, t1, t3, t2)
        cnt += dp[n-2][p2idx[(p1, p3, p2)]][t2idx[(t1, t3, t2)]][0]
        ans += dp[n-2][p2idx[(p1, p3, p2)]][t2idx[(t1, t3, t2)]][1]

        cnt += 2
        ans += (str(p1) + ' ' + str(p3) + '\n') * 2

        if dp[n-2][p2idx[(p2, p1, p3)]][t2idx[(t2, t1, t3)]][0] == None:
            solution_impl(n-2, p2, p1, p3, t2, t1, t3)
        cnt += dp[n-2][p2idx[(p2, p1, p3)]][t2idx[(t2, t1, t3)]][0]
        ans += dp[n-2][p2idx[(p2, p1, p3)]][t2idx[(t2, t1, t3)]][1]

    dp[n][p2idx[(p1, p2, p3)]][t2idx[(t1, t2, t3)]] = [cnt, ans]

# N = int(input())

for N in range(1, 27):
    solution_impl(N, 1, 2, 3, 0, 0, 0)
    print(dp[N][0][0][0])
# print(dp[N][0][0][1])