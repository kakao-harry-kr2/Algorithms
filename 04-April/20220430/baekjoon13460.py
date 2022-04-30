# 01:34:40

N, M = map(int, input().split())
table = [list(input()) for _ in range(N)]
pos_history = [[] for _ in range(11)]
dir_history = [[] for _ in range(11)]

RX, RY, BX, BY = 0, 0, 0, 0
for i in range(1, N-1):
    for j in range(1, M-1):
        if table[i][j] == 'R':
            RX, RY = i, j
        if table[i][j] == 'B':
            BX, BY = i, j

pos_history[0] = [(RX, RY, BX, BY)]
table[RX][RY], table[BX][BY] = '.', '.'
dir_history[0] = [[(0, 0)]]

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for cnt in range(1, 11):
    for pos, dir in zip(pos_history[cnt-1], dir_history[cnt-1]):
        for mx, my in move:
            if (mx, my) == dir[-1]:
                continue
            
            red_in, blue_in = False, False
            rx, ry, bx, by = pos
            red_val = rx * mx + ry * my
            blu_val = bx * mx + by * my
            if red_val > blu_val:
                # R 먼저 이동
                while True:
                    if table[rx+mx][ry+my] == '#':
                        break
                    
                    if table[rx+mx][ry+my] == 'O':
                        red_in = True
                        break
                    
                    rx, ry = rx + mx, ry + my
                
                if not red_in:
                    table[rx][ry] = 'R'

                while True:
                    if table[bx+mx][by+my] in ['#', 'R']:
                        break

                    if table[bx+mx][by+my] == 'O':
                        blue_in = True
                        break
                    
                    bx, by = bx + mx, by + my
                table[rx][ry] = '.'

            else:
                # B 먼저 이동
                while True:
                    if table[bx+mx][by+my] == '#':
                        break

                    if table[bx+mx][by+my] == 'O':
                        blue_in = True
                        break
                    
                    bx, by = bx + mx, by + my
                
                if not blue_in:
                    table[bx][by] = 'B'

                if blue_in:
                    continue

                while True:
                    if table[rx+mx][ry+my] in ['#', 'B']:
                        break
                    
                    if table[rx+mx][ry+my] == 'O':
                        red_in = True
                        break
                    
                    rx, ry = rx + mx, ry + my
                table[bx][by] = '.'
            
            if red_in and not blue_in:
                print(cnt)
                exit()

            elif not blue_in:
                pos_history[cnt].append((rx, ry, bx, by))
                dir_history[cnt].append(dir + [(mx, my)])

print(-1)