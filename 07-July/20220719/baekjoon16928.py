from collections import deque

N, M = map(int, input().split())

node2node = [node for node in range(101)]

for _ in range(N):
    x, y = map(int, input().split())
    node2node[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    node2node[u] = v

# bfs
visited = [False] * 101

visited[1] = True
q = deque([(0, 1)])

while q:
    cnt, now = q.popleft()
    
    for next in [now + j for j in range(1, 7)]:
        next = node2node[next]
        if next == 100:
            print(cnt+1)
            exit()

        if not visited[next]:
            visited[next] = True
            q.append((cnt+1, next))