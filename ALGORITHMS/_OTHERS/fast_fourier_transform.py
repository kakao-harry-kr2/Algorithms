from cmath import cos, sin, pi

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