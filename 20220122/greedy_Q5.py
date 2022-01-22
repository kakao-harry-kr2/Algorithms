N, M = map(int, input().split())
ballList = list(map(int, input().split()))

freqList = [0] * M
for ball in ballList:
    freqList[ball-1] += 1

answer = N * (N-1) // 2
for freq in freqList:
    answer -= max(0, freq * (freq-1) // 2)

print(answer)