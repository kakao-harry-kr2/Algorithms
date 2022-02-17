# 집합

import sys
input = sys.stdin.readline

S = [False] * 21

M = int(input())

for _ in range(M):
    inputStr = input().rstrip()

    if inputStr[0] == 'a' and len(inputStr) != 3:
        S[int(inputStr.split()[1])] = True
    elif inputStr[0] == 'r':
        S[int(inputStr.split()[1])] = False
    elif inputStr[0] == 'c':
        answer = S[int(inputStr.split()[1])]
        print(1 if answer else 0)
    elif inputStr[0] == 't':
        S[int(inputStr.split()[1])] = not S[int(inputStr.split()[1])]
    elif inputStr[0] == 'a':
        S = [True] * 21
    else:
        S = [False] * 21