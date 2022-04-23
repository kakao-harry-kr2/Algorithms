import sys
sys.setrecursionlimit(10000)

N, Q = map(int, input().split())
n = 2 ** N
move = [(0, -1), (-1, 0), (0, 1), (1, 0)]

def rotate_mat(table, x, y, l):
    mat = [[table[x+i][y+j] for j in range(l)] for i in range(l)]
    for i in range(l):
        for j in range(l):
            table[x+j][y+l-1-i] = mat[i][j]

def rotate_tab(table, l):
    for x in range(n//l):
        for y in range(n//l):
            rotate_mat(table, l*x, l*y, l)

def melt(table):
    melt_mat = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            count = 0
            for k in range(4):
                next_i, next_j = i + move[k][0], j + move[k][1]
                if 0 <= next_i < n and 0 <= next_j < n:
                    if table[next_i][next_j] > 0:
                        count += 1
            if count < 3:
                melt_mat[i][j] = -1
    
    for i in range(n):
        for j in range(n):
            table[i][j] = max(0, table[i][j] + melt_mat[i][j])

def bfs(i, j, visited, group:list):
    visited[i][j] = True
    group.append((i, j))
    for k in range(4):
        next_i, next_j = i + move[k][0], j + move[k][1]
        if 0 <= next_i < n and 0 <= next_j < n and not visited[next_i][next_j] and table[next_i][next_j] > 0:
            bfs(next_i, next_j, visited, group)

table = [list(map(int, input().split())) for _ in range(n)]
L_list = list(map(int, input().split()))

for L in L_list:
    rotate_tab(table, 2**L)
    melt(table)

total = 0
for i in range(n):
    for j in range(n):
        total += table[i][j]
print(total)

groups = [0]
visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and table[i][j] > 0:
            group = []
            bfs(i, j, visited, group)
            groups.append(len(group))

print(max(groups))