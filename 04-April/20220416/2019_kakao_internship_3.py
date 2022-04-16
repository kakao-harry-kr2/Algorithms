def process(count, included, idx, answer:set):
    if idx == len(count):
        answer.add(''.join(list(map(str, sorted(included)))))
        return

    ans = 0
    for id in count[idx]:
        if id not in included:
            process(count, included + [id], idx+1, answer)
    
    return ans

def solution(user_id, banned_id):
    count = [[] for _ in range(len(banned_id))]

    for idx1, bid in enumerate(banned_id):
        for idx2, uid in enumerate(user_id):
            if len(bid) != len(uid):
                continue
            
            is_same = True
            for i in range(len(bid)):
                if bid[i] == '*':
                    continue
                
                if bid[i] != uid[i]:
                    is_same = False
                    break
            
            if is_same:
                count[idx1].append(idx2)

    answer = set()

    process(count, [], 0, answer)

    return len(list(answer))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]
print(solution(user_id, banned_id))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
print(solution(user_id, banned_id))

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
print(solution(user_id, banned_id))