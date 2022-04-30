# 00:18:00

from collections import deque

N = int(input())
K = int(input())
table = [[False] * N for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    table[r-1][c-1] = True

L = int(input())
direction = [0] * 10001
for _ in range(L):
    X, C = input().split()
    direction[int(X)] = -1 if C == 'L' else 1

t = 0
move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
snake = deque([(0, 0)])
dir = 0
while True:
    if direction[t] != None:
        dir = (dir + direction[t] + 4) % 4
    
    hx, hy = snake[0]
    next_hx, next_hy = hx + move[dir][0], hy + move[dir][1]

    if not 0 <= next_hx < N or not 0 <= next_hy < N or (next_hx, next_hy) in snake:
        break
    
    snake.appendleft((next_hx, next_hy))
    if table[next_hx][next_hy]:
        table[next_hx][next_hy] = False
    else:
        snake.pop()

    t += 1

print(t+1)