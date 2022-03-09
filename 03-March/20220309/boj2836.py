# 수상 택시

import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

q = []
for _ in range(N):
    x, y = map(int, input().split())
    # 정방향으로 가는 사람은 고려할 필요 X
    if x <= y:
        continue
    
    # 역방향으로 가는 사람은 스위핑 기법으로 처리
    heapq.heappush(q, (y, x))

answer = 0
tmp_left, tmp_right = heapq.heappop(q)

while q:
    left, right = heapq.heappop(q)
    # 다음 선분이 이어지는 경우
    if left <= tmp_right:
        tmp_right = max(tmp_right, right)
    
    # 다음 선분이 이어지지 않는 경우
    else:
        answer += tmp_right - tmp_left
        tmp_left, tmp_right = left, right

answer += tmp_right - tmp_left

print(M + 2 * answer)