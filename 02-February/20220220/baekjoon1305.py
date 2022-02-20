# 광고

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

L = int(input())
s = input().rstrip()

F = failureFunc(s)

# 반복되는 문자열의 길이
m = L - F[-1]
print(m)