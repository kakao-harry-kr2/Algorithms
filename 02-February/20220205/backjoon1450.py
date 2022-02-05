# 냅색 문제
from itertools import combinations
import sys
input = sys.stdin.readline

N, C = map(int, input().split())
weights = list(map(int, input().split()))

# 두 개의 부분집합으로 나누기
weight_A = weights[:N//2]
weight_B = weights[N//2:]

len_A = len(weight_A)
len_B = len(weight_B)

subset_A = []
subset_B = []

for num in range(len_A+1):
    for subset in combinations(weight_A, num):
        subset_A.append(sum(subset))

for num in range(len_B+1):
    for subset in combinations(weight_B, num):
        subset_B.append(sum(subset))

subset_A.sort()

answer = 0

for sum_subset in subset_B:
    remainder = C - sum_subset

    if remainder < 0:
        continue

    # subset_A에서 값이 remainder이하인 것의 개수 파악
    count = 0
    start, end = 0, len(subset_A)- 1
    while start <= end:
        mid = (start + end) // 2
        if subset_A[mid] <= remainder:
            count = mid + 1
            start = mid + 1
        else:
            end = mid - 1
    
    answer += count

print(answer)