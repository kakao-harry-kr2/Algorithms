# 숨바꼭질 4
from collections import deque

N, K = map(int, input().split())

# BFS을 위한 queue 초기화
queue = deque()
# 중복 체크를 방지하기 위해 방문기록 체크
visited = [False] * 100001
# memory : 이전 위치를 표시
memory = [None] * 100001

queue.append((0, N))
visited[N] = True

while queue:
    count, now = queue.popleft()

    # 동생을 찾은 경우
    if now == K:
        print(count)
        break

    next1 = now - 1
    next2 = now + 1
    next3 = now * 2

    for next in [next1, next2, next3]:
        if 0 <= next <= 100000 and not visited[next]:
            queue.append((count+1, next))
            visited[next] = True
            memory[next] = now

moveList = [K]
now = K
while now != N:
    prev = memory[now]
    moveList.append(prev)
    now = prev

print(*moveList[::-1])