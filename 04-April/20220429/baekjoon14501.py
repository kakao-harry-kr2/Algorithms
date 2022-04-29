# 00:07:33

N = int(input())
time = []
pay = []
for _ in range(N):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

""" idx번째날부터 선택할 수 있고 현재 금액은 current! """
def process(idx, current):
    global answer
    if idx == N:
        if current > answer:
            answer = current
        return

    # idx번째날 상담을 하는 경우
    if idx + time[idx] <= N:
        process(idx + time[idx], current + pay[idx])
    
    # idx번째날 상담을 하지 않는 경우
    process(idx+1, current)

answer = 0
process(0, 0)

print(answer)