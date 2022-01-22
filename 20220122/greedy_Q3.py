import sys
input = sys.stdin.readline

inputStr = input().rstrip()
answer, type = 1, inputStr[0]

for i in range(1, len(inputStr)):
    if inputStr[i] != type:
        answer += 1
        type = inputStr[i]

print(answer//2)