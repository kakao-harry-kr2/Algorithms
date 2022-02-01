import heapq
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(M)]

result = [[0] * N for _ in range(M)]
result[0][0] = 1

x_list = [-1, 1, 0, 0]
y_list = [0, 0, -1, 1]

# Priority Queue (maxHeap)
pq = [[-table[0][0], 0, 0]]

while pq:
    now = heapq.heappop(pq)
    height, i, j = -now[0], now[1], now[2]

    if i == M-1 and j == N-1:
        print(result[i][j])
        exit()

    for k in range(4):
        next_i, next_j = i + x_list[k], j + y_list[k]
        if 0 <= next_i < M and 0 <= next_j < N and table[next_i][next_j] < table[i][j]:
            if result[next_i][next_j] == 0:
                heapq.heappush(pq, [-table[next_i][next_j], next_i, next_j])
            result[next_i][next_j] += result[i][j]

print(0)