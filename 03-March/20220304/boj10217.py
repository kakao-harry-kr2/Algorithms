# KCM Travel

import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

for _ in range(T):
    N, M, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(K):
        u, v, c, d = map(int, input().split())
        graph[u].append((v, c, d))

    # dp[i][j] : i번째 노드까지 j만큼의 비용을 통해서 갈수있는 최소 시간
    dp = [[INF] * (M + 1) for _ in range(N + 1)]
    dp[1][0] = 0

    # cost를 먼저 처리해야함
    # node를 먼저 처리하면 다른 경로를 생각할 수가 없음
    for cost in range(M):
        for now in range(N):
            if dp[now][cost] != INF:
                for j in graph[now]:
                    if cost + j[1] <= M:
                        dp[j[0]][cost + j[1]] = min(dp[j[0]][cost + j[1]], dp[now][cost] + j[2])
    
    answer = min(dp[N])

    print(answer if answer != INF else 'Poor KCM')