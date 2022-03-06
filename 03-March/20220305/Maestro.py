from itertools import combinations
import time
import random

# N = int(input())
# Cal = list(map(int, input().split()))

N = 100
Cal = [random.randint(1, 2498) for _ in range(N)]

start = time.time()

li = [0] * 2500

for c in Cal:
    li[c] += 1

summation = [0] * 2500

for i in range(1, 2500):
    summation[i] = summation[i-1] + li[i]

count = 0
for i in range(2500):
    if li[i] == 0: continue
    for j in range(i, 2500):
        if li[j] == 0: continue
        if i + j >= 2500: continue
        elif i + j >= 2000:
            s = summation[2500-i-j]
            if i <= 2500-i-j: s -= 1
            if j <= 2500-i-j: s -= 1
            if i != j:
                count += s * li[i] * li[j]
            else:
                count += s * li[i] * (li[i] - 1) // 2
        else:
            s = summation[2500-i-j] - summation[1999-i-j]
            if 2000-i-j <= i <= 2500-i-j: s -= 1
            if 2000-i-j <= j <= 2500-i-j: s -= 1
            if i != j:
                count += s * li[i] * li[j]
            else:
                count += s * li[i] * (li[i] - 1) // 2

end = time.time()

print(end-start)

print(count//3)

answer = 0
for comb in combinations(Cal, 3):
    if 2000 <= sum(comb) <= 2500:
        answer += 1

print(answer)