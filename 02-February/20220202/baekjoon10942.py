import sys
input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))

table_odd = [0] * N

for i in range(N):
    # i를 중심으로 팰린드롬을 이루는가?
    answer = 0
    for j in range(1, min(i+1, N-i)):
        if numList[i-j] == numList[i+j]:
            answer += 1
        else:
            break
    table_odd[i] = answer

table_even = [0] * (N - 1)

for i in range(N-1):
    # i, i+1을 중심으로 팰린드롬을 이루는가?
    answer = 0
    for j in range(min(i+1, N-1-i)):
        if numList[i-j] == numList[i+1+j]:
            answer += 1
        else:
            break
    table_even[i] = answer

M = int(input())

for _ in range(M):
    start, end = map(int, input().split())
    if (end - start) % 2 == 0:
        mid = (start + end) // 2
        if mid - start > table_odd[mid-1]:
            print(0)
        else:
            print(1)

    else:
        mid = (start + end) // 2
        if mid - start < table_even[mid-1]:
            print(1)
        else:
            print(0)