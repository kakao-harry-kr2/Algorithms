def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    average = (sum1 + sum2) // 2
    diff = sum1 - average

    q1 = queue1 + queue2
    q2 = queue2 + queue1
    L = len(q1)

    i, j = 0, 0
    while i < L or j < L:
        if diff == 0:
            return i + j

        elif i < L and diff > 0:
            diff -= q1[i]
            i += 1
        
        elif j < L and diff < 0:
            diff += q2[j]
            j += 1
        
        else:
            break
            
    return -1

print(solution([3,2,7,2], [4,6,5,1]))
print(solution([1,2,1,2], [1,10,1,2]))
print(solution([1,1], [1,5]))