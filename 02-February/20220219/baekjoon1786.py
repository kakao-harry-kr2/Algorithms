# 찾기

import sys
input = sys.stdin.readline

T = input().rstrip()
P = input().rstrip()

n = len(T)
m = len(P)

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

F = failureFunc(P)

def KMP(T, P):
    i = 0 # T의 index
    j = 0 # P의 index

    answer = []

    while i < n:
        if T[i] == P[j]:
            if j == m - 1:
                answer.append(i - j + 1)
                i = i + 1
                j = F[j]
            else:
                i += 1
                j += 1
        
        else:
            # 최소 1개라도 일치한 경우
            if j > 0:
                j = F[j-1]
            else:
                i += 1
    
    return answer

answer = KMP(T, P)

print(len(answer))
print(*answer)