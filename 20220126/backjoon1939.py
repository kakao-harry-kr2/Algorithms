from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
table = [[] for _ in range(N+1)]
max_weight = 0

# 연결 리스트
for _ in range(M):
    A, B, C = map(int, input().rstrip().split())
    table[A] += [(B, C)]
    table[B] += [(A, C)]
    max_weight = max(max_weight, C)

start_point, end_point = map(int, input().rstrip().split())

# weight 이하의 무게로 통과를 할 수 있는가?
def bfs(min_weight):
    global start_point, end_point
    queue = deque([start_point])
    visited = [False] * (N+1)
    visited[start_point] = True

    while queue:
        point = queue.popleft()
        if point == end_point:
            return 1

        for next_point, weight in table[point]:
            if visited[next_point] == False and weight >= min_weight:
                queue.append(next_point)
                visited[next_point] = True
    
    return 0

start, end = 0, max_weight
answer = 0

while start <= end:
    mid = (start + end) // 2

    if bfs(mid):
        answer = mid
        start = mid + 1
    else:
        end = mid - 1

print(int(answer))