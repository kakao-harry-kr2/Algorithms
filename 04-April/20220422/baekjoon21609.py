move = [(0, -1), (-1, 0), (0, 1), (1, 0)] # LURD

def fallDown(table):
    global N
    for j in range(N):
        for i in reversed(range(N-1)):
            if table[i][j] != None and table[i][j] >= 0 and table[i+1][j] == None:
                dest_i = i
                while dest_i + 1 < N and table[dest_i+1][j] == None:
                    dest_i += 1
                table[dest_i][j] = table[i][j]
                table[i][j] = None
    
    return table

def rotate_ccw(table):
    global N
    ret_table = [[None] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            ret_table[N-1-c][r] = table[r][c]

    return ret_table

def bfs(x, y, visited, val, group:list):
    global N
    visited[x][y] = True
    group.append((x, y))
    for i in range(4):
        next_x, next_y = x + move[i][0], y + move[i][1]
        if 0 <= next_x < N and 0 <= next_y < N:
            if not visited[next_x][next_y] and (table[next_x][next_y] in [0, val]):
                bfs(next_x, next_y, visited, val, group)

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

score = 0
while True:
    """ step 1 """
    visited = [[False] * N for _ in range(N)]
    groups = []
    rainbowColors = [(i, j) for i in range(N) for j in range(N) if table[i][j] == 0]
    for i in range(N):
        for j in range(N):
            if table[i][j] != None and table[i][j] > 0 and not visited[i][j]:
                group = []
                bfs(i, j, visited, table[i][j], group)
                groups.append(group)
                # 무지개 블록은 재방문 가능
                for x, y in rainbowColors:
                    visited[x][y] = False
    
    max_len_group = []
    for group in groups:
        if len(group) > len(max_len_group):
            max_len_group = group
        elif len(group) == len(max_len_group):
            group_count = 0
            for i, j in group:
                if table[i][j] == 0:
                    group_count += 1
            max_len_group_count = 0
            for i, j in max_len_group:
                if table[i][j] == 0:
                    max_len_group_count += 1
            if group_count > max_len_group_count:
                max_len_group = group
            elif group_count == max_len_group_count:
                if group[0][0] > max_len_group[0][0]:
                    max_len_group = group
                elif group[0][0] == max_len_group[0][0]:
                    if group[0][1] > max_len_group[0][1]:
                        max_len_group = group

    """ step 2 """
    if len(max_len_group) < 2:
        break

    for i, j in max_len_group:
        table[i][j] = None

    score += len(max_len_group) ** 2

    """ step 3 """
    table = fallDown(table)

    """ step 4 """
    table = rotate_ccw(table)

    """ step 5 """
    table = fallDown(table)

print(score)