import sys
input = sys.stdin.readline

N = int(input())
table = [list(input().split()) for _ in range(N)]

table.sort(key=lambda x: int(x[1]))

for p in table:
    print(p[0], end=' ')