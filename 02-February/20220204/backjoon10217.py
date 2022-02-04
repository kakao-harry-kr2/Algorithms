import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    outgoings = [[] for _ in range(N+1)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        outgoings[u].append((v, c, d))

    # dp[i][j] : i번째 도시에 j만큼의 비용으로 갈수있는 최단시간
    dp = [[INF] * (M+1) for _ in range(N+1)]
    dp[1][0] = 0

    for cost in range(M):
        for now in range(N):
            if dp[now][cost] != INF:
                for j in outgoings[now]:
                    if cost + j[1] <= M:
                        dp[j[0]][cost + j[1]] = min(dp[j[0]][cost + j[1]], dp[now][cost] + j[2])

    min_time = min(dp[N])
    print(min_time if min_time != INF else "Poor KCM")