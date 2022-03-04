# 미확인 도착지

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

T = int(input())

def dijkstra(distance, start):
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    dest = [int(input()) for _ in range(t)]

    distance1 = [INF] * (n + 1)
    dijkstra(distance1, s)
    
    distance2 = [INF] * (n + 1)
    dijkstra(distance2, g)

    distance3 = [INF] * (n + 1)
    dijkstra(distance3, h)

    li = []
    for des in dest:
        if distance1[des] == distance1[g] + distance2[h] + distance3[des]:
            li.append(des)
        elif distance1[des] == distance1[h] + distance3[g] + distance2[des]:
            li.append(des)
    
    print(*sorted(li))