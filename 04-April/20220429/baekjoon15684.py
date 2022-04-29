# 01:15:00

from itertools import combinations

N, M, H = map(int, input().split())
table = [[-1] * N for _ in range(H)]

for _ in range(M):
    a, b = map(int, input().split())
    table[a-1][b-1], table[a-1][b] = b, b-1

count = [0] * N
for i in range(H):
    for j in range(N):
        if table[i][j] != -1:
            count[j] = (count[j] + 1) % 2

if count.count(1) > 6:
    print(-1)
    exit()

must_needed = False
if count.count(1) > 4:
    must_needed = True

dotted = []
for i in range(H):
    for j in range(N-1):
        if must_needed and count[j] + count[j+1] < 2:
            continue

        if table[i][j] == -1 and table[i][j+1] == -1:
            dotted.append((i, j))

for cnt in range(4):
    for comb in combinations(dotted, cnt):
        possible = True
        for i, j in comb:
            if table[i][j] != -1 or table[i][j+1] != -1:
                possible = False
                break
            table[i][j], table[i][j+1] = j+1, j
        
        if not possible:
            for i, j in comb:
                table[i][j], table[i][j+1] = -1, -1
            continue

        # 확인
        for idx in range(N):
            j = idx
            for i in range(H):
                if table[i][j] == -1:
                    continue
                
                j = table[i][j]

            if j != idx:
                possible = False
                break
        
        if possible:
            print(cnt)
            exit()

        for i, j in comb:
            table[i][j], table[i][j+1] = -1, -1

print(-1)