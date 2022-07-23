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
x = list(map(int, input().split()))
y = list(map(int, input().split()))

# preprocessing
total_size = 2 ** 17
x += [0] * (total_size - N)
y = y[::-1] + [0] * (total_size - 2 * N) + y[::-1]

fft_x = fft(x)
fft_y = fft(y)
z = list(map(lambda w: round(w.real), ifft([fft_x[i] * fft_y[i] for i in range(total_size)])))

answer = max(z)
print(answer)