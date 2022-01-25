import sys
input = sys.stdin.readline

N = int(input())
numList = [int(input()) for _ in range(N)]

sortedList = sorted(numList, reverse=True)
for num in sortedList:
    print(num, end=' ')