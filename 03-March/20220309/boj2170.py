# 선 긋기

import heapq
import sys
input = sys.stdin.readline

N = int(input())

q = []
for _ in range(N):
    x, y = map(int, input().split())
    heapq.heappush(q, (x, y))

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

print(answer)