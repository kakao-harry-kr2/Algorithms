import sys
input = sys.stdin.readline

N, M = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(N)]

summation = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        summation[i][j] = summation[i][j-1] + summation[i-1][j] - summation[i-1][j-1] + table[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(lambda x: int(x)-1, input().split())
    print(summation[x2][y2] - summation[x2][y1-1] - summation[x1-1][y2] + summation[x1-1][y1-1])