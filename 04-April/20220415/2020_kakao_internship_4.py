import sys
sys.setrecursionlimit(10 ** 9)

INF = 10 ** 9
moveList = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# (i, j)에서 k방향에 대한 process
def process(board, dp, i, j, k):
    # k -> (i+moveList[k], j+moveList[k]) 로 + 100
    # (k+1) % 4 -> (i+moveList[(k+1)%4], j+moveList[(k+1)%4]) 로 + 600
    # (k+3) % 4 -> (i+moveList[(k+3)%4], j+moveList[(k+3)%4]) 로 + 600
    cost = [100, 600, 600]
    N = len(board)
    for idx, next_k in enumerate([k, (k+1)%4, (k+3)%4]):
        next_i, next_j = i + moveList[next_k][0], j + moveList[next_k][1]
        # 다음 도착지가 지도 내부에 있고, 벽이 아닌 경우
        if 0 <= next_i < N and 0 <= next_j < N and board[next_i][next_j] == 0:
            new_value = dp[i][j][k] + cost[idx]
            # 새로운 값이 더 적은 비용인 경우 값 업데이트 후 recursively process
            if new_value < dp[next_i][next_j][next_k]:
                dp[next_i][next_j][next_k] = new_value
                process(board, dp, next_i, next_j, next_k)

def solution(board):
    N = len(board)

    # dp[i][j][k] : (i, j)에서 moveList[k] 방향으로의 건설 비용의 최솟값
    dp = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

    dp[0][0] = [0, 0, INF, INF]

    process(board, dp, 0, 0, 0)
    process(board, dp, 0, 0, 1)

    return min(dp[N-1][N-1])

# print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
# print(solution([[0,0,0],[0,0,0],[0,0,0]]))
# print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
# print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))

print(solution([[0] * 25 for _ in range(25)]))