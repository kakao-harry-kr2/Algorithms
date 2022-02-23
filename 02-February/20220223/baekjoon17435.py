# 합성함수와 쿼리

import sys
input = sys.stdin.readline

m = int(input())

# table[i][j] : f_(2^i)[j]의 값
table = [[None] * (m + 1) for _ in range(19)]

table[0] = [None] + list(map(int, input().split()))

for i in range(1, 19):
    for j in range(1, m + 1):
        table[i][j] = table[i-1][table[i-1][j]]

Q = int(input())
for _ in range(Q):
    n, x = map(int, input().split())

    for i in range(19):
        if 1 & (n >> i):
            x = table[i][x]
    
    print(x)
