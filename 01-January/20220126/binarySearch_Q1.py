import random
import time
import sys
input = sys.stdin.readline

def binary_search(numList, target):
    start, end = 0, N-1
    while start <= end:
        mid = (start + end) // 2
        if numList[mid] == target:
            return 1
        elif numList[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

# N = int(input())
# numList = list(map(int, input().split()))
# M = int(input())
# findList = list(map(int, input().split()))

# 시간 초과 테스트
N = 1000000
numList = [random.randint(1, 1000000) for _ in range(N)]
M = 1000000
findList = [random.randint(1, 1000000) for _ in range(M)]

""" 다른 풀이 : 계수 정렬 """
start1 = time.time()

array = [0] * 1000001
for num in numList:
    array[num] = 1

for find in findList:
    answer = "yes" if array[find] else "no"

end1 = time.time()

print("계수 정렬 :", end1-start1)

""" 내 풀이 : 이진 탐색 """
start2 = time.time()

numList.sort()

for find in findList:
    answer = "yes" if binary_search(numList, find) else "no"

end2 = time.time()

print("이진 탐색 :", end2-start2)

""" 다른 풀이 : 집합 """
start3 = time.time()
array = set(numList)

for find in findList:
    answer = "yes" if find in numList else "no"

end3 = time.time()
print("집합 :", end3-start3)

# 계수 정렬 : 0.13995790481567383
# 이진 탐색 : 2.7034082412719727
# 집합 : X