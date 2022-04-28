# 1:06:30

R, C, M = map(int, input().split())
table = [[[[] for _ in range(C)] for _ in range(R)] for _ in range(C+1)]
move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
back = [1, 0, 3, 2]
for idx in range(M):
    r, c, s, d, z = map(int, input().split())
    if d in [1, 2]:
        s %= 2*(R-1)
    else:
        s %= 2*(C-1)
    table[0][r-1][c-1] = (s, d-1, z)

count = 0
for idx in range(C):
    for i in range(R):
        if table[idx][i][idx]:
            count += table[idx][i][idx][2]
            table[idx][i][idx] = None
            break

    for i in range(R):
        for j in range(C):
            if table[idx][i][j]:
                s, d, z = table[idx][i][j]
                next_i, next_j = i + s * move[d][0], j + s * move[d][1]
                
                while not 0 <= next_i < R:
                    d = back[d]
                    if next_i < 0:
                        next_i = -next_i
                    else:
                        next_i = 2 * R - 2 - next_i
                
                while not 0 <= next_j < C:
                    d = back[d]
                    if next_j < 0:
                        next_j = -next_j
                    else:
                        next_j = 2 * C - 2 - next_j

                table[idx+1][next_i][next_j].append((s, d, z))
    
    for i in range(R):
        for j in range(C):
            if len(table[idx+1][i][j]) == 0:
                table[idx+1][i][j] = None
            elif len(table[idx+1][i][j]) == 1:
                table[idx+1][i][j] = table[idx+1][i][j][0]
            else:
                max_shark = (0, 0, 0)
                for s, d, z in table[idx+1][i][j]:
                    if z > max_shark[2]:
                        max_shark = (s, d, z)
                table[idx+1][i][j] = max_shark
    
    # for i in range(R):
    #     for j in range(C):
    #         print(table[idx+1][i][j] if table[idx+1][i][j] else '(-, -, -)', end=' ')
    #     print()
    # print()

print(count)