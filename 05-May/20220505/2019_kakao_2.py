def solution(N, stages):
    current = [0] * (N+2)
    for stage in stages:
        current[stage] += 1

    accumulated = [num for num in current]
    for i in reversed(range(1, N+1)):
        accumulated[i] += accumulated[i+1]

    failure_ratio = []
    for i in range(1, N+1):
        if accumulated[i] != 0:
            failure_ratio.append((-(current[i] / accumulated[i]), i))
        else:
            failure_ratio.append((0, i))
    
    failure_ratio.sort()

    answer = [num for ratio, num in failure_ratio]

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))