def solution(lines):
    checkTime = []
    for line in lines:
        _, S, T = line.split()
        endTime = ((int(S[:2]) * 60 + int(S[3:5])) * 60 + int(S[6:8])) * 1000 + int(S[9:])
        duration = int(float(T[:-1]) * 1000) - 1
        startTime = endTime - duration
        checkTime.append((startTime, -1))
        checkTime.append((endTime + 999, 1))
    
    checkTime.sort()

    answer = 0
    count = 0
    for time, t in checkTime:
        if t == -1:
            count += 1
            answer = max(answer, count)
        
        elif t == 1:
            count -= 1

    return answer

lines = [
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]
print(solution(lines))