import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    numList = [input().rstrip() for _ in range(n)]
    numList.sort()
    consistency = 1
    for i in range(n-1):
        if len(numList[i]) <= len(numList[i+1]) and numList[i] == numList[i+1][:len(numList[i])]:
            consistency = 0
            break
    print("YES" if consistency else "NO")