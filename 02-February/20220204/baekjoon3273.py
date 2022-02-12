import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split()))
x = int(input())

numList.sort()

# numList : 1 2 3 5 7 9 10 11 12
# x = 13
i, j = 0, n-1
count = 0

while i < j:
    value = numList[i] + numList[j]
    if value == x:
        count += 1
        i += 1
        j -= 1
    elif value < x:
        i += 1
    else:
        j -= 1

print(count)