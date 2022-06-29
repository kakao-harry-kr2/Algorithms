from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9

# 정점의 수 & 간선의 수
N, P = map(int, input().split())

# capacity[u][v]: u -> v의 간선에 최대로 흘려보낼수 있는 유량
# i로 들어오는 간선 -> i / i에서 나가는 간선 -> N + i
capacity = [[0] * (2*N) for _ in range(2*N)]
for _ in range(P):
    u, v = map(lambda x: int(x)-1, input().split())
    capacity[N+u][v] = 1
    capacity[N+v][u] = 1

# 1,2번 노드는 여러번 이동할 수 있음
capacity[0][N] = capacity[N][0] = capacity[1][N+1] = capacity[N+1][1] = N

# 나머지 노드는 1번만 이동할 수 있음
for i in range(2, N):
    capacity[i][N+i] = 1
    capacity[N+i][i] = 1

# flow[u][v]: u -> v의 간선에 실제로 흐르는 유량
flow = [[0] * (2*N) for _ in range(2*N)]

def MaximumFlow(source, sink):
    total_flow = 0

    while True:
        # 경로의 역추적을 위해서 이전 정점을 기록
        parent = [-1] * (2*N)
        q = deque()

        parent[source] = source
        q.append(source)

        while q and parent[sink] == -1:
            here = q.popleft()

            for there in range(2*N):
                if capacity[here][there] - flow[here][there] > 0 and parent[there] == -1:
                    q.append(there)
                    parent[there] = here
    
        if parent[sink] == -1:
            break
        
        amount = INF

        p = sink
        while p != source:
            amount = min(capacity[parent[p]][p] - flow[parent[p]][p], amount)
            p = parent[p]
        
        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
            p = parent[p]
        
        total_flow += amount
    
    return total_flow

print(MaximumFlow(0, N+1))