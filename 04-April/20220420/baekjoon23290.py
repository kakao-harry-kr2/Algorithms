M, S = map(int, input().rstrip().split())
table = [[[[0] * 8 for _ in range(4)] for _ in range(4)] for _ in range(S+1)]

for _ in range(M):
    x, y, d = map(int, input().rstrip().split())
    table[0][x-1][y-1][d-1] += 1

shark_x, shark_y = map(lambda x: int(x) - 1, input().rstrip().split())
smell = [[] for _ in range(S+1)] # smell[i] : i번째 연습에서 만들어진 물고기의 냄새

move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
shark_move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
for p_idx in range(S):
    """ step 2 : 물고기들 한칸 이동 """
    # 이동할 수 있는 곳을 먼저 찾자
    possible = [[True] * 4 for _ in range(4)]
    # 상어가 있거나
    possible[shark_x][shark_y] = False
    # 물고기의 냄새가 있거나
    for sx, sy in smell[p_idx-2]:
        possible[sx][sy] = False
    for sx, sy in smell[p_idx-1]:
        possible[sx][sy] = False

    for i in range(4):
        for j in range(4):
            # k방향에 있는 물고기
            for k in range(8):
                # 이동할 수 있는 방향 찾기
                moving = False
                for rotate in range(8):
                    next_i, next_j = i + move[(k-rotate+8)%8][0], j + move[(k-rotate+8)%8][1]
                    if 0 <= next_i < 4 and 0 <= next_j < 4 and possible[next_i][next_j]:
                        table[p_idx+1][next_i][next_j][(k-rotate+8)%8] += table[p_idx][i][j][k]
                        moving = True
                        break
                # 이동하지 않았을 때
                if not moving:
                    table[p_idx+1][i][j][k] += table[p_idx][i][j][k]
    
    """ step 3 : 상어의 이동 """
    max_count = -1 # 제거한 물고기들의 최댓값
    max_move = [] # 이동 경로
    for i in range(4):
        for j in range(4):
            for k in range(4):
                count = 0
                next_x, next_y = shark_x, shark_y
                visited = [[False] * 4 for _ in range(4)]
                for direction in [i, j, k]:
                    next_x, next_y = next_x + shark_move[direction][0], next_y + shark_move[direction][1]
                    if not (0 <= next_x < 4 and 0 <= next_y < 4):
                        count = -1
                        break
                    count += sum(table[p_idx+1][next_x][next_y]) if not visited[next_x][next_y] else 0
                    visited[next_x][next_y] = True
                if count > max_count:
                    max_count = count
                    max_move = [i, j, k]
    
    next_x, next_y = shark_x, shark_y
    for direction in max_move:
        next_x, next_y = next_x + shark_move[direction][0], next_y + shark_move[direction][1]
        if sum(table[p_idx+1][next_x][next_y]) > 0:
            smell[p_idx].append((next_x, next_y))
        for k in range(8):
            table[p_idx+1][next_x][next_y][k] = 0
    
    shark_x, shark_y = next_x, next_y
    
    """ step 5 : 물고기 복제 완료 """
    for i in range(4):
        for j in range(4):
            for k in range(8):
                table[p_idx+1][i][j][k] += table[p_idx][i][j][k]

answer = 0

for i in range(4):
    for j in range(4):
        answer += sum(table[S][i][j])

print(answer)