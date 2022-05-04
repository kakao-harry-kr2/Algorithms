answer = 16

def solution_impl(weak, checked:list, dist, used:list):
    # 마지막 취약 지점까지 모두 점검한 경우
    if checked[-1]:
        used_count = used.count(True)
        global answer
        if used_count < answer:
            answer = used_count
        
        return

    for i in range(len(used)):
        # i번째 친구를 투입하지 않았다면
        if not used[i]:
            index_to_be_checked = checked.index(False)
            j = index_to_be_checked
            used[i] = True
            checked[j] = True
            while j + 1 < len(weak) and weak[j+1] - weak[index_to_be_checked] <= dist[i]:
                checked[j+1] = True
                j += 1
            
            solution_impl(weak, checked, dist, used)

            for j in range(index_to_be_checked, len(weak)):
                checked[j] = False

            used[i] = False

def solution(n, weak, dist):
    global answer
    for i in range(len(weak)):
        reordered_weak = sorted([(num - weak[i] + n) % n for num in weak])
        solution_impl(reordered_weak, [False] * len(weak), dist, [False] * len(dist))
    
    return answer if answer != 16 else -1

print(solution(12, [1,5,6,10], [1,2,3,4]))
print(solution(12, [1,3,4,9,10], [3,5,7]))