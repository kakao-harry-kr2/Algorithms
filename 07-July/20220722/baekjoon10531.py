from cmath import cos, sin, pi
import sys
input = sys.stdin.readline

def fft_impl(x, w):
    N = len(x)

    if N == 1:
        return x

    x_even = fft_impl(x[::2], w * w)
    x_odd = fft_impl(x[1::2], w * w)

    factor = [1]
    for _ in range(N//2-1):
        factor.append(factor[-1]*w)

    ret = [x_even[n] + factor[n] * x_odd[n] for n in range(N//2)] + [x_even[n] - factor[n] * x_odd[n] for n in range(N//2)]
    
    return ret

def fft(x):
    N = len(x)
    w = complex(cos(2 * pi / N), sin(2 * pi / N))

    return fft_impl(x, w)

def ifft(x):
    N = len(x)
    w = complex(cos(2 * pi / N), -sin(2 * pi / N))

    return list(map(lambda x: x/N, fft_impl(x, w)))

N = int(input())

x = [0] * (2 ** 19)
x[0] = 1
for _ in range(N):
    x[int(input())] = 1

fft_x = fft(x)

available = list(map(lambda x: 1 if round(x.real) > 0 else 0, ifft(list(map(lambda x: x ** 2, fft_x)))))

M = int(input())
answer = 0
for _ in range(M):
    if available[int(input())]:
        answer += 1

print(answer)