N, K = map(int, input().split())
numList = list(map(int, input().split()))

i, j = 0, K
summation = answer = sum(numList[:K])

while j < N:
    summation += (numList[j] - numList[i])
    answer = max(answer, summation)

    i += 1
    j += 1

print(answer)