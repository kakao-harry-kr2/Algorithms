""" 
두 개의 queue가 존재하는데
각 queue에서 숫자를 하나씩 제거해서 다른 queue에 추가할 수 있을 때
각 queue의 합이 같도록 하는 시행 횟수의 최솟값은 얼마인가?
불가능한 경우 -1
"""

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)

    average = (sum1 + sum2) // 2
    diff = sum1 - average

    q1 = queue1 + queue2
    q2 = queue2 + queue1

    N = len(q1)

    i, j = 0, 0
    while i < N or j < N:
        if diff == 0:
            return i + j
        
        elif i < N and diff > 0:
            diff -= q1[i]
            i += 1
        
        elif j < N and diff < 0:
            diff += q2[j]
            j += 1
        
        else:
            break

    return -1

print(solution([3,2,7,2], [4,6,5,1])) # 2
print(solution([1,2,1,2], [1,10,1,2])) # 7
print(solution([1,1], [1,5])) # -1