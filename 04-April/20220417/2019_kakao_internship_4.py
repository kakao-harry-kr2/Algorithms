import time

def solution(k, room_number):
    answer = []

    ordered_list = []
    for idx, rn in enumerate(room_number):
        start, end = 0, idx - 1
        while True:
            if start > end:
                # rn이 배정되지 않은 경우
                answer.append(rn)
                ordered_list.insert(start, rn)
                break

            mid = (start + end) // 2

            if rn == ordered_list[mid]:
                # rn이 이미 배정된 경우
                i, j = mid, idx - 1
                s = i
                while i <= j:
                    m = (i + j) // 2
                    if ordered_list[m] - rn == m - mid:
                        s = m
                        i = m + 1
                    else:
                        j = m - 1

                answer.append(ordered_list[s]+1)
                ordered_list.insert(s+1, ordered_list[s]+1)
                break

            elif rn < ordered_list[mid]:
                end = mid - 1
            
            else:
                start = mid + 1

    return answer

start = time.time()
solution(10**12, [1]*200000)
end = time.time()

print(end-start)