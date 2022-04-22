N, M = map(int, input().split())

table = [list(map(int, input().split())) for _ in range(N)]

clouds = [[False] * N for _ in range(N)]
clouds[N-1][0], clouds[N-1][1], clouds[N-2][0], clouds[N-2][1] = True, True, True, True

move = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]

for _ in range(M):
    d, s = map(int, input().split())

    """ step 1 """
    clouds = [[clouds[(i-s*move[d-1][0]+N)%N][(j-s*move[d-1][1]+N)%N] for j in range(N)] for i in range(N)]

    """ step 2 """
    for i in range(N):
        for j in range(N):
            if clouds[i][j]:
                table[i][j] += 1
    
    """ step 3 """
    
    """ step 4 """
    for i in range(N):
        for j in range(N):
            if clouds[i][j]:
                count = 0
                for k in range(4):
                    next_i, next_j = i + move[2*k+1][0], j + move[2*k+1][1]
                    if 0 <= next_i < N and 0 <= next_j < N and table[next_i][next_j] != 0:
                        count += 1
                table[i][j] += count
    
    """ step 5 """
    for i in range(N):
        for j in range(N):
            if clouds[i][j]:
                clouds[i][j] = False
            else:
                if table[i][j] >= 2:
                    clouds[i][j] = True
                    table[i][j] -= 2

answer = 0
for i in range(N):
    answer += sum(table[i])

print(answer)