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

dist = [INF] * (N+1)
start = 1
dist[start] = 0

def BellmanFord(start):
    # distance initialization (distance for k=1)
    for i in outgoings[start]:
        dist[i[0]] = i[1]
    
    # k번의 edges를 지나는 최단 경로
    for k in range(2, N):
        for u in range(1, N+1):
            # 경로의 합이 음수가 되는 cycle이 없다는 가정하에
            if u != start and len(incomings[u]) > 0:
                for i in incomings[u]:
                    # 경로의 길이를 1 증가시켰을 때 업데이트
                    if dist[u] > dist[i[0]] + i[1]:
                        dist[u] = dist[i[0]] + i[1]

BellmanFord(start)