def str2int(time_str):
    return int(time_str[:2]) * 3600 + int(time_str[3:5]) * 60 + int(time_str[6:8])

def solution(play_time, adv_time, logs):
    play_time_sec = str2int(play_time)
    adv_time_sec = str2int(adv_time)

    logs_start_sec = []
    logs_end_sec = []

    for log in logs:
        logs_start_sec.append(str2int(log[:8]))
        logs_end_sec.append(str2int(log[9:]))
    
    total_time = [0] * (play_time_sec + 1)

    # total_time[x] : x 시각에 시작된 재생 구간의 개수 - x 시각에 종료된 재생구간의 개수
    for time in logs_start_sec:
        total_time[time] += 1
    for time in logs_end_sec:
        total_time[time] -= 1

    # 시각 x부터 x+1까지 1초 간의 구간을 포함하는 재생 구간의 개수
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]
    
    # 시각 0부터 x+1까지 x+1초 간의 구간을 포함하는 누적 재생시간
    for i in range(1, play_time_sec):
        total_time[i] = total_time[i] + total_time[i-1]
    
    # 시각 0부터 x까지 x초 간의 구간을 포함하는 누적 재생시간
    total_time = [0] + total_time

    max_time, answer = 0, 0
    for i in range(adv_time_sec, play_time_sec + 1):
        value = total_time[i] - total_time[i - adv_time_sec]
        if value > max_time:
            max_time = value
            answer = i - adv_time_sec
    
    HH = answer // 3600
    MM = (answer % 3600) // 60
    SS = answer % 60

    time = [HH, MM, SS]
    for i in range(3):
        if time[i] == 0:
            time[i] = "00"
        elif time[i] < 10:
            time[i] = '0' + str(time[i])
        else:
            time[i] = str(time[i])

    return time[0] + ':' + time[1] + ':' + time[2]

play_time = "02:03:55"
adv_time = "00:14:15"
logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]

print(solution(play_time, adv_time, logs))

play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]

print(solution(play_time, adv_time, logs))

play_time = "50:00:00"
adv_time = "50:00:00"
logs = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

print(solution(play_time, adv_time, logs))