# 00:30:25

N, K = map(int, input().split())
table_color = [list(map(int, input().split())) + [2] for _ in range(N)] + [[2] * (N+1)]
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
back = [1, 0, 3, 2]
position = []
table_num = [[[] for _ in range(N)] for _ in range(N)]
for idx in range(K):
    i, j, dir = map(int, input().split())
    position.append([i-1, j-1, dir-1])
    table_num[i-1][j-1].append(idx)

count = 1
while count <= 1000:
    for idx in range(K):
        i, j = position[idx][0], position[idx][1]
        index = table_num[i][j].index(idx)
        num_set = table_num[i][j][index:]
        table_num[i][j] = list(table_num[i][j][:index]) if index != 0 else []

        next_i, next_j = (i + move[position[idx][2]][0] + N+1) % (N+1), (j + move[position[idx][2]][1] + N+1) % (N+1)
        next_table_color = table_color[next_i][next_j]

        if next_table_color == 0: # white
            for num in num_set:
                table_num[next_i][next_j].append(num)
                if len(table_num[next_i][next_j]) >= 4:
                    print(count)
                    exit()
                position[num][0], position[num][1] = next_i, next_j
        
        elif next_table_color == 1: # red
            for num in num_set[::-1]:
                table_num[next_i][next_j].append(num)
                if len(table_num[next_i][next_j]) >= 4:
                    print(count)
                    exit()
                position[num][0], position[num][1] = next_i, next_j
        
        else:
            position[idx][2] = back[position[idx][2]]
            next_i, next_j = i + move[position[idx][2]][0], j + move[position[idx][2]][1]
            next_table_color = table_color[next_i][next_j]
            if next_table_color == 0:
                for num in num_set:
                    table_num[next_i][next_j].append(num)
                    if len(table_num[next_i][next_j]) >= 4:
                        print(count)
                        exit()
                    position[num][0], position[num][1] = next_i, next_j
            
            elif next_table_color == 1:
                for num in num_set[::-1]:
                    table_num[next_i][next_j].append(num)
                    if len(table_num[next_i][next_j]) >= 4:
                        print(count)
                        exit()
                    position[num][0], position[num][1] = next_i, next_j
            
            else:
                for num in num_set:
                    table_num[i][j].append(num)
    
    count += 1

print(-1)