# 소수의 연속합

N = int(input())

if N == 1:
    print(0)
    exit()

count = 0

# 에라토스테네스의 채 : N이하의 소수들
isPrime = [1 for _ in range(N+1)]
primeList = []

num = 2
while num <= N:
    primeList.append(num)
    for i in range(num * num, N+1, num):
        isPrime[i] = 0
    num += 1
    while num <= N and isPrime[num] != 1:
        num += 1

i, j = 0, 0
value = primeList[0]

while i <= j:
    if value >= N:
        if value == N:
            count += 1
        value -= primeList[i]
        i += 1
    else:
        j += 1
        if j == len(primeList):
            break
        value += primeList[j]

print(count)