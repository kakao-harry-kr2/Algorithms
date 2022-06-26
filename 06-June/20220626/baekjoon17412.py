from collections import deque
import sys
input = sys.stdin.readline
INF = 10 ** 9

N, P = map(int, input().split())

capacity = [[0] * N for _ in range(N)]
for _ in range(P):
    u, v = map(int, input().split())
    capacity[u-1][v-1] = 1

flow = [[0] * N for _ in range(N)]

def MaximumFlow(source, sink):
    total_flow = 0

    while True:
        parent = [-1] * N
        q = deque()

        parent[source] = source
        q.append(source)

        while q and parent[sink] == -1:
            here = q.popleft()

            for there in range(N):
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