import sys
input = sys.stdin.readline

N = int(input())
numList = [False] * 20000000
for n in list(map(int, input().split())):
    numList[n] = True

answer = []

M = int(input())
for n in list(map(int, input().split())):
    if numList[n]:
        answer.append(1)
    else:
        answer.append(0)

print(*answer)