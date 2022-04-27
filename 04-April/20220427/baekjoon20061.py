# 1:21:07

N = int(input())

green = [[False] * 4 for _ in range(6)]
blue = [[False] * 6 for _ in range(4)]

score = 0
for _ in range(N):
    t, x, y = map(int, input().split())
    """ 블록 slide """
    if t == 1: # (x, y)
        i = 2
        while i < 6 and not green[i][y]:
            i += 1
        green[i-1][y] = True
        j = 2
        while j < 6 and not blue[x][j]:
            j += 1
        blue[x][j-1] = True
    elif t == 2: # (x, y), (x, y+1)
        i = 2
        while i < 6 and not green[i][y] and not green[i][y+1]:
            i += 1
        green[i-1][y], green[i-1][y+1] = True, True
        j = 2
        while j < 6 and not blue[x][j]:
            j += 1
        blue[x][j-2], blue[x][j-1] = True, True
    elif t == 3: # (x, y), (x+1, y)
        i = 2
        while i < 6 and not green[i][y]:
            i += 1
        green[i-2][y], green[i-1][y] = True, True
        j = 2
        while j < 6 and not blue[x][j] and not blue[x+1][j]:
            j += 1
        blue[x][j-1], blue[x+1][j-1] = True, True
    
    """ green process """

    for i in range(2, 6):
        if green[i].count(True) == 4:
            for k in reversed(range(1, i+1)):
                green[k] = [green[k-1][l] for l in range(4)]
            score += 1
    
    count = 0
    for i in range(2):
        if green[i].count(True) > 0:
            count += 1
    
    for i in reversed(range(2, 6)):
        green[i] = [green[i-count][j] for j in range(4)]
    
    green[0], green[1] = [False] * 4, [False] * 4
    
    """ blue process """

    for j in range(2, 6):
        if blue[0][j] and blue[1][j] and blue[2][j] and blue[3][j]:
            for k in reversed(range(1, j+1)):
                for i in range(4):
                    blue[i][k] = blue[i][k-1]
            score += 1

    count = 0
    for j in range(2):
        if blue[0][j] or blue[1][j] or blue[2][j] or blue[3][j]:
            count += 1
    
    for j in reversed(range(2, 6)):
        for i in range(4):
            blue[i][j] = blue[i][j-count]
    
    for i in range(4):
        for j in range(2):
            blue[i][j] = False
    
print(score)

count = 0
for i in range(6):
    for j in range(4):
        if green[i][j]:
            count += 1

for i in range(4):
    for j in range(6):
        if blue[i][j]:
            count += 1

print(count)