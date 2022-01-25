import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

for i in range(N):
    numList[i] = [abs(numList[i]), 1 if numList[i] > 0 else -1]

numList.sort()

value = 2000000000
answer = [0, 0]
for i in range(N-1):
    if numList[i][1] == numList[i+1][1] and numList[i][0] + numList[i+1][0] < value:
        value = numList[i][0] + numList[i+1][0]
        answer = [numList[i][0]*numList[i][1], numList[i+1][0]*numList[i+1][1]]
    if numList[i][1] != numList[i+1][1] and numList[i+1][0] - numList[i][0] < value:
        value = numList[i+1][0] - numList[i][0]
        answer = [numList[i][0]*numList[i][1], numList[i+1][0]*numList[i+1][1]]

print(min(answer), max(answer))