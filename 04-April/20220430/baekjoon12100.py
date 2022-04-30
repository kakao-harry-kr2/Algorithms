# 00:47:57

import math, sys, copy
sys.setrecursionlimit(10 ** 4)

N = int(input())
fixed_table = [list(map(lambda x: int(math.log2(int(x))) if x != '0' else 0, input().split())) for _ in range(N)]
answer = 0

def rotate(table):
    global N
    ret = [[None] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            ret[j][N-1-i] = table[i][j]
    
    return ret

def process(idx, dirs):
    if idx == 5:
        table = copy.deepcopy(fixed_table)
        for dir in dirs:
            for _ in range(dir):
                table = rotate(table)
            
            for r in range(N):
                j = 0
                new_row = []
                notZero = [table[r][c] for c in range(N) if table[r][c] != 0]
                length = len(notZero)
                while j < length:
                    if j < length - 1 and notZero[j] == notZero[j+1]:
                        new_row.append(notZero[j]+1)
                        j += 2
                    else:
                        new_row.append(notZero[j])
                        j += 1
                
                new_row += [0] * (N - len(new_row))
                table[r] = new_row

            for _ in range(4-dir):
                table = rotate(table)
        
        global answer
        for i in range(N):
            answer = max(answer, max(table[i]))

        return

    for i in range(4):
        process(idx+1, dirs + [i])

process(0, [])

print(int(2 ** answer))