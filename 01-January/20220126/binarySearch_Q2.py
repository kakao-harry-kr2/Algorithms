import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))

start, end = 0, max(numList)
answer = 0

while start <= end:
    mid = (start + end) // 2

    length = 0
    for num in numList:
        length += max(0, num - mid)
    
    if length < M:
        end = mid - 1
    else:
        answer = mid
        start = mid + 1

print(int(answer))