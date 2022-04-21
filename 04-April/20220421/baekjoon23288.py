def search(x, y, visited, val):
    global N, M
    visited[x][y] = True
    count = 1
    for move_x, move_y in move:
        next_x, next_y = x + move_x, y + move_y
        if 0 <= next_x < N and 0 <= next_y < M and not visited[next_x][next_y] and table[next_x][next_y] == val:
            count += search(next_x, next_y, visited, val)
    return count

N, M, K = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]
top, right, down = 1, 3, 5
direction = 3 # Up/Left/Down/Right 반시계방향
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]

score_table = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        visited = [[False] * M for _ in range(N)]
        score_table[i][j] = table[i][j] * search(i, j, visited, table[i][j])

x, y = 0, 0
score = 0
for _ in range(K):
    """ step 1 """
    next_x, next_y = x + move[direction][0], y + move[direction][1]
    if 0 <= next_x < N and 0 <= next_y < M:
        x, y = x + move[direction][0], y + move[direction][1]
    else:
        x, y = x - move[direction][0], y - move[direction][1]
        direction = (direction+2) % 4
    
    if direction == 0: # Up
        top, down = down, 7 - top
    elif direction == 1: # Left
        top, right = right, 7 - top
    elif direction == 2: # Down
        top, down = 7 - down, top
    elif direction == 3: # Right
        top, right = 7 - right, top

    """ step 2 """
    score += score_table[x][y]

    """ step 3 """
    A = 7 - top
    B = table[x][y]

    if A > B:
        direction = (direction + 3) % 4
    elif A < B:
        direction = (direction + 1) % 4

print(score)