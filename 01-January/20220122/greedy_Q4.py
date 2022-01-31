import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
numList.sort()

sum = 0
for i in range(N):
    if sum < numList[i] - 1:
        break
    
    sum += numList[i]

print(sum+1)
