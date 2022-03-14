# 최솟값 찾기

from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
numList = list(map(int, input().split()))

m = deque()
for i in range(N):
    tmp = numList[i]

    while m and m[-1] > tmp:
        m.pop()
    
    m.append(tmp)

    if i >= L and m[0] == numList[i-L]:
        m.popleft()
    
    print(m[0], end=' ')