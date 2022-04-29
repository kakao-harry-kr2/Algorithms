# 00:20:00

N, M, x, y, K = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

command = list(map(int, input().split()))

top, bottom, up, down, left, right = 0, 0, 0, 0, 0, 0
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
for cmd in command:
    next_x, next_y = x + move[cmd-1][0], y + move[cmd-1][1]
    if not (0 <= next_x < N and 0 <= next_y < M):
        continue

    x, y = next_x, next_y

    if cmd == 1:
        top, left, bottom, right = left, bottom, right, top
    elif cmd == 2:
        top, left, bottom, right = right, top, left, bottom
    elif cmd == 3:
        top, down, bottom, up = down, bottom, up, top
    else:
        top, down, bottom, up = up, top, down, bottom
    
    print(top)

    if table[x][y] == 0:
        table[x][y] = bottom
    else:
        bottom = table[x][y]
        table[x][y] = 0