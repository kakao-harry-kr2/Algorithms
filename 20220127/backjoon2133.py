N = int(input())

if N % 2 == 1:
    print(0)
    exit()

n = N // 2
a = [1] * (n+1)

for i in range(1, n+1):
    a[i] = a[i-1] + 2 * sum(a[:i])

print(a[n])