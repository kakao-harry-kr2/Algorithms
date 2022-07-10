n = int(input())

f = [1] * (n+1)
for i in range(3, n+1):
    f[i] = f[i-1] + f[i-2]

print(f[n], n-2)