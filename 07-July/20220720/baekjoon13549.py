import heapq

N, K = map(int, input().split())

INF = 10 ** 6

dist = [INF] * 100001
dist[N] = 0

q = [(0, N)]
while q:
    t, now = heapq.heappop(q)
    if now == K:
        print(t)
        exit()

    if now != 0:
        if t + 1 < dist[now-1]:
            dist[now-1] = t + 1
            heapq.heappush(q, (t+1, now-1))
    if now != 100000:
        if t + 1 < dist[now+1]:
            dist[now+1] = t + 1
            heapq.heappush(q, (t+1, now+1))
    if now <= 50000:
        if t < dist[now*2]:
            dist[now*2] = t
            heapq.heappush(q, (t, now * 2))