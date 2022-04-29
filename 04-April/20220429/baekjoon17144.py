# 00:32:15

R, C, T = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(R)]
move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
x, y = -1, -1
for i in range(R):
    for j in range(C):
        if table[i][j] == -1:
            x, y = i, j
            break
    if x > 0:
        break

next = [[[] for _ in range(C)] for _ in range(R)]
for i in range(R):
    for j in range(C):
        for k in range(4):
            next_i, next_j = i + move[k][0], j + move[k][1]
            if 0 <= next_i < R and 0 <= next_j < C and table[next_i][next_j] != -1:
                next[i][j].append((next_i, next_j))

for _ in range(T):
    """ step 1 """
    diff = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if table[i][j] > 0:
                for next_i, next_j in next[i][j]:
                    diff[next_i][next_j] += table[i][j] // 5
                table[i][j] -= len(next[i][j]) * (table[i][j] // 5)
    
    for i in range(R):
        for j in range(C):
            table[i][j] += diff[i][j]
    
    # for i in range(R):
    #     for j in range(C):
    #         print("{0:2d}".format(table[i][j]), end=' ')
    #     print()
    # print()

    """ step 2 """
    # 위쪽 공기청정기 작동
    for i in reversed(range(1, x)):
        table[i][y] = table[i-1][y]
    
    for j in range(y, C-1):
        table[0][j] = table[0][j+1]
    
    for i in range(x):
        table[i][-1] = table[i+1][-1]
    
    for j in reversed(range(y+2, C)):
        table[x][j] = table[x][j-1]
    
    table[x][y+1] = 0

    # 아래쪽 공기청정기 작동
    for i in range(x+2, R-1):
        table[i][y] = table[i+1][y]
    
    for j in range(y, C-1):
        table[-1][j] = table[-1][j+1]
    
    for i in reversed(range(x+2, R)):
        table[i][-1] = table[i-1][-1]
    
    for j in reversed(range(y+2, C)):
        table[x+1][j] = table[x+1][j-1]
    
    table[x+1][y+1] = 0

    # for i in range(R):
    #     for j in range(C):
    #         print("{0:2d}".format(table[i][j]), end=' ')
    #     print()
    # print()

answer = 2
for i in range(R):
    answer += sum(table[i])

print(answer)
