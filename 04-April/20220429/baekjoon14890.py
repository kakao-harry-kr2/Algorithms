# 00:32:20

N, L = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

def transpose(table):
    for i in range(N-1):
        for j in range(i+1, N):
            table[i][j], table[j][i] = table[j][i], table[i][j]

answer = 0
for idx in range(2):
    for r in range(N):
        runway = [False] * N
        road = table[r]
        height = road[0]
        possible = True
        c = 1
        while c < N:
            if abs(road[c] - height) > 1:
                possible = False
                break
            
            if road[c] == height:
                c += 1
                continue
            
            if road[c] > height: # 올라가야함
                if c - L < 0:
                    possible = False
                    break

                for i in range(c-L, c):
                    if runway[i] or table[r][i] != height:
                        possible = False
                        break
                
                if not possible:
                    break
                
                c += 1
                height += 1
            
            else: # 내려가야함
                if c + L > N:
                    possible = False
                    break

                for i in range(c, c+L):
                    if table[r][i] != height - 1:
                        possible = False
                        break
                
                if not possible:
                    break
                
                for i in range(c, c+L):
                    runway[i] = True
                
                c = c + L
                height -= 1

        if possible:
            answer += 1

    if idx == 0:
        transpose(table)

print(answer)