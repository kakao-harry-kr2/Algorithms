from collections import deque

N, K = map(int, input().split())
visited = [False] * 1000001

q = deque([(0, N)])
visited[N] = True

while q:
    count, now = q.popleft()
    if now == K:
        print(count)
        exit()
    
    next_1 = now - 1
    next_2 = now + 1
    next_3 = now * 2

    if 0 <= next_1 <= 100000 and not visited[next_1]:
        q.append((count+1, next_1))
        visited[next_1] = True
    if 0 <= next_2 <= 100000 and not visited[next_2]:
        q.append((count+1, next_2))
        visited[next_2] = True
    if 0 <= next_3 <= 100000 and not visited[next_3]:
        q.append((count+1, next_3))
        visited[next_3] = True

print(count)