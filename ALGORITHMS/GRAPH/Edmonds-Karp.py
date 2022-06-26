from collections import deque
INF = 10 ** 9

# 정점의 수 & 간선의 수
V, E = map(int, input().split())

# capacity[u][v]: u -> v의 간선에 최대로 흘려보낼수 있는 유량
capacity = [[0] * V for _ in range(V)]
for _ in range(E):
    u, v = map(int, input().split())
    capacity[u-1][v-1] = 1

# flow[u][v]: u -> v의 간선에 실제로 흐르는 유량
flow = [[0] * V for _ in range(V)]

def MaximumFlow(source, sink):
    total_flow = 0

    while True:
        # 경로의 역추적을 위해서 이전 정점을 기록
        parent = [-1] * V
        q = deque()

        parent[source] = source
        q.append(source)

        while q and parent[sink] == -1:
            here = q.popleft()

            for there in range(V):
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

print(MaximumFlow(0, 1))