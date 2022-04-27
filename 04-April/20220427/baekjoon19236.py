# 1:08:07

from copy import deepcopy

def process(table, position, shark_x, shark_y, shark_dir, current):
    global answer

    """ 물고기들 이동 """
    for i in range(1, 17):
        if position[i] != None:
            x, y = position[i]
            for k in range(8):
                next_x, next_y = x + move[(table[x][y][1]+k)%8][0], y + move[(table[x][y][1]+k)%8][1]
                if 0 <= next_x < 4 and 0 <= next_y < 4 and (shark_x, shark_y) != (next_x, next_y):
                    table[x][y][1] = (table[x][y][1]+k)%8
                    table[x][y], table[next_x][next_y] = table[next_x][next_y], table[x][y]
                    if table[x][y] != None:
                        position[table[x][y][0]] = (x, y)
                    if table[next_x][next_y] != None:
                        position[table[next_x][next_y][0]] = (next_x, next_y)
                    break
    
    """ 상어 이동 """
    going = False
    for i in range(1, 4):
        shark_next_x, shark_next_y = shark_x + i * move[shark_dir][0], shark_y + i * move[shark_dir][1]
        if not (0 <= shark_next_x < 4 and 0 <= shark_next_y < 4):
            break
        
        if table[shark_next_x][shark_next_y] == None:
            continue
        
        going = True
        fish_idx, fish_dir = table[shark_next_x][shark_next_y]
        table[shark_next_x][shark_next_y] = None
        position[fish_idx] = None

        new_table = deepcopy(table)
        new_position = deepcopy(position)
        process(new_table, new_position, shark_next_x, shark_next_y, fish_dir, current+fish_idx)

        position[fish_idx] = (shark_next_x, shark_next_y)
        table[shark_next_x][shark_next_y] = [fish_idx, fish_dir]
    
    if not going and current > answer:
        answer = current

move = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
table = [[None for _ in range(4)] for _ in range(4)]
position = [None] * 17
for i in range(4):
    inputList = list(map(int, input().split()))
    for j in range(4):
        table[i][j] = [inputList[2*j], inputList[2*j+1]-1]
        position[inputList[2*j]] = (i, j)

idx, dir = table[0][0]
table[0][0] = None
position[idx] = None
shark_x, shark_y, shark_dir = 0, 0, dir

answer, current = 0, idx
process(table, position, shark_x, shark_y, shark_dir, current)

print(answer)