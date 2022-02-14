# 오븐 시계

h, m = map(int, input().split())
minutes = int(input())

total = 60 * h + m + minutes

M = total % 60
H = int((total - M) / 60) % 24

print(H, M)