import time

def solution(k, room_number):
    answer = []

    rn2next = dict()
    for rn in room_number:
        trace = []
        while True:
            try:
                trace.append(rn)
                rn = rn2next[rn]
            except:
                answer.append(rn)
                for t in trace:
                    rn2next[t] = rn + 1
                break

    return answer

start = time.time()
solution(10**12, [1]*200000)
end = time.time()

print(end-start)