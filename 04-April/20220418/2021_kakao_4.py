INF = 10 ** 9

def solution(n, s, a, b, fares):
    answer = INF

    dist = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dist[i][i] = 0
    
    for c, d, f in fares:
        dist[c][d] = f
        dist[d][c] = f
    
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    for node in range(1, n + 1):
        answer = min(answer, dist[s][node] + dist[node][a] + dist[node][b])

    return answer