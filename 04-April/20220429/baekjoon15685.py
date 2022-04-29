# 00:47:45

def rotate(table):
    ret = [[False] * 101 for _ in range(101)]
    for r in range(101):
        for c in range(101):
            ret[c][100-r] = table[r][c]
    
    return ret

N = int(input())

generation = [set() for _ in range(11)]
points = [None for _ in range(11)]

generation[0].add((0, 0))
generation[0].add((1, 0))
points[0] = [(0, 0), (1, 0)]

for i in range(10):
    X, Y = points[i][1]
    X_PLUS_Y = X + Y
    Y_MINUS_X = Y - X
    for x, y in generation[i]:
        generation[i+1].add((x, y))
        generation[i+1].add((X_PLUS_Y-y, Y_MINUS_X+x))
    
    points[i+1] = [points[i][0], (X_PLUS_Y-points[i][0][0], Y_MINUS_X+points[i][0][1])]

table = [[False] * 101 for _ in range(101)]

for _ in range(N):
    x, y, d, g = map(int, input().split())
    for _ in range(d):
        y, x = x, 100-y
        table = rotate(table)
    
    for i, j in generation[g]:
        table[y+j][x+i] = True

    for _ in range(4-d):
        table = rotate(table)

answer = 0
for i in range(100):
    for j in range(100):
        if table[i][j] and table[i][j+1] and table[i+1][j] and table[i+1][j+1]:
            answer += 1

print(answer)