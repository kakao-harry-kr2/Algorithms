import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, E = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

# start = 1
distance1 = [INF] * (N+1)
# start = N
distance2 = [INF] * (N+1)
# start = v1
distance3 = [INF] * (N+1)

def dijkstra(start, distance):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(1, distance1)
dijkstra(N, distance2)
dijkstra(v1, distance3)

# 1 -> v1 -> v2 -> N
answer1 = distance1[v1] + distance3[v2] + distance2[v2]
# 1 -> v2 -> v1 -> N
answer2 = distance1[v2] + distance3[v2] + distance2[v1]

if answer1 >= INF and answer2 >= INF:
    print(-1)
else:
    print(min(answer1, answer2))