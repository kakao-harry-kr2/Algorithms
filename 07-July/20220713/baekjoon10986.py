import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numList = list(map(int, input().split()))

# remList[k]: 누적합의 나머지가 k가 되는 경우의 수
remList = [1] + [0] * (M - 1)
acc = 0
for i in range(N):
    acc = (acc + numList[i]) % M
    remList[acc] += 1

answer = 0
for rem in remList:
    answer += rem * (rem-1) // 2

print(answer)