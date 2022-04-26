N, M, k = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]
direction = list(map(lambda x: int(x)-1, input().split()))
priority = [[list(map(lambda x: int(x)-1, input().split())) for _ in range(4)] for _ in range(M)]
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
smell = [[(-k, -1) for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if table[i][j] > 0:
            smell[i][j] = (0, table[i][j]-1)

position = [None] * M
for i in range(N):
    for j in range(N):
        if table[i][j] > 0:
            position[table[i][j]-1] = (i, j)

for idx in range(1001):
    if position.count(None) == M - 1:
        print(idx)
        exit()
    
    smell_plus = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(M):
        if position[i] != None:
            x, y = position[i]
            going = False
            for d in priority[i][direction[i]]:
                next_x, next_y = x + move[d][0], y + move[d][1]
                if not (0 <= next_x < N and 0 <= next_y < N):
                    continue
                
                if smell[next_x][next_y][0] <= idx - k:
                    direction[i] = d
                    position[i] = (next_x, next_y)
                    smell_plus[next_x][next_y].append(i)
                    going = True
                    break
            if not going:
                for d in priority[i][direction[i]]:
                    next_x, next_y = x + move[d][0], y + move[d][1]
                    if not (0 <= next_x < N and 0 <= next_y < N):
                        continue

                    if smell[next_x][next_y][1] == i:
                        direction[i] = d
                        position[i] = (next_x, next_y)
                        smell_plus[next_x][next_y].append(i)
                        break
    
    for i in range(N):
        for j in range(N):
            if len(smell_plus[i][j]) == 1:
                smell[i][j] = (idx + 1, smell_plus[i][j][0])
            elif len(smell_plus[i][j]) > 1:
                for l in range(len(smell_plus[i][j])):
                    if l == 0:
                        smell[i][j] = (idx + 1, smell_plus[i][j][l])
                    else:
                        position[smell_plus[i][j][l]] = None
    
print(-1)