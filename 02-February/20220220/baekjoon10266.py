# 시계 사진들

import sys
input = sys.stdin.readline

# Failure Function
def failureFunc(P):
    m = len(P)
    answer = [0] * m

    i, j = 0, 1

    while j < m:
        while i > 0 and P[i] != P[j]:
            i = answer[i-1]

        if P[i] == P[j]:
            i += 1
            answer[j] = i
        
        j += 1

    return answer

def diff(numList):
    n = len(numList)
    ret = []

    index = 1
    prev, now = numList[0], numList[1]
    while index < n:
        now = numList[index]
        ret.append(now-prev)
        prev = now
        index += 1

    return ret

n = int(input())

numList1 = list(map(int, input().split()))
numList2 = list(map(int, input().split()))

numList1.sort()
numList2.sort()

diff1 = diff(numList1)
diff2 = diff(numList2)

diff1 = diff1 + [360000 + numList1[0] - numList1[-1]] + diff1

F = failureFunc(diff2)

i = 0 # diff1의 index
j = 0 # diff2의 index

while i < 2 * n - 1:
    if diff1[i] == diff2[j]:
        if j == n - 2:
            print("possible")
            exit()
        else:
            i += 1
            j += 1
    
    else:
        # 최소 1개라도 일치한 경우
        if j > 0:
            j = F[j-1]
        else:
            i += 1

print("impossible")