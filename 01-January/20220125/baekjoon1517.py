import time
from random import randint
import sys

def merge_sort(start, end):
    global swap_count, numList

    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid + 1, end)

        a, b = start, mid + 1
        temp = []

        while a <= mid and b <= end:
            if numList[a] <= numList[b]:
                temp.append(numList[a])
                a += 1
            else:
                temp.append(numList[b])
                b += 1
                swap_count += (mid - a + 1)

        if a <= mid:
            temp = temp + numList[a:mid + 1]
        if b <= end:
            temp = temp + numList[b:end + 1]

        for i in range(len(temp)):
            numList[start + i] = temp[i]

input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

swap_count = 0
merge_sort(0, N-1)

print(swap_count)