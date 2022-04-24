N, M, K = map(int, input().split())
table = [[[[] for _ in range(N)] for _ in range(N)] for _ in range(K+1)]
move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    table[0][r-1][c-1].append((d, m, s))

for idx in range(K):
    """ step 1 """
    for r in range(N):
        for c in range(N):
            for d, m, s in table[idx][r][c]:
                next_r, next_c = r + s * move[d][0], c + s * move[d][1]
                table[idx+1][(next_r+N)%N][(next_c+N)%N].append((d, m, s))

    """ step 2 """
    for r in range(N):
        for c in range(N):
            if len(table[idx+1][r][c]) > 1:
                total_m, total_s, count = 0, 0, 0
                prev_d = table[idx+1][r][c][0][0] % 2
                total_d = 0
                for d, m, s in table[idx+1][r][c]:
                    total_m += m
                    total_s += s
                    count += 1
                    if d % 2 != prev_d:
                        total_d = 1
                table[idx+1][r][c] = []
                if total_m >= 5:
                    for i in range(4):
                        table[idx+1][r][c].append((2*i+total_d, total_m//5, total_s//count))

answer = 0
for r in range(N):
    for c in range(N):
        for d, m, s in table[K][r][c]:
            answer += m

print(answer)