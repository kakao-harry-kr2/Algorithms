import time, random

INF = 10 ** 9

def solution(stones, k):
    answer = 0
    stones = [INF] + stones + [INF]
    dest = len(stones) - 1

    start, end = 1, 2 * 10 ** 8
    while start <= end:
        mid = (start + end) // 2
        now = 0
        diff = 1
        while diff <= k:
            if stones[now+diff] >= mid:
                now += diff
                if now == dest:
                    answer = mid
                    break
                diff = 1
            else:
                diff += 1

        if answer == mid:
            start = mid + 1
        else:
            end = mid - 1

    return answer

stones = [2 * 10 ** 8] * 2*10**5

start = time.time()
print(solution(stones, 3))
end = time.time()

print(end-start)