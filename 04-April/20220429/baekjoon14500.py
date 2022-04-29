# 00:58:02

N, M = map(int, input().split())
table1 = [list(map(int, input().split())) for _ in range(N)]

def rotate(table):
    row_len = len(table)
    col_len = len(table[0])
    ret = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            ret[c][row_len-1-r] = table[r][c]
    
    return ret

def flip(table):
    ret = []
    for i in range(len(table)):
        ret.append(table[i][::-1])
    
    return ret

table2 = rotate(table1)
table3 = rotate(table2)
table4 = rotate(table3)

answer = 0

""" 1번 """
for table in [table1, table2]:
    for i in range(len(table)):
        for j in range(len(table[0])-3):
            value = sum(table[i][j:j+4])
            answer = max(answer, value)

""" 2번 """
for i in range(N-1):
    for j in range(M-1):
        value = sum(table1[i][j:j+2]) + sum(table1[i+1][j:j+2])
        answer = max(answer, value)

""" 3번, 4번, 5번(90도 반시계방향 회전) : 3x2짜리 """
for table in [table1, table2, table3, table4]:
    for tab in [table, flip(table)]:
        for i in range(len(tab)-2):
            for j in range(len(tab[0])-1):
                value1 = tab[i+2][j] + tab[i+2][j+1]
                value2 = tab[i+1][j+1] + tab[i+2][j+1]
                value3 = tab[i+1][j+1] + tab[i+2][j]
                answer = max(answer, tab[i][j] + tab[i+1][j] + max(value1, value2, value3))

print(answer) 