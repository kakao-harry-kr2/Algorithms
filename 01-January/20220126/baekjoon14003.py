from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

li = [-1e9-1]
place = [-1] * N

for i, num in enumerate(numList):
    if li[-1] < num:
        li.append(num)
        place[i] = len(li) - 1

    else:
        index = bisect_left(li, num)
        li[index] = num
        place[i] = index

li = li[1:]
answer = []
value, index = len(li), N-1
print(value)

while value > 0:
    while place[index] != value:
        index -= 1
    answer.append(numList[index])
    value -= 1

for ans in answer[::-1]:
    print(ans, end=' ')