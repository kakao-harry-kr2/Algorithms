import sys
input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
incomings = [[] for _ in range(N+1)]
outgoings = [[] for _ in range(N+1)]

for _ in range(M):
    A, B, C = map(int, input().split())
    outgoings[A].append((B, C))
    incomings[B].append((A, C))

dist = [2 * INF] * (N+1)
dist[1] = 0

def BellmanFord(start):
    # distance initialization (distance for k=1)
    for i in outgoings[start]:
        dist[i[0]] = i[1]

    # k번의 edges를 지나는 최단 경로
    for k in range(2, N+1):
        # 출발 도시를 제외한 u번째 도시에 대해서
        for u in range(1, N+1):
            # u로 들어가는 i번째 도시에 대해서
            for i in incomings[u]:
                # i를 거쳐서 가는 경우가 더 최단경로인 경우 업데이트
                if dist[i[0]] < INF and dist[u] > dist[i[0]] + i[1]:
                    # N번의 edges를 이용해서 최단 경로가 생성된다면, negative cycle 존재
                    if k == N:
                        print(-1)
                        exit()
                    else:
                        dist[u] = dist[i[0]] + i[1]

BellmanFord(1)

for i in range(2, N+1):
    print(dist[i] if dist[i] < INF else -1)