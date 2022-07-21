from numpy.fft import fft, ifft
import sys
input = sys.stdin.readline

N = int(input())

x = [0] * 2 ** 18
x[0] = 1
for _ in range(N):
    x[int(input())] = 1

fft_x = fft(x)

y = ifft(fft_x ** 2).real

available = [0] * 2 ** 18
for i in range(2 ** 18):
    if abs(y[i]) > 0.5:
        available[i] = 1

M = int(input())
answer = 0
for _ in range(M):
    if available[int(input())]:
        answer += 1

print(answer)