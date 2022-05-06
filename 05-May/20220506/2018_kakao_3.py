import heapq

def solution(n, t, m, timetable):
    count = [[] for _ in range(n)]

    for time in timetable:
        time = int(time[:2]) * 60 + int(time[3:])
        for k in range(n):
            if time <= 540 + t * k:
                count[k].append(time)
                break
    
    for i in range(n):
        count[i].sort()
    
    for i in range(n-1):
        if len(count[i]) <= m:
            continue

        for time in count[i][m:len(count[i])][::-1]:
            count[i+1] = [time] + count[i+1]

    answer = 0
    if len(count[-1]) < m:
        answer = 540 + (n-1) * t
    else:
        answer = count[-1][m-1] - 1

    return str(answer//60).zfill(2) + ':' + str(answer%60).zfill(2)

print(solution(2, 10, 2, ["08:00", "08:00", "09:10", "09:09", "08:00"]))