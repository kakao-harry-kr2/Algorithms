# 문자열 제곱

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

    return m, answer

while True:
    s = input().rstrip()

    if s == '.':
        break

    total, F = failureFunc(s)
    
    # 반복되는 문자열의 길이
    m = total - F[-1]

    if total % m == 0:
        print(total // m)
    else:
        print(1)