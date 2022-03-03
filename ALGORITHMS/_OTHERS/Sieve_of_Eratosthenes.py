""" N보다 작은 소수들 """

def prime_list(N):
    # 에라토스테네스의 체 초기화: N개 요소에 True 설정(소수로 간주)
    sieve = [True] * N
    # N의 최대 약수가 sqrt(N) 이하이므로 i = sqrt(N)까지 검사
    m = int(N ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True: # i가 소수인 경우
            for j in range(i*i, N, i):
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, N) if sieve[i] == True]

print(prime_list(19))