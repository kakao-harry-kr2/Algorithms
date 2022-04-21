move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
prop = [(2, 3), (2, 3), (0, 1), (0, 1)]

def matrix_sum(mat1, mat2):
    global R, C
    for i in range(R):
        for j in range(C):
            mat1[i][j] += mat2[i][j]

def propagate(diff, x, y, d, strength):
    # 온도 증가 정보 저장
    diff[x][y] = strength
    if strength == 1:
        return

    # 원래의 방향으로 전파
    if possible[x][y][d]:
        propagate(diff, x+move[d][0], y+move[d][1], d, strength-1)
    
    # 대각선으로의 전파
    for p in prop[d]:
        if possible[x][y][p]:
            next_x, next_y = x + move[p][0], y + move[p][1]
            if possible[next_x][next_y][d]:
                propagate(diff, next_x+move[d][0], next_y+move[d][1], d, strength-1)

# (x, y)위치에 있고, 방향이 direction
def heat(x, y, direction):
    global R, C

    # 온도 증가의 강도가 5인 좌표
    sx, sy = x + move[direction][0], y + move[direction][1]

    diff = [[0] * C for _ in range(R)]
    propagate(diff, sx, sy, direction, 5)

    return diff

def adjust_temperature(temperature):
    global R, C

    diff = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            # 오른쪽 체크
            if possible[i][j][0]:
                diff_val = temperature[i][j] - temperature[i][j+1]
                val = abs(diff_val) // 4
                diff[i][j] += val if diff_val < 0 else -val
                diff[i][j+1] += val if diff_val > 0 else -val
            
            # 아래쪽 체크
            if possible[i][j][3]:
                diff_val = temperature[i][j] - temperature[i+1][j]
                val = abs(diff_val) // 4
                diff[i][j] += val if diff_val < 0 else -val
                diff[i+1][j] += val if diff_val > 0 else -val
            
    return diff

R, C, K = map(int, input().rstrip().split())

# heater[i] : i방향의 heater들의 좌표
heater = [[] for _ in range(4)]
# 온도를 조사해야 하는 칸
check = []

table = [list(map(int, input().split())) for _ in range(R)]
for i in range(R):
    for j in range(C):
        if 1 <= table[i][j] <= 4:
            heater[table[i][j]-1].append((i, j))
        
        if table[i][j] == 5:
            check.append((i, j))

W = int(input())
# possible[i][j] : 우/좌/상/하로의 움직임이 가능한가?
possible = [[[True] * 4 for _ in range(C)] for _ in range(R)]
for i in range(R):
    possible[i][0][1] = False
    possible[i][-1][0] = False
for j in range(C):
    possible[0][j][2] = False
    possible[-1][j][3] = False

for _ in range(W):
    x, y, t = map(int, input().split())
    if t == 0:
        possible[x-1][y-1][2] = False
        possible[x-2][y-1][3] = False
    elif t == 1:
        possible[x-1][y-1][0] = False
        possible[x-1][y][1] = False

eat_chocolate = 0
temperature = [[0] * C for _ in range(R)]
while True:
    """ step 1 """
    for i in range(4):
        for x, y in heater[i]:
            diff = heat(x, y, i)
            matrix_sum(temperature, diff)
    
    """ step 2 """
    diff = adjust_temperature(temperature)
    matrix_sum(temperature, diff)

    """ step 3 """
    for i in range(R):
        temperature[i][0] = max(0, temperature[i][0] - 1)
        temperature[i][-1] = max(0, temperature[i][-1] - 1)
    for j in range(1, C-1):
        temperature[0][j] = max(0, temperature[0][j] - 1)
        temperature[-1][j] = max(0, temperature[-1][j] - 1)

    """ step 4 """
    eat_chocolate += 1

    """ step 5 """
    stop = True
    for x, y in check:
        if temperature[x][y] < K:
            stop = False
            break
    
    if stop:
        break

    if eat_chocolate > 100:
        break

print(eat_chocolate)