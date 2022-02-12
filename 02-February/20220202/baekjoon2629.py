import copy
import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

M = int(input())
checkList = list(map(int, input().split()))

# i를 측정할 수 있는가?
table = [0] * 30001
table[0] = 1

for num in reversed(numList):
    new_table = copy.deepcopy(table)
    for i in range(30001):
        if table[i] == 1:
            if -15000 <= i - num <= 15000:
                new_table[i - num] = 1
            if -15000 <= i + num <= 15000:
                new_table[i + num] = 1
    table = copy.deepcopy(new_table)

for check in checkList:
    if check > 15000:
        print('N', end=' ')
        continue

    if table[check] == 1 or table[-check] == 1:
        print('Y', end=' ')
    else:
        print('N', end=' ')