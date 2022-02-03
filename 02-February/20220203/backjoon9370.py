import heapq
import sys
input = sys.stdin.readline
INF = 2 * int(1e9)

T = int(input())

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        a, b, d = map(int, input().split())
        # 최단 경로가 여러개인 경우에는 항상 (g, h)를 지나는 경로를 선택
        if (a == g and b == h) or (a == h and b == g):
            graph[g].append((h, 2 * d - 1))
            graph[h].append((g, 2 * d - 1))
        else:
            graph[a].append((b, 2 * d))
            graph[b].append((a, 2 * d))

    finals = [int(input()) for _ in range(t)]

    distance = [INF] * (n+1)
    distance[s] = 0

    # 최단경로를 이용할 때 주어진 (g, h) 경로를 이용했는가?
    # 사실 g-h를 연결하는 경로를 이용할 때에는 distance값이 홀수가 나오고
    # 나머지의 경우에는 짝수가 나오기 때문에 나중에 홀/짝 판단만으로도
    # 특정 경로를 이용했는지 알 수 있다.
    used = [False] * (n+1)

    q = []
    heapq.heappush(q, (0, s))
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                # 만약 now -> i[0] 의 경로가 (g, h)인 경우
                if (now == g and i[0] == h) or (now == h and i[0] == g):
                    used[i[0]] = True
                # now까지 갈 때 (g, h)를 이용 -> i[0]도 이용
                else:
                    used[i[0]] = used[now]

    for final in sorted(finals):
        if distance[final] < INF and used[final] == True:
            print(final, end=' ')

    print()